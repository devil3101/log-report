import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_json_schema():
    """Success criterion 1: /app/report.json exists with required keys."""
    data = json.loads(REPORT.read_text())
    assert set(data.keys()) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Success criterion 2: total_requests matches non-empty log line count."""
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips matches distinct client IP count."""
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path is the most frequent request path."""
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html"