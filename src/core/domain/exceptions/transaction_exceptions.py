# src/core/domain/exceptions/transaction_exceptions.py

class TransactionException(Exception):
    pass


class SelfTransferError(TransactionException):
    pass


class NegativeAmountError(TransactionException):
    pass


class CurrencyMismatchError(TransactionException):
    pass