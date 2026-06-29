# src/core/domain/rules/accounting_rules.py

from core.domain.exceptions.account_exceptions import (
    FrozenAccountError,
    ClosedAccountError,
    InsufficientBalanceError
)

from core.domain.exceptions.transaction_exceptions import (
    SelfTransferError,
    CurrencyMismatchError,
    NegativeAmountError
)


class AccountingRules:


    @staticmethod
    def validate_transfer(
        source,
        destination,
        amount
    ):


        if source.account_id == destination.account_id:
            raise SelfTransferError(
                "Cannot transfer to same account"
            )


        if amount.amount <= 0:
            raise NegativeAmountError(
                "Amount must be positive"
            )


        if source.is_frozen:
            raise FrozenAccountError(
                "Source frozen"
            )


        if destination.is_frozen:
            raise FrozenAccountError(
                "Destination frozen"
            )


        if source.status == "closed":
            raise ClosedAccountError(
                "Source closed"
            )


        if destination.status == "closed":
            raise ClosedAccountError(
                "Destination closed"
            )


        if (
            source.balance.currency
            !=
            amount.currency
        ):
            raise CurrencyMismatchError(
                "Currency mismatch"
            )


        if (
            source.balance.amount
            <
            amount.amount
        ):
            raise InsufficientBalanceError(
                "Insufficient balance"
            )