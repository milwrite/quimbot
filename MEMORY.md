# MEMORY.md

## Discord protocol: communicating with Petrarch (Clawdbot, PI)

**Who is Petrarch (in Discord):**
- Petrarch appears as a bot user: **Clawdbot, PI**
- Discord user/app id: **1464098720340508776**

### Reliable mention / attribution (don’t use plain @handles)
Discord mentions must use the ID form to reliably ping the right entity:
- Mention Petrarch: `<@1464098720340508776>`
- Mention this OpenClaw bot (Quimbot): `<@1467736354766196829>`

(Plain text like `@Petrarch` may not create a real Discord mention and won’t reliably trigger notifications or automation.)

### Bot-to-bot caveat (likely cause of “handle attribution fails”)
Because Petrarch is a bot, **bot-authored messages may be ignored** by default on either side:
- OpenClaw Discord channel config has an `allowBots` flag (if false/omitted, Petrarch’s messages might not trigger OpenClaw).
- Petrarch may also ignore messages authored by bots unless explicitly designed otherwise.

**Practical workaround:**
- Prefer a human to “bridge” by mentioning the other bot with the ID mention, or
- Enable/confirm `channels.discord.allowBots=true` if you want OpenClaw to respond to Petrarch’s bot messages.

### Stand-up / sync message format
When pinging Petrarch for stand-ups (KANBAN sync):
1. Start with an ID mention: `<@1464098720340508776>`
2. State the task explicitly: “sync KANBAN.md”
3. Include the app id for traceability: `app id: 1464098720340508776`
4. Ask for structured output:
   - “Commitment / Blocker / No” or “Done / Next / Blockers”

### Preferred location
- Keep Petrarch coordination inside the relevant Discord thread/channel so both bots can see the same context.
