ECHOMIND STUDENT HUB — RESPONSIVE STUDY WEBSITE
================================================

Features
- Responsive phone and laptop layout
- Task planner, deadlines, priorities and completion tracking
- Save/edit/search study notes by chapter and subject
- Chapter summary helper based on text you saved
- Practice questions extracted from chapter notes, with show/hide answers
- Ask a question and retrieve matching sentences from the selected saved chapter
- Focus timer, session log, progress stats and data export
- Local browser saving and offline-friendly static website

HONEST LIMITATION
The built-in chapter helper is an offline text-extraction helper, not a full AI model. It can summarize and find matching text, but it may miss context or answer incorrectly. Check important answers against your textbook. For true AI-generated summaries and open-ended answers, a secure AI API/backend would need to be connected; do not put a secret API key into public browser code.

PREVIEW ON A LAPTOP
1. Extract this ZIP into a folder.
2. Double-click index.html.
3. It opens in Chrome or Edge. No Python, VS Code, or package installation is required.

USE ON A PHONE
You can preview index.html in a mobile browser only if your phone's file manager/browser permits opening local HTML files. The easiest reliable way is to deploy it online using GitHub + Vercel (steps below), then open the generated HTTPS link on phone and laptop.

PUBLISH ONLINE FROM A PHONE (NO LAPTOP REQUIRED)
1. In your phone browser, sign in to GitHub and create a new repository named echomind-student-hub.
2. Extract this ZIP using your phone's file manager/archive app.
3. Upload the CONTENTS of the EchoMind_Studio folder into the repository root: index.html, manifest.json, icon.svg, sw.js, README.txt. Do not upload only the ZIP file.
4. Sign in to Vercel using GitHub and choose Add New → Project.
5. Import echomind-student-hub. Keep the framework preset as Other. Leave Build Command empty. Use ./ as the output/root directory if asked, then Deploy.
6. Vercel will create a public URL like https://your-project-name.vercel.app. The exact name is chosen by Vercel and may need to be changed if already taken.
7. Open that URL on both phone and laptop. You can use the browser menu → Add to Home screen if offered.

SAVING DATA
Tasks, notes, and study progress are saved in the browser on that device. They do not automatically sync between phone and laptop. Use Export data to make a backup. If you clear browser data, locally saved content may be lost.

SECURITY
This is a static frontend. Do not put passwords, private API keys, or sensitive personal information into it. Public deployments are visible to anyone with the URL.
