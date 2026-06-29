# tests/integration/api/test_freeze_account_api.py

import pytest

from rest_framework.test import APIClient

from apps.accounts.models import AccountModel



@pytest.mark.django_db
def test_freeze_account_api():

    client = APIClient()


    create_response = client.post(
        "/api/accounts",
        {
            "owner": "alice",
            "initial_balance": 100,
            "currency": "USD"
        },
        format="json"
    )


    assert create_response.status_code == 201


    account_id = create_response.data["account_id"]


    response = client.patch(
        f"/api/accounts/{account_id}/freeze"
    )


    assert response.status_code == 200


    account = AccountModel.objects.get(
        id=account_id
    )


    assert account.is_frozen is True