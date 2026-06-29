# src/core/domain/value_objects/money.py

from decimal import Decimal


class Money:

    def __init__(self, amount, currency: str = "USD"):

        # forcing always Decimal
        self.amount = Decimal(str(amount))
        self.currency = currency

        if self.amount < 0:
            from core.domain.exceptions.account_exceptions import NegativeBalanceError

            if self.amount < 0:
                raise NegativeBalanceError(
                    "Balance cannot be negative"
                )

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return Money(self.amount - other.amount, self.currency)

    def __repr__(self):
        return f"{self.amount} {self.currency}"