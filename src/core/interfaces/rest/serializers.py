# src/core/interfaces/rest/serializers.py

from rest_framework import serializers


class CreateAccountSerializer(serializers.Serializer):
    owner = serializers.CharField(max_length=255)
    initial_balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    currency = serializers.CharField(max_length=3, default="USD")


class AccountResponseSerializer(serializers.Serializer):
    account_id = serializers.UUIDField()
    owner = serializers.CharField()
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    currency = serializers.CharField()
    is_frozen = serializers.BooleanField()


class BalanceResponseSerializer(serializers.Serializer):
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    currency = serializers.CharField()

class TransferMoneySerializer(serializers.Serializer):
    from_account_id = serializers.UUIDField()
    to_account_id = serializers.UUIDField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    currency = serializers.CharField(max_length=3)

class TransactionResponseSerializer(serializers.Serializer):
    transaction_id = serializers.UUIDField()
    from_account_id = serializers.UUIDField()
    to_account_id = serializers.UUIDField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    currency = serializers.CharField(max_length=3)
    status = serializers.CharField()
    created_at = serializers.DateTimeField()

class TransferMoneySerializer(serializers.Serializer):

    from_account_id = serializers.UUIDField()

    to_account_id = serializers.UUIDField()

    amount = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    currency = serializers.CharField(
        max_length=3
    )


    idempotency_key = serializers.CharField(
        max_length=255
    )