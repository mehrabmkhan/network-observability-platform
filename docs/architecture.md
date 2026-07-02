# Architecture

The stack has four moving parts that line up with day-to-day monitoring work.

- The exporter exposes a small set of fixed metrics for a lab service and a lab link.
- Prometheus scrapes the exporter and evaluates alert rules.
- Alertmanager forwards alerts to a local receiver so the flow is visible without external services.
- Grafana is provisioned with Prometheus as a datasource and a dashboard that watches the core metrics.

The point is to make the data path obvious: metrics in, rules in the middle, alerts and dashboards out.

## Design boundaries

This is a local observability lab, not a production monitoring platform. It does not include persistent storage sizing, authentication, TLS, remote write, multi-tenant Grafana controls, or cloud-managed monitoring integrations.
