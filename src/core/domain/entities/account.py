# core/domain/entities/account.py

from uuid import uuid4
from core.domain.value_objects.money import Money

class Account:
    def __init__(self, account_id: str = None, balance: Money = None, owner: str = "", is_frozen: bool = False):
        self.account_id = account_id or str(uuid4())
        self.owner = owner
        self.balance = balance or Money(0, "USD")
        self.is_frozen = is_frozen

    def deposit(self, amount: Money):
        if amount.amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: Money):
        if amount.amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance.amount < amount.amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def freeze(self):
        self.is_frozen = True