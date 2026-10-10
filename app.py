from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def run_script():
    try:
        result = subprocess.run(
            ["./gas"],
            capture_output=True,
            text=True,
            timeout=300
        )

        return jsonify({
            "status": "success" if result.returncode == 0 else "failed",
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }), 200 if result.returncode == 0 else 500
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
