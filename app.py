from flask import Flask, jsonify
import subprocess
import sys
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def run_script():
    try:
        print(f"[{datetime.now()}] Menjalankan ./gas...")
        sys.stdout.flush()
        
        result = subprocess.run(
            ["./gas"],
            capture_output=True,
            text=True,
            timeout=300
        )

        output = {
            "timestamp": datetime.now().isoformat(),
            "status": "success" if result.returncode == 0 else "failed",
            "returncode": result.returncode,
            "stdout": result.stdout if result.stdout else "(no stdout)",
            "stderr": result.stderr if result.stderr else "(no stderr)"
        }
        
        print(f"[{datetime.now()}] Output: {output}")
        sys.stdout.flush()
        
        return jsonify(output), 200 if result.returncode == 0 else 500
    
    except subprocess.TimeoutExpired:
        return jsonify({
            "status": "error",
            "message": "Script timeout (>300 detik)"
        }), 500
    
    except Exception as e:
        print(f"[{datetime.now()}] Error: {str(e)}")
        sys.stdout.flush()
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    print(f"[{datetime.now()}] Flask app started on port 8000")
    sys.stdout.flush()
    app.run(host="0.0.0.0", port=8000, debug=False)
