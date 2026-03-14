import pytest
from unittest.mock import AsyncMock

from core.application.use_cases.create_account import CreateAccountUseCase
from core.domain.value_objects.money import Money


@pytest.mark.asyncio
async def test_create_account_use_case():

    repo = AsyncMock()

    use_case = CreateAccountUseCase(account_repo=repo)

    account = await use_case.execute(
        owner="alice",
        initial_balance=100,
        currency="USD"
    )

    repo.save.assert_awaited_once()

    assert account.owner == "alice"
    assert account.balance.amount == 100
    assert account.balance.currency == "USD"