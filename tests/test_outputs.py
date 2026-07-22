import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load_report():
    assert REPORT.exists(), "no /app/report.json found"
    return json.loads(REPORT.read_text())


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and parses as a single JSON object."""
    data = _load_report()
    assert isinstance(data, dict), "report.json is not a JSON object"


def test_total_requests():
    """Criterion 2: total_requests equals the number of request lines (6)."""
    data = _load_report()
    assert data["total_requests"] == 6


def test_unique_ips():
    """Criterion 3: unique_ips equals the number of distinct client IPs (3)."""
    data = _load_report()
    assert data["unique_ips"] == 3


def test_top_path():
    """Criterion 4: top_path is the most frequently requested path (/index.html)."""
    data = _load_report()
    assert data["top_path"] == "/index.html"
