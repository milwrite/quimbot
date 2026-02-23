#!/usr/bin/env node
// A2A Bridge for OpenClaw — exposes OpenClaw via Google's Agent2Agent protocol

import http from "node:http";
import { networkInterfaces } from "node:os";
import crypto from "node:crypto";

const A2A_PORT = parseInt(process.env.A2A_PORT || "18800", 10);
const OPENCLAW_URL = process.env.OPENCLAW_URL || "http://127.0.0.1:18789";
const OPENCLAW_TOKEN = process.env.OPENCLAW_GATEWAY_TOKEN || "";

// In-memory task store
const tasks = new Map();

function getLocalIP() {
  for (const ifaces of Object.values(networkInterfaces())) {
    for (const iface of ifaces) {
      if (iface.family === "IPv4" && !iface.internal) return iface.address;
    }
  }
  return "127.0.0.1";
}

function agentCard() {
  return {
    name: "OpenClaw",
    description: "Personal AI assistant (Discord)",
    url: `http://${getLocalIP()}:${A2A_PORT}`,
    version: "1.0.0",
    capabilities: { streaming: false, pushNotifications: false },
    skills: [
      {
        id: "chat",
        name: "General Chat",
        description: "General-purpose AI assistant",
      },
    ],
    securitySchemes: {},
    security: [],
  };
}

function jsonRpcError(id, code, message) {
  return { jsonrpc: "2.0", id, error: { code, message } };
}

function jsonRpcResult(id, result) {
  return { jsonrpc: "2.0", id, result };
}

async function handleTasksSend(params, rpcId) {
  const message = params?.message;
  if (!message || !Array.isArray(message.parts)) {
    return jsonRpcError(rpcId, -32602, "Invalid params: message with parts required");
  }

  const userText = message.parts
    .filter((p) => p.text != null)
    .map((p) => p.text)
    .join("\n");

  if (!userText) {
    return jsonRpcError(rpcId, -32602, "No text content in message parts");
  }

  const taskId = params.id || crypto.randomUUID();

  // Call OpenClaw chat completions
  let assistantText;
  try {
    const res = await fetch(`${OPENCLAW_URL}/v1/chat/completions`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...(OPENCLAW_TOKEN && { Authorization: `Bearer ${OPENCLAW_TOKEN}` }),
      },
      body: JSON.stringify({
        model: "default",
        messages: [{ role: "user", content: userText }],
      }),
    });

    if (!res.ok) {
      const body = await res.text();
      return jsonRpcError(rpcId, -32000, `OpenClaw error ${res.status}: ${body}`);
    }

    const data = await res.json();
    assistantText = data.choices?.[0]?.message?.content || "";
  } catch (err) {
    return jsonRpcError(rpcId, -32000, `Failed to reach OpenClaw: ${err.message}`);
  }

  const task = {
    id: taskId,
    status: { state: "completed" },
    artifacts: [
      {
        parts: [{ type: "text", text: assistantText }],
      },
    ],
    history: [
      message,
      { role: "agent", parts: [{ type: "text", text: assistantText }] },
    ],
  };

  tasks.set(taskId, task);
  return jsonRpcResult(rpcId, task);
}

function handleTasksGet(params, rpcId) {
  const taskId = params?.id;
  if (!taskId) {
    return jsonRpcError(rpcId, -32602, "Missing params.id");
  }
  const task = tasks.get(taskId);
  if (!task) {
    return jsonRpcError(rpcId, -32001, `Task not found: ${taskId}`);
  }
  return jsonRpcResult(rpcId, task);
}

function handleTasksCancel(params, rpcId) {
  const taskId = params?.id;
  if (!taskId) {
    return jsonRpcError(rpcId, -32602, "Missing params.id");
  }
  const task = tasks.get(taskId);
  if (!task) {
    return jsonRpcError(rpcId, -32001, `Task not found: ${taskId}`);
  }
  // Tasks complete synchronously, so cancel is a no-op
  return jsonRpcResult(rpcId, task);
}

async function handleJsonRpc(body, rpcId) {
  const { method, params, id } = body;

  if (!method || id == null) {
    return jsonRpcError(id ?? null, -32600, "Invalid JSON-RPC request");
  }

  switch (method) {
    case "tasks/send":
      return handleTasksSend(params, id);
    case "tasks/get":
      return handleTasksGet(params, id);
    case "tasks/cancel":
      return handleTasksCancel(params, id);
    default:
      return jsonRpcError(id, -32601, `Method not found: ${method}`);
  }
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    req.on("data", (c) => chunks.push(c));
    req.on("end", () => resolve(Buffer.concat(chunks).toString()));
    req.on("error", reject);
  });
}

const server = http.createServer(async (req, res) => {
  // CORS headers for browser-based agents
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    res.writeHead(204);
    res.end();
    return;
  }

  // Agent Card discovery
  if (req.method === "GET" && req.url === "/.well-known/agent.json") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(agentCard(), null, 2));
    return;
  }

  // A2A JSON-RPC endpoint
  if (req.method === "POST" && (req.url === "/" || req.url === "")) {
    let body;
    try {
      const raw = await readBody(req);
      body = JSON.parse(raw);
    } catch {
      res.writeHead(400, { "Content-Type": "application/json" });
      res.end(JSON.stringify(jsonRpcError(null, -32700, "Parse error")));
      return;
    }

    const result = await handleJsonRpc(body);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(result));
    return;
  }

  res.writeHead(404, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ error: "Not found" }));
});

server.listen(A2A_PORT, "0.0.0.0", () => {
  const ip = getLocalIP();
  console.log(`A2A bridge listening on http://0.0.0.0:${A2A_PORT}`);
  console.log(`Agent Card: http://${ip}:${A2A_PORT}/.well-known/agent.json`);
  console.log(`Proxying to OpenClaw at ${OPENCLAW_URL}`);
});
