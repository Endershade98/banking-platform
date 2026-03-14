import pytest

from core.application.use_cases.create_account import CreateAccountUseCase
from core.infrastructure.db.repositories.account_repository import DjangoAccountRepository


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_create_account_integration():

    repo = DjangoAccountRepository()

    use_case = CreateAccountUseCase(repo)

    account = await use_case.execute(
        owner="bob",
        initial_balance=50
    )

    loaded = await repo.get_by_id(account.account_id)

    assert loaded.owner == "bob"
    assert loaded.balance.amount == 50