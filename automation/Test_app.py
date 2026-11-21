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


def test_get_missing_equipment(client):
    response = client.get("/equipment/999")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Equipment not found"}