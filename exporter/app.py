from flask import Flask, Response, jsonify


app = Flask(__name__)

METRICS = """# HELP service_up Service availability for the lab app
# TYPE service_up gauge
service_up{service="edge-api"} 1
# HELP service_latency_ms Service latency in milliseconds
# TYPE service_latency_ms gauge
service_latency_ms{service="edge-api"} 142
# HELP interface_utilization_pct Interface utilization percentage
# TYPE interface_utilization_pct gauge
interface_utilization_pct{device="leaf-01",interface="Ethernet1/1"} 38
# HELP packet_loss_pct Packet loss percentage
# TYPE packet_loss_pct gauge
packet_loss_pct{device="leaf-01",interface="Ethernet1/1"} 0.2
"""


@app.get("/")
def index():
    return jsonify(service="network-observability-platform", endpoints=["/metrics", "/healthz"])


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")


@app.get("/metrics")
def metrics():
    return Response(METRICS, mimetype="text/plain; version=0.0.4; charset=utf-8")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
