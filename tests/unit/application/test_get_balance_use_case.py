import pytest
from unittest.mock import AsyncMock

from core.application.use_cases.get_balance import GetBalanceUseCase
from core.domain.entities.account import Account
from core.domain.value_objects.money import Money


@pytest.mark.asyncio
async def test_get_balance_use_case():

    repo = AsyncMock()

    account = Account(owner="alice")
    account.deposit(Money(200))

    repo.get_by_id.return_value = account

    use_case = GetBalanceUseCase(repo)

    balance = await use_case.execute(account.account_id)

    assert balance.amount == 200