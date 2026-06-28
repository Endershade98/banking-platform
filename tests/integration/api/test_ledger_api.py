# tests/integration/api/test_ledger_api.py

import pytest

from rest_framework.test import APIClient



@pytest.mark.django_db
def test_get_ledger_api():


    client = APIClient()


    response = client.get(
        "/api/ledger"
    )


    assert response.status_code == 200

    assert isinstance(
        response.data,
        list
    )