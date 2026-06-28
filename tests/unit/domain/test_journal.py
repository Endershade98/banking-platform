# tests/unit/domain/test_journal.py

from decimal import Decimal

import pytest

from core.domain.entities.journal import Journal
from core.domain.entities.ledger_entry import LedgerEntry
from core.domain.exceptions.ledger_exceptions import UnbalancedJournalError


def debit(account: str, amount: str) -> LedgerEntry:
    return LedgerEntry(
        account_id=account,
        amount=Decimal(amount),
        currency="USD",
        entry_type="debit",
        transaction_id="TX1",
    )


def credit(account: str, amount: str) -> LedgerEntry:
    return LedgerEntry(
        account_id=account,
        amount=Decimal(amount),
        currency="USD",
        entry_type="credit",
        transaction_id="TX1",
    )


# -------------------------------------------------------
# Balanced journals
# -------------------------------------------------------


def test_balanced_journal_is_created():
    journal = Journal(
        transaction_id="TX1",
        entries=[
            debit("A", "100"),
            credit("B", "100"),
        ],
    )

    assert journal.transaction_id == "TX1"
    assert len(journal.entries) == 2


def test_balanced_journal_validate_balance():
    journal = Journal(
        transaction_id="TX2",
        entries=[
            debit("Cash", "250"),
            credit("Revenue", "250"),
        ],
    )

    assert journal.validate_balance() is None


def test_multiple_entries_balanced():
    journal = Journal(
        transaction_id="TX3",
        entries=[
            debit("Cash", "100"),
            debit("Fees", "20"),
            credit("Revenue", "120"),
        ],
    )

    assert journal.validate_balance() is None


# -------------------------------------------------------
# Invalid journals
# -------------------------------------------------------


def test_unbalanced_journal_raises_exception():
    with pytest.raises(UnbalancedJournalError):
        Journal(
            transaction_id="TX4",
            entries=[
                debit("A", "100"),
                credit("B", "90"),
            ],
        )


def test_multiple_entries_unbalanced():
    with pytest.raises(UnbalancedJournalError):
        Journal(
            transaction_id="TX5",
            entries=[
                debit("Cash", "100"),
                debit("Fees", "20"),
                credit("Revenue", "100"),
            ],
        )


def test_empty_journal_not_allowed():
    with pytest.raises(ValueError, match="Journal requires entries"):
        Journal(
            transaction_id="EMPTY",
            entries=[],
        )


# -------------------------------------------------------
# LedgerEntry validation
# -------------------------------------------------------


def test_negative_amount_not_allowed():
    with pytest.raises(ValueError):
        LedgerEntry(
            account_id="A",
            amount=Decimal("-10"),
            currency="USD",
            entry_type="debit",
            transaction_id="TX6",
        )


def test_zero_amount_not_allowed():
    with pytest.raises(ValueError):
        LedgerEntry(
            account_id="A",
            amount=Decimal("0"),
            currency="USD",
            entry_type="debit",
            transaction_id="TX7",
        )


def test_invalid_entry_type():
    with pytest.raises(ValueError):
        LedgerEntry(
            account_id="A",
            amount=Decimal("100"),
            currency="USD",
            entry_type="invalid",
            transaction_id="TX8",
        )


# -------------------------------------------------------
# Exception message
# -------------------------------------------------------


def test_exception_message_contains_totals():
    with pytest.raises(UnbalancedJournalError) as exc:
        Journal(
            transaction_id="TX9",
            entries=[
                debit("A", "150"),
                credit("B", "100"),
            ],
        )

    message = str(exc.value)

    assert "Debit=150" in message
    assert "Credit=100" in message