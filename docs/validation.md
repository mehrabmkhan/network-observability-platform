# Validation

Run these checks from the repo root:

```bash
python scripts/validate_configs.py
pytest
```

Then bring the stack up and check the key endpoints:

```bash
docker compose up --build
```

- `http://localhost:8000/metrics`
- `http://localhost:9090/targets`
- `http://localhost:3000`
