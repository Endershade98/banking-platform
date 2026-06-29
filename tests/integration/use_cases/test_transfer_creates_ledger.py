# tests/integration/use_cases/test_transfer_creates_ledger.py

import uuid
import pytest

from core.application.use_cases.transfer_money import (
    TransferMoneyUseCase
)

from core.domain.entities.account import Account
from core.domain.value_objects.money import Money

from core.infrastructure.db.repositories.transaction_repository import (
    DjangoTransactionRepository
)

from core.infrastructure.db.repositories.ledger_repository import (
    DjangoLedgerRepository
)

from tests.fakes.fake_account_repository import (
    FakeAccountRepository
)


@pytest.mark.django_db
def test_transfer_generates_ledger_entries():

    sender_id = uuid.uuid4()
    receiver_id = uuid.uuid4()

    account_repo = FakeAccountRepository()

    sender = Account(
        account_id=sender_id,
        balance=Money(1000, "USD"),
    )

    receiver = Account(
        account_id=receiver_id,
        balance=Money(500, "USD"),
    )

    account_repo.save_sync(sender)
    account_repo.save_sync(receiver)


    transaction_repo = DjangoTransactionRepository()
    ledger_repo = DjangoLedgerRepository()


    use_case = TransferMoneyUseCase(
        account_repo,
        transaction_repo,
        ledger_repo,
    )


    transaction = use_case._execute_transaction(
        sender_id,
        receiver_id,
        Money(30, "USD"),
        "key-001",
    )


    assert transaction is not None
    assert transaction.status == "COMPLETED"


    entries = ledger_repo.find_by_account_id_sync(
        sender_id
    )


    assert len(entries) == 1


    debit = entries[0]


    assert str(debit.transaction_id) == str(
        transaction.transaction_id
    )

    assert debit.account_id == sender_id
    assert debit.amount == 30
    assert debit.currency == "USD"
    assert debit.entry_type == "debit"