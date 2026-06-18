from flask import Flask, jsonify, request


app = Flask(__name__)


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")


@app.post("/alerts")
def alerts():
    payload = request.get_json(silent=True) or {}
    return jsonify(received=len(payload.get("alerts", [])))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
