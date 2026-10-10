from flask import Flask, jsonify
import subprocess
import sys
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def run_script():
    print(f"[{datetime.now()}] Starting job...", flush=True)
    try:
        result = subprocess.run(
            ["./gas"],
            capture_output=True,
            text=True,
            timeout=300
        )
        payload = {
            "status": "success" if result.returncode == 0 else "failed",
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
        print(payload, flush=True)
        return jsonify(payload), 200 if result.returncode == 0 else 500
    except Exception as e:
        print(f"ERROR: {str(e)}", flush=True)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Flask app started", flush=True)
    app.run(host="0.0.0.0", port=8000)
