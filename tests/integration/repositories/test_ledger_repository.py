# tests/integration/repositories/test_ledger_repository.py

import uuid
import pytest

from core.infrastructure.db.repositories.ledger_repository import (
    DjangoLedgerRepository,
)

from core.domain.entities.ledger_entry import LedgerEntry


@pytest.mark.django_db
def test_save_and_find_ledger_entry():

    repo = DjangoLedgerRepository()

    account_id = uuid.uuid4()
    transaction_id = uuid.uuid4()

    entry = LedgerEntry(
        account_id=account_id,
        amount=100,
        currency="USD",
        entry_type="debit",
        transaction_id=transaction_id,
    )

    repo.save_sync(entry)

    result = repo.find_by_account_id_sync(account_id)

    assert len(result) == 1

    saved = result[0]

    assert saved.account_id == account_id
    assert saved.transaction_id == transaction_id
    assert saved.amount == 100
    assert saved.currency == "USD"
    assert saved.entry_type == "debit"