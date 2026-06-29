# src/core/domain/entities/account.py

from uuid import uuid4
from core.domain.value_objects.money import Money


class Account:

    def __init__(
        self,
        account_id=None,
        balance=None,
        owner="",
        is_frozen=False,
        status="active"
    ):
        self.account_id = account_id or str(uuid4())
        self.owner = owner
        self.balance = balance or Money(0, "USD")
        self.is_frozen = is_frozen
        self.status = status


    def deposit(self, amount: Money):

        if self.status != "active":
            raise ValueError(
                "Inactive account"
            )

        self.balance += amount


    def withdraw(self, amount: Money):

        if self.status != "active":
            raise ValueError(
                "Inactive account"
            )

        if amount.amount <= 0:
            raise ValueError(
                "Amount must be positive"
            )

        if self.balance.amount < amount.amount:
            raise ValueError(
                "Insufficient funds"
            )

        self.balance -= amount


    def freeze(self):

        self.is_frozen = True


    def close(self):

        if self.status != "active":
            raise ValueError(
                "Account already closed"
            )


        if self.is_frozen:
            raise ValueError(
                "Frozen account cannot close"
            )


        self.status="closed"