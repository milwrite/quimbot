(function(){
  const PASS = 'gutenberg';
  const REPO = 'milwrite/quimbot';
  const PATH = 'docs/cloze-reader-draft/index.html';
  const LS_PAT = '__editor_pat';
  const LS_SHA = '__editor_sha';
  const EDITABLE = 'h1,h2,p,pre,code,.ref,figcaption';
  let editMode = false;

  /* ── inject chrome ── */
  const lock = document.createElement('button');
  lock.id = '__lock'; lock.title = 'Edit mode'; lock.textContent = '🔒';
  document.body.appendChild(lock);

  const hlbar = document.createElement('div');
  hlbar.id = '__hlbar';
  hlbar.innerHTML = '<button id="__hlbtn">✦ highlight</button>';
  document.body.appendChild(hlbar);

  const footer = document.createElement('div');
  footer.id = '__footer';
  footer.innerHTML = '<input id="__commitmsg" type="text" placeholder="commit message…" value="draft edit"><button id="__commitbtn">↑ commit</button><span id="__commitstatus"></span>';
  document.body.appendChild(footer);

  const hlbtn   = document.getElementById('__hlbtn');
  const cmsg    = document.getElementById('__commitmsg');
  const cbtn    = document.getElementById('__commitbtn');
  const cstatus = document.getElementById('__commitstatus');

  /* ── auth ── */
  lock.addEventListener('click', () => {
    if (editMode) { exitEdit(); return; }
    const pw = prompt('Password:');
    if (pw !== PASS) { alert('Wrong password.'); return; }
    if (!localStorage.getItem(LS_PAT)) {
      const pat = prompt('GitHub token (one-time setup):');
      if (!pat) return;
      localStorage.setItem(LS_PAT, pat.trim());
    }
    enterEdit();
  });

  function enterEdit() {
    editMode = true;
    lock.textContent = '🔓';
    lock.style.opacity = '0.7';
    document.querySelectorAll(EDITABLE).forEach(el => {
      el.setAttribute('contenteditable', 'true');
      el.setAttribute('spellcheck', 'true');
      const wrap = document.createElement('div');
      wrap.className = 'block-wrap';
      const btn = document.createElement('button');
      btn.className = 'block-del';
      btn.title = 'Delete block';
      btn.textContent = '✕';
      btn.addEventListener('click', e => {
        e.stopPropagation();
        if (confirm('Delete this block?')) wrap.remove();
      });
      el.parentNode.insertBefore(wrap, el);
      wrap.appendChild(btn);
      wrap.appendChild(el);
      wrap.addEventListener('mouseenter', () => { btn.style.display = 'block'; });
      wrap.addEventListener('mouseleave', () => { btn.style.display = ''; });
    });
    footer.style.display = 'flex';
  }

  function exitEdit() {
    editMode = false;
    lock.textContent = '🔒';
    lock.style.opacity = '0.25';
    document.querySelectorAll('.block-wrap').forEach(wrap => {
      const el = wrap.querySelector(EDITABLE);
      if (el) {
        el.removeAttribute('contenteditable');
        el.removeAttribute('spellcheck');
        wrap.parentNode.insertBefore(el, wrap);
      }
      wrap.remove();
    });
    document.querySelectorAll('[contenteditable]').forEach(el => {
      el.removeAttribute('contenteditable');
      el.removeAttribute('spellcheck');
    });
    footer.style.display = 'none';
    hlbar.style.display = 'none';
  }

  /* ── highlight toolbar ── */
  document.addEventListener('mouseup', () => {
    if (!editMode) return;
    const sel = window.getSelection();
    if (!sel || sel.isCollapsed || sel.rangeCount === 0) {
      hlbar.style.display = 'none'; return;
    }
    const range = sel.getRangeAt(0);
    const rect = range.getBoundingClientRect();
    hlbar.style.display = 'block';
    hlbar.style.left = (window.scrollX + rect.left) + 'px';
    hlbar.style.top  = (window.scrollY + rect.top - 38) + 'px';
  });

  document.addEventListener('mousedown', e => {
    if (e.target !== hlbtn) hlbar.style.display = 'none';
  });

  hlbtn.addEventListener('mousedown', e => {
    e.preventDefault();
    const sel = window.getSelection();
    if (!sel || sel.isCollapsed) return;
    const range = sel.getRangeAt(0);
    const mark = document.createElement('mark');
    mark.className = 'hl';
    try { range.surroundContents(mark); }
    catch(_) {
      const frag = range.extractContents();
      mark.appendChild(frag);
      range.insertNode(mark);
    }
    sel.removeAllRanges();
    hlbar.style.display = 'none';
  });

  /* ── commit ── */
  cbtn.addEventListener('click', async () => {
    const pat = localStorage.getItem(LS_PAT);
    cbtn.disabled = true;
    cstatus.textContent = 'Fetching SHA…';
    try {
      const metaRes = await fetch(
        `https://api.github.com/repos/${REPO}/contents/${PATH}`,
        { headers: { Authorization: `Bearer ${pat}`, Accept: 'application/vnd.github+json' } }
      );
      if (!metaRes.ok) throw new Error(`GitHub ${metaRes.status}`);
      const meta = await metaRes.json();
      const sha = meta.sha;
      localStorage.setItem(LS_SHA, sha);

      /* serialize — clone, unwrap blocks, strip editor chrome only (not the script tag) */
      const clone = document.documentElement.cloneNode(true);
      clone.querySelectorAll('.block-wrap').forEach(wrap => {
        const child = wrap.querySelector('h1,h2,p,pre,code,.ref,figcaption');
        if (child) {
          child.removeAttribute('contenteditable');
          child.removeAttribute('spellcheck');
          wrap.parentNode.insertBefore(child, wrap);
        }
        wrap.remove();
      });
      clone.querySelectorAll('[contenteditable]').forEach(el => {
        el.removeAttribute('contenteditable');
        el.removeAttribute('spellcheck');
      });
      clone.querySelectorAll('#__lock,#__hlbar,#__footer').forEach(el => el.remove());
      const html = '<!DOCTYPE html>\n' + clone.outerHTML;

      const b64 = btoa(unescape(encodeURIComponent(html)));
      cstatus.textContent = 'Pushing…';
      const msg = cmsg.value.trim() || 'draft edit';
      const putRes = await fetch(
        `https://api.github.com/repos/${REPO}/contents/${PATH}`,
        {
          method: 'PUT',
          headers: {
            Authorization: `Bearer ${pat}`,
            Accept: 'application/vnd.github+json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ message: msg, content: b64, sha })
        }
      );
      if (!putRes.ok) {
        const err = await putRes.json().catch(() => ({}));
        throw new Error(err.message || `GitHub ${putRes.status}`);
      }
      const result = await putRes.json();
      localStorage.setItem(LS_SHA, result.content.sha);
      cstatus.textContent = '✓ committed';
      setTimeout(() => { cstatus.textContent = ''; }, 3000);
    } catch(e) {
      cstatus.textContent = '✗ ' + e.message;
    } finally {
      cbtn.disabled = false;
    }
  });
})();
