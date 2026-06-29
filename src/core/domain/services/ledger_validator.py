# src/core/domain/services/ledger_validator.py

from decimal import Decimal


class LedgerValidator:


    @staticmethod
    def validate(
        entries
    ):


        debit=sum(
            e.amount
            for e in entries
            if e.entry_type=="debit"
        )


        credit=sum(
            e.amount
            for e in entries
            if e.entry_type=="credit"
        )


        if debit != credit:
            raise ValueError(
                "Ledger imbalance"
            )


        return True