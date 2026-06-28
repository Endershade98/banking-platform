# tests/unit/domain/test_ledger_service.py

import pytest
from unittest.mock import AsyncMock

from core.domain.services.ledger_service import LedgerService
from core.domain.entities.transaction import Transaction
from core.domain.value_objects.money import Money



@pytest.mark.asyncio
async def test_ledger_service_posts_entries():


    repository = AsyncMock()


    service = LedgerService(
        repository
    )


    transaction = Transaction(
        from_account_id="A",
        to_account_id="B",
        amount=Money(
            50,
            "USD"
        )
    )


    journal = await service.post_transaction(
        transaction
    )


    assert len(journal.entries) == 2


    assert repository.save.call_count == 2