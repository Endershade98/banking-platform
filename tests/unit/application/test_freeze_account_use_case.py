# tests/unit/application/test_freeze_account_use_case.py

import pytest
from unittest.mock import AsyncMock

from core.application.use_cases.freeze_account import FreezeAccountUseCase
from core.domain.entities.account import Account


@pytest.mark.asyncio
async def test_freeze_account_use_case():

    repo = AsyncMock()

    account = Account(
        owner="alice"
    )

    repo.get_by_id.return_value = account


    use_case = FreezeAccountUseCase(repo)


    await use_case.execute(
        account.account_id
    )


    assert account.is_frozen is True

    repo.get_by_id.assert_awaited_once_with(
        account.account_id
    )