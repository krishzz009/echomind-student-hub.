// TEST SNIPPET ONLY — do not paste into the live site until Flask is deployed
// and you have replaced FLASK_API_BASE with your real Render URL.
const FLASK_API_BASE = "https://YOUR-FLASK-SERVICE.onrender.com";

async function testEchoMindFlask() {
  const response = await fetch(`${FLASK_API_BASE}/api/health`);
  if (!response.ok) throw new Error(`Flask API returned ${response.status}`);
  return await response.json();
}

async function getEchoMindStudyTip(topic) {
  const response = await fetch(`${FLASK_API_BASE}/api/study-tip`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ topic })
  });
  const result = await response.json();
  if (!response.ok) throw new Error(result.error || "Request failed");
  return result;
}

// Example manual test in your browser console after setting the URL:
// testEchoMindFlask().then(console.log).catch(console.error);
// This test endpoint does not use or modify Supabase data.
