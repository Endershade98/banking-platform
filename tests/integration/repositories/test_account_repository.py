import pytest
from core.infrastructure.db.repositories.account_repository import DjangoAccountRepository
from core.domain.entities.account import Account
from core.domain.value_objects.money import Money


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_account_repository_save_and_get():

    repo = DjangoAccountRepository()

    account = Account(owner="alice")
    account.deposit(Money(100))

    await repo.save(account)

    loaded = await repo.get_by_id(account.account_id)

    assert loaded.balance.amount == 100