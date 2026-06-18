# Network observability platform

Docker-based monitoring stack for a small network/service lab.

It includes:

- a sample exporter that exposes network and service metrics
- Prometheus scraping and alert rules
- Alertmanager routing to a local receiver container
- Grafana provisioning with a small dashboard

The stack is intentionally compact so it can be brought up, checked, and modified without carrying a full platform around.

## Layout

- `exporter/` contains the sample metrics app
- `alert-receiver/` contains the alert logging app
- `prometheus/` contains scrape config and rules
- `grafana/` contains provisioning and dashboard files
- `alertmanager/` contains the alert routing config
- `tests/` validates the configs and apps
- `screenshots/` is a placeholder only

## Local setup

```bash
python -m pip install -r requirements-dev.txt
```

## Run the stack

```bash
docker compose up --build
```

Useful endpoints:

- exporter metrics: `http://localhost:8000/metrics`
- alert receiver: `http://localhost:5000/healthz`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`

## Validation

```bash
python scripts/validate_configs.py
pytest
```

## Cleanup

```bash
docker compose down -v
```
