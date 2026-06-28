# tests/integration/api/test_transfer_money_api.py

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_transfer_money_api():

    client = APIClient()

    # crea account A e B (puoi usare factory o API)
    response = client.post(
        "/api/accounts",
        {
            "owner": "alice",
            "initial_balance": 100,
            "currency": "USD"
        },
        format="json"
    )
    acc1 = response.data["account_id"]

    response = client.post(
        "/api/accounts",
        {
            "owner": "bob",
            "initial_balance": 50,
            "currency": "USD"
        },
        format="json"
    )
    acc2 = response.data["account_id"]

    # transfer
    response = client.post(
        "/api/transactions/transfer",
        {
            "from_account_id": acc1,
            "to_account_id": acc2,
            "amount": 30,
            "currency": "USD"
        },
        format="json"
    )

    assert response.status_code == 201
    assert response.data["status"] == "COMPLETED"