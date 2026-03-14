# core/domain/services/account_services.py

from core.domain.entities.account import Account
from core.domain.value_objects.money import Money

class AccountService:
    @staticmethod
    def transfer(source: Account, destination: Account, amount: Money):
        source.withdraw(amount)
        destination.deposit(amount)