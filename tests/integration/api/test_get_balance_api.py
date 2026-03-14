import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_get_balance_api():

    client = APIClient()

    create = client.post(
        "/api/accounts",
        {
            "owner": "alice",
            "initial_balance": 200,
            "currency": "USD"
        },
        format="json"
    )

    account_id = create.json()["account_id"]

    response = client.get(f"/api/accounts/{account_id}/balance")

    assert response.status_code == 200

    data = response.json()

    assert data["balance"] == "200.00"
    assert data["currency"] == "USD"