# src/apps/ledger/models.py

import uuid

from django.db import models


class LedgerEntryModel(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    account_id = models.UUIDField()

    transaction_id = models.UUIDField()

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    currency = models.CharField(
        max_length=3
    )

    entry_type = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        db_table = "ledger_entries"

        ordering = [
            "-created_at"
        ]