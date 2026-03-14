import pytest

from core.application.use_cases.freeze_account import FreezeAccountUseCase
from core.application.use_cases.create_account import CreateAccountUseCase
from core.infrastructure.db.repositories.account_repository import DjangoAccountRepository


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_freeze_account_integration():

    repo = DjangoAccountRepository()

    create_use_case = CreateAccountUseCase(repo)

    account = await create_use_case.execute("alice", 100)

    freeze_use_case = FreezeAccountUseCase(repo)

    await freeze_use_case.execute(account.account_id)

    loaded = await repo.get_by_id(account.account_id)

    assert loaded.is_frozen is True