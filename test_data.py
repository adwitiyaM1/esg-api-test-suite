import requests
import pytest

BASE_URL = "http://localhost:8000"

@pytest.fixture
def new_data_payload():
    return {
        "id": 1001,
        "name": "Water Usage",
        "unit": 3.5,
        "category": "Environment",
        "mandatory": True
    }
def test_post_data_positive(new_data_payload):
    res = requests.post(f"{BASE_URL}/data", json=new_data_payload)
    assert res.status_code == 201

def test_post_data_invalid_payload():
    res = requests.post(f"{BASE_URL}/data", json={"bad": "data"})
    assert res.status_code in [400, 422]

def test_put_data_positive(new_data_payload):
    update = new_data_payload.copy()
    update["unit"] = 4.2
    res = requests.put(f"{BASE_URL}/data/1001", json=update)
    assert res.status_code in [200, 204]

def test_put_data_not_found():
    payload = {
        "id": 99999,
        "name": "Missing KPI",
        "unit": 0.0,
        "category": "Test",
        "mandatory": False
    }
    res = requests.put(f"{BASE_URL}/data/99999", json=payload)
    assert res.status_code == 404


def test_delete_data_positive():
    res = requests.delete(f"{BASE_URL}/data/1001")
    assert res.status_code == 200 or res.status_code == 204

def test_delete_data_not_found():
    res = requests.delete(f"{BASE_URL}/data/99999")
    assert res.status_code == 404