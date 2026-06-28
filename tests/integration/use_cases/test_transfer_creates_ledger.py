# tests/integration/use_cases/test_transfer_creates_ledger.py

import pytest
import uuid

from core.application.use_cases.transfer_money import (
    TransferMoneyUseCase
)

from core.domain.entities.account import Account
from core.domain.value_objects.money import Money

from core.infrastructure.db.repositories.ledger_repository import (
    DjangoLedgerRepository
)

from core.infrastructure.db.repositories.transaction_repository import (
    DjangoTransactionRepository
)


class FakeAccountRepository:

    def __init__(self):

        self.accounts = {
            "A": Account(
                account_id=str(uuid.uuid4()),
                owner="alice",
                balance=Money(
                    100,
                    "USD"
                )
            ),

            "B": Account(
                account_id=str(uuid.uuid4()),
                owner="bob",
                balance=Money(
                    50,
                    "USD"
                )
            )
        }


    async def get_by_id(self, account_id):

        return self.accounts[account_id]


    async def update(self, account):

        self.accounts[
            account.account_id
        ] = account



@pytest.mark.django_db
@pytest.mark.asyncio
async def test_transfer_generates_ledger_entries():


    account_repo = FakeAccountRepository()


    transaction_repo = DjangoTransactionRepository()


    ledger_repo = DjangoLedgerRepository()


    use_case = TransferMoneyUseCase(
        account_repo,
        transaction_repo,
        ledger_repo
    )


    transaction = await use_case.execute(
        "A",
        "B",
        Money(
            30,
            "USD"
        )
    )


    entries = await ledger_repo.find_by_transaction(
        transaction.transaction_id
    )


    assert len(entries) == 2


    types = {
        entry.entry_type
        for entry in entries
    }


    assert types == {
        "debit",
        "credit"
    }


    for entry in entries:

        assert uuid.UUID(
            str(entry.account_id)
        )

        assert uuid.UUID(
            str(entry.transaction_id)
        ) == uuid.UUID(
            str(transaction.transaction_id)
        )