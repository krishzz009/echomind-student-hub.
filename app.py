import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Set FRONTEND_ORIGIN in your hosting dashboard to your exact Vercel URL.
# Example: https://echomind-student-hub.vercel.app
frontend_origin = os.environ.get(
    "FRONTEND_ORIGIN",
    "https://echomind-student-hub.vercel.app"
).rstrip("/")

CORS(
    app,
    resources={r"/api/*": {"origins": [frontend_origin]}},
    methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)


@app.get("/")
def home():
    return jsonify({
        "app": "EchoMind Flask API",
        "status": "running",
        "message": "The API is running separately from the EchoMind frontend."
    })


@app.get("/api/health")
def health():
    return jsonify({"ok": True, "service": "echomind-flask-api"})


@app.post("/api/study-tip")
def study_tip():
    # Example endpoint to prove the frontend can communicate with Flask.
    # This does not read or change Supabase data.
    payload = request.get_json(silent=True) or {}
    topic = str(payload.get("topic", "")).strip()

    if not topic:
        return jsonify({
            "error": "Please provide a topic.",
            "example": {"topic": "C programming pointers"}
        }), 400

    if len(topic) > 200:
        return jsonify({"error": "Topic must be 200 characters or fewer."}), 400

    return jsonify({
        "topic": topic,
        "tip": f"Study {topic} in short sections, then explain the key idea in your own words and solve one practice question.",
        "source": "EchoMind Flask API"
    })


if __name__ == "__main__":
    # Local testing only. Render uses Gunicorn in production.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=False)
