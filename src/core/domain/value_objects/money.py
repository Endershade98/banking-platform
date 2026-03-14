# core/domain/value_objects/money.py

class Money:
    def __init__(self, amount: float, currency: str = "USD"):
        if amount < 0:
            raise ValueError("Money amount cannot be negative")
        self.amount = amount
        self.currency = currency

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