from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from agent import agent_executor
import logging
import os
import json
from datetime import datetime
from tools import check_session, is_session_valid
from constants import *
from session import save_sessions

app = Flask(__name__)

# Enable CORS for all routes (you can customize this if needed)
CORS(app)

# Setup Logging
logging.basicConfig(
    filename="agent_interactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


from flask import Flask, request, jsonify
import logging
import json

@app.route("/ask", methods=["POST"])
def handle_query():
    data = request.get_json()

    user_id = data.get("user_id")
    token = data.get("token")
    message = data.get("message")

    if not all([user_id, token, message]):
        return jsonify({"error": "Missing user_id, token or message"}), 400

    print(user_id, token)

    if not is_session_valid(check_session(user_id, token)):
        return jsonify({"error": "Invalid session or token"}), 401

    save_sessions({
        'user_id': user_id,
        'token': token
    })

    logging.info(f"[REQUEST] user_id={user_id}, message={message}")

    try:
        response = agent_executor.invoke({"input": message})

        # Convert the response to JSON-safe format
        def make_json_safe(obj):
            if isinstance(obj, dict):
                return {k: make_json_safe(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [make_json_safe(i) for i in obj]
            elif hasattr(obj, '__dict__'):
                return make_json_safe(vars(obj))
            else:
                return str(obj)

        safe_response = make_json_safe(response)

        logging.info(f"[AGENT RESPONSE] user_id={user_id} -> {safe_response}")
        return jsonify({"response": safe_response}), 200

    except Exception as e:
        logging.error(f"[ERROR] user_id={user_id}, message={message}, error={str(e)}")
        return jsonify({"error": "Agent processing failed", "details": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
