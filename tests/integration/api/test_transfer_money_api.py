# tests/integration/api/test_transfer_money_api.py

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_transfer_money_api():

    client = APIClient()


    r1 = client.post(
        "/api/accounts",
        {
            "owner": "alice",
            "initial_balance": 100,
            "currency": "USD",
        },
        format="json",
    )

    assert r1.status_code == 201

    acc1 = r1.data["account_id"]



    r2 = client.post(
        "/api/accounts",
        {
            "owner": "bob",
            "initial_balance": 50,
            "currency": "USD",
        },
        format="json",
    )


    assert r2.status_code == 201

    acc2 = r2.data["account_id"]



    response = client.post(
        "/api/transactions/transfer",
        {
            "from_account_id": acc1,
            "to_account_id": acc2,
            "amount": 30,
            "currency": "USD",
            "idempotency_key": "transfer-001",
        },
        format="json",
    )


    assert response.status_code == 201

    assert response.data["status"] == "COMPLETED"