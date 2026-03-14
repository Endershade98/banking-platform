import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_account_api():

    client = APIClient()

    response = client.post(
        "/api/accounts",
        {
            "owner": "alice",
            "initial_balance": 100,
            "currency": "USD"
        },
        format="json"
    )

    assert response.status_code == 201

    data = response.json()

    assert data["owner"] == "alice"
    assert data["balance"] == "100.00"
    assert data["currency"] == "USD"
    assert data["is_frozen"] is False