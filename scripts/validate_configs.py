from pathlib import Path
import json

import yaml


ROOT = Path(__file__).resolve().parents[1]


def validate() -> list[str]:
    errors: list[str] = []

    prometheus = yaml.safe_load((ROOT / "prometheus" / "prometheus.yml").read_text(encoding="utf-8"))
    jobs = [item.get("job_name") for item in prometheus.get("scrape_configs", [])]
    if "exporter" not in jobs:
        errors.append("Prometheus is not scraping the exporter job")

    alert_rules = yaml.safe_load((ROOT / "prometheus" / "rules" / "network-alerts.yml").read_text(encoding="utf-8"))
    rule_names = {rule.get("alert") for group in alert_rules.get("groups", []) for rule in group.get("rules", [])}
    for expected in {"ServiceDown", "HighLatency"}:
        if expected not in rule_names:
            errors.append(f"Missing alert rule: {expected}")

    alertmanager = yaml.safe_load((ROOT / "alertmanager" / "alertmanager.yml").read_text(encoding="utf-8"))
    receivers = {receiver.get("name") for receiver in alertmanager.get("receivers", [])}
    if "alert-receiver" not in receivers:
        errors.append("Alertmanager receiver is missing")

    webhook_urls = [webhook.get("url") for receiver in alertmanager.get("receivers", []) for webhook in receiver.get("webhook_configs", [])]
    if "http://alert-receiver:5000/alerts" not in webhook_urls:
        errors.append("Alertmanager is not wired to the alert receiver endpoint")

    dashboard = json.loads((ROOT / "grafana" / "dashboards" / "network-overview.json").read_text(encoding="utf-8"))
    panel_titles = {panel.get("title") for panel in dashboard.get("panels", [])}
    for expected in {"Service Up", "Latency"}:
        if expected not in panel_titles:
            errors.append(f"Dashboard is missing panel: {expected}")

    exporter_metrics = (ROOT / "exporter" / "app.py").read_text(encoding="utf-8")
    for metric_name in ["service_up", "service_latency_ms", "interface_utilization_pct", "packet_loss_pct"]:
        if metric_name not in exporter_metrics:
            errors.append(f"Exporter is missing metric: {metric_name}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(error)
        return 1
    print("Configuration validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
