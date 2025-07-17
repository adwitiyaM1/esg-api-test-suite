import requests
import pytest
from jsonschema import validate

BASE_URL = "http://localhost:8000"  

kpi_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "unit": {"type": "number"},
        "category": {"type": "string"},
        "mandatory": {"type": "boolean"}
    },
    "required": ["id", "name", "unit", "category", "mandatory"]
}

def test_get_all_kpis():
    res = requests.get(f"{BASE_URL}/kpis")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    for kpi in res.json():
        validate(instance=kpi, schema=kpi_schema)

def test_get_kpi_by_id_positive():
    res = requests.get(f"{BASE_URL}/kpis/1")
    assert res.status_code == 200
    validate(instance=res.json(), schema=kpi_schema)

def test_get_kpi_by_id_not_found():
    res = requests.get(f"{BASE_URL}/kpis/99999")
    assert res.status_code == 404
