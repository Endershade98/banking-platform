import pytest
from unittest.mock import AsyncMock
from core.application.use_cases.transfer_money import TransferMoneyUseCase
from core.domain.entities.account import Account
from core.domain.value_objects.money import Money


def create_account(account_id, balance):
    return Account(
        account_id=account_id,
        owner="test",
        balance=Money(balance, "USD"),
    )


@pytest.mark.asyncio
async def test_transfer_money_use_case():

    account_repo = AsyncMock()
    transaction_repo = AsyncMock()

    acc1 = create_account("A", 100)
    acc2 = create_account("B", 50)

    account_repo.get_by_id.side_effect = [acc1, acc2]

    use_case = TransferMoneyUseCase(account_repo, transaction_repo)

    transaction = await use_case.execute(
        "A",
        "B",
        Money(30, "USD")
    )

    assert transaction.status == "COMPLETED"

    account_repo.update.assert_any_call(acc1)
    account_repo.update.assert_any_call(acc2)
    transaction_repo.save.assert_called_once()