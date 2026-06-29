# src/apps/accounts/models.py

from django.db import models
import uuid

class AccountModel(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    owner=models.CharField(
        max_length=255
    )


    balance=models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )


    currency=models.CharField(
        max_length=3,
        default="USD"
    )


    is_frozen=models.BooleanField(
        default=False
    )


    status=models.CharField(
        max_length=20,
        default="active"
    )


    created_at=models.DateTimeField(
        auto_now_add=True
    )


    updated_at=models.DateTimeField(
        auto_now=True
    )


    class Meta:
        db_table="accounts"