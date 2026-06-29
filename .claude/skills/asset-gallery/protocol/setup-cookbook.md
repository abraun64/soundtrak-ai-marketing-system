# Gallery quick-actions setup — one-time, ~2 minutes

Makes the gallery lightbox buttons behave natively:
- **✏️ Edit copy** → opens the `.md` in VS Code (if installed) or Notepad, instead of rendering in the browser
- **📁 Open folder** → opens the asset folder in File Explorer, instead of a browser directory listing

## Step 1 — register the protocol (once)

Double-click this file in File Explorer:

```
C:/Users/<you>\OneDrive\Claude\Marketing AI System\.claude\skills\asset-gallery\protocol\gallery-open.reg
```

Windows will ask "Are you sure you want to continue?" → **Yes** → "keys added successfully" → **OK**.

This writes one user-level registry key (`HKCU\Software\Classes\gallery-open`). No admin rights needed. To undo later: open `regedit`, delete `HKEY_CURRENT_USER\Software\Classes\gallery-open`.

## Step 2 — first click in the browser (once per browser)

The first time you click **Edit copy** or **Open folder** in any gallery, the browser shows a dialog like *"Open gallery-open?"* / *"This site is trying to open an application"*.

- Tick **"Always allow"** (Edge: "Always allow soundtrak gallery pages to open links of this type")
- Click **Open**

After that, both buttons work silently forever.

## What the handler does (and refuses)

`gallery-open.ps1` receives the path, then:
- **Folder** → `explorer.exe <folder>`
- **File** → VS Code if `code` is on PATH, else Notepad
- **Refuses any path outside** `C:/Users/<you>\OneDrive\Claude\Marketing AI System` — a malicious page can't use it to open arbitrary files.

## If nothing happens on click

1. Confirm Step 1 ran (regedit → `HKEY_CURRENT_USER\Software\Classes\gallery-open` exists)
2. Rebuild the gallery (`python .claude/skills/asset-gallery/build-gallery.py --campaign <slug>`) so buttons carry the `gallery-open:` links
3. Check the browser didn't permanently block the protocol (site settings → permissions)
