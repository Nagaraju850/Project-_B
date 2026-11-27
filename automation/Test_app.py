from concurrent.futures import ThreadPoolExecutor
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent / "simulator"))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_get_equipment(client):
    response = client.get("/equipment")

    assert response.status_code == 200
    assert response.get_json()[0]["name"] == "Equipment A"


def test_get_equipment_by_id(client):
    equipment_id = 101
    response = client.get(f"/equipment/{equipment_id}")

    assert response.status_code == 200
    assert response.get_json()["id"] == equipment_id


def test_get_equipment_in_multiple_threads():
    def get_equipment(equipment_id):
        with app.test_client() as test_client:
            response = test_client.get(f"/equipment/{equipment_id}")
            return response.status_code, response.get_json()

    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(get_equipment, [101, 102]))

    assert results == [
        (200, {"id": 101, "name": "Equipment A", "type": "FCU", "status": "active"}),
        (200, {"id": 102, "name": "Equipment B", "type": "AHU", "status": "inactive"}),
    ]


def test_home_page_displays_selected_equipment(client):
    response = client.get("/?id=102")

    assert response.status_code == 200
    assert b"Equipment B" in response.data
    assert b"AHU" in response.data


def test_get_missing_equipment(client):
    response = client.get("/equipment/999")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Equipment not found"}