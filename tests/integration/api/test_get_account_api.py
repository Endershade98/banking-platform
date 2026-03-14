import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_get_account_api():

    client = APIClient()

    create = client.post(
        "/api/accounts",
        {
            "owner": "alice",
            "initial_balance": 100,
            "currency": "USD"
        },
        format="json"
    )

    account_id = create.json()["account_id"]

    response = client.get(f"/api/accounts/{account_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["owner"] == "alice"
    assert data["balance"] == "100.00"
