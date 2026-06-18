from alert_receiver.app import app as alert_receiver_app
from exporter.app import app as exporter_app


def test_exporter_metrics_include_core_series():
    client = exporter_app.test_client()
    response = client.get("/metrics")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "service_up" in body
    assert "service_latency_ms" in body


def test_alert_receiver_accepts_webhook_payload():
    client = alert_receiver_app.test_client()
    response = client.post("/alerts", json={"alerts": [{"labels": {"alertname": "ServiceDown"}}]})

    assert response.status_code == 200
    assert response.get_json()["received"] == 1
