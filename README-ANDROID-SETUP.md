# EchoMind Flask Backend Starter (Android-friendly setup)

## What this starter does
- Adds a separate Python Flask API.
- Includes `/api/health` to verify deployment.
- Includes `/api/study-tip` as a safe test endpoint.
- Does NOT replace your existing HTML/CSS/JavaScript frontend.
- Does NOT change Supabase login, cloud sync, tables, or policies.
- Does NOT contain Supabase keys or other secrets.

## Deploy using only an Android phone
You can upload these files using GitHub's website in your mobile browser, then deploy the repository as a Python Web Service on Render.

### 1. Create a separate GitHub repository
1. Open GitHub in your phone browser and sign in.
2. Create a new repository named `echomind-flask-api`.
3. Keep it separate from the existing website repository for now.
4. Upload `app.py`, `requirements.txt`, `.gitignore`, and optionally `.env.example` from this folder.
5. Do not upload real secrets. This starter does not require any Supabase secret.

### 2. Deploy the Flask API on Render
1. Open the Render Dashboard and choose **New → Web Service**.
2. Connect the new `echomind-flask-api` repository.
3. Choose Python as the runtime.
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
6. Create the service and wait for the deploy to finish.
7. In the service's Environment settings, add:
   - Key: `FRONTEND_ORIGIN`
   - Value: your exact Vercel origin, e.g. `https://echomind-student-hub.vercel.app`
8. Save and redeploy if prompted.

Render's free web services can sleep after inactivity, so the first request after a quiet period may take a little time.

### 3. Test the API
Open this URL in your phone browser, replacing the example host with your actual Render service URL:
`https://YOUR-FLASK-SERVICE.onrender.com/api/health`

Expected JSON:
`{"ok":true,"service":"echomind-flask-api"}`

Then test the POST endpoint from a REST client or the frontend snippet:
`POST https://YOUR-FLASK-SERVICE.onrender.com/api/study-tip`
JSON body:
`{"topic":"C programming pointers"}`

### 4. Connect the existing frontend only after the API test succeeds
1. Copy the real Render URL.
2. In `frontend-integration-example.js`, replace `https://YOUR-FLASK-SERVICE.onrender.com` with your real URL.
3. Test `testEchoMindFlask()` first.
4. Only then add the small fetch call to a suitable feature in a COPY of the frontend, test it, and deploy the copy.
5. Keep your current live Vercel deployment unchanged until the test copy works.

## Supabase safety
Your existing frontend currently handles Supabase authentication and cloud syncing. This starter intentionally leaves that flow alone. Do not put a Supabase `service_role` key in browser JavaScript, a public repository, or this starter. Do not migrate user data or change Row Level Security policies as part of the first test.

## Limits
This is a starter API, not a full conversion of all EchoMind features to Flask. No existing task/note/auth operations are routed through Flask yet. That requires inspecting the current frontend and deciding which specific operation should use the API.
