# src/apps/transactions/models.py

import uuid

from django.db import models


class TransactionModel(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    idempotency_key = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        db_index=True
    )


    from_account_id=models.UUIDField()

    to_account_id=models.UUIDField()


    amount=models.DecimalField(
        max_digits=12,
        decimal_places=2
    )


    currency=models.CharField(
        max_length=3
    )


    status=models.CharField(
        max_length=20
    )


    created_at=models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        db_table="transactions"