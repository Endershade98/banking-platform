# tests/unit/domain/test_ledger_service.py

from unittest.mock import Mock

from core.domain.services.ledger_service import LedgerService
from core.domain.entities.transaction import Transaction
from core.domain.value_objects.money import Money


def test_ledger_service_posts_entries():

    repository = Mock()

    service = LedgerService(
        repository
    )


    transaction = Transaction(
        from_account_id="account1",
        to_account_id="account2",
        amount=Money(100, "USD")
    )


    service.post_transaction_sync(
        transaction
    )


    repository.save_sync.assert_called()