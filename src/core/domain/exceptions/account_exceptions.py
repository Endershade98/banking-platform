# src/core/domain/exceptions/account_exceptions.py

class AccountException(Exception):
    pass


class FrozenAccountError(AccountException):
    pass


class ClosedAccountError(AccountException):
    pass


class InsufficientBalanceError(AccountException):
    pass

class NegativeBalanceError(AccountException):
    pass