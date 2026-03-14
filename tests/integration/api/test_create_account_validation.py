import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_account_invalid_balance():

    client = APIClient()

    response = client.post(
        "/api/accounts",
        {
            "owner": "alice",
            "initial_balance": -10,
            "currency": "USD"
        },
        format="json"
    )

    assert response.status_code == 400