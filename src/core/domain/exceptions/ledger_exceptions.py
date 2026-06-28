# src/core/domain/exceptions/ledger_exceptions.py

class UnbalancedJournalError(Exception):
    """
    Sollevata quando un Journal
    non rispetta la regola:

    Total Debit == Total Credit
    """

    pass