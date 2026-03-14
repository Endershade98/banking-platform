import pytest

from core.application.use_cases.get_balance import GetBalanceUseCase
from core.application.use_cases.create_account import CreateAccountUseCase
from core.infrastructure.db.repositories.account_repository import DjangoAccountRepository


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_get_balance_integration():

    repo = DjangoAccountRepository()

    create_use_case = CreateAccountUseCase(repo)

    account = await create_use_case.execute("alice", 150)

    get_balance = GetBalanceUseCase(repo)

    balance = await get_balance.execute(account.account_id)

    assert balance.amount == 150