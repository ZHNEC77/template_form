import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_form_with_matching_template():
    response = client.post("/get_form", data={"order_date": "2023-10-01",
                           "customer_email": "test@example.com", "customer_phone": "+7 123 456 78 90"})
    assert response.status_code == 200
    assert response.json() == "Order Form"


def test_get_form_without_matching_template():
    response = client.post("/get_form", data={"unknown_field": "some_value"})
    assert response.status_code == 200
    assert response.json() == {"unknown_field": "text"}
