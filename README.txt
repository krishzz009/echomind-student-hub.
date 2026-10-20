ECHOMIND STUDENT HUB v6
======================

New in v6
- Welcome/sign-in screen shown before the workspace.
- Demo mode works immediately and stores data only in the current browser.
- Optional Supabase email/password account creation and sign-in.
- Optional Google sign-in through Supabase OAuth.
- Optional cloud database sync, with row-level security SQL included.
- Mind Arcade: memory matching, mental maths, and a short breathing reset.
- XP for task completion and focus sessions; level progress and in-app cosmetic/study rewards. No cash, purchases, gambling or promised physical gifts.
- Existing notes/tasks/focus/flashcard/planner features retained.

IMPORTANT AUTH SETUP
This is a static Vercel site. Real account creation, Google login, and cloud sync do not work until you configure your own Supabase project. No credentials are included.
1. Create a project at https://supabase.com/
2. In SQL Editor, run supabase_schema.sql.
3. In Project Settings / API, copy Project URL and the publishable/anon key. Put them in config.js. NEVER use the service_role/secret key in config.js.
4. In Supabase Authentication providers, enable Email. For Google, configure Google OAuth credentials and the authorized redirect URLs as shown by Supabase.
5. In Supabase Auth URL Configuration, add your Vercel site URL (e.g. https://your-project.vercel.app) to Site URL and Redirect URLs.
6. Commit config.js and supabase_schema.sql to your GitHub repo. Since config.js contains only a public client key, the SQL row-level security is essential. Never disable RLS or expose a service role key.

WITHOUT SETUP
The welcome screen offers Demo mode. Data stays in localStorage on that device and does not sync to other devices.

XP & REWARDS
XP is a motivational game mechanic, not an official grade. Completing a task gives 20 XP once per task; a completed focus session gives XP based on session minutes. Arcade games award small fixed XP. Digital rewards are in-app only. Do not promise physical prizes unless a real, fair program is separately arranged.

TESTING NOTES
JavaScript syntax and archive integrity were checked, but this project has not been tested end-to-end in a live browser. Test demo mode first. Test Supabase auth only after configuring providers and URLs. Google login requires OAuth setup by the site owner.

DEPLOY
Upload index.html, sw.js, config.js, README.txt, and supabase_schema.sql to the existing GitHub repository root. Commit. Vercel should deploy automatically. Do not upload only the ZIP.
