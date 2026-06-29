# src/core/domain/entities/transaction_status.py

from enum import Enum


class TransactionStatus(str, Enum):

    CREATED = "CREATED"
    VALIDATING = "VALIDATING"
    PENDING = "PENDING"
    POSTING = "POSTING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    ROLLED_BACK = "ROLLED_BACK"