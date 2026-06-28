# src/core/infrastructure/db/repositories/ledger_repository.py

from apps.ledger.models import LedgerEntryModel

from core.domain.entities.ledger_entry import LedgerEntry



class DjangoLedgerRepository:


    async def save(
        self,
        entry: LedgerEntry
    ):

        await LedgerEntryModel.objects.acreate(

            account_id=entry.account_id,

            transaction_id=entry.transaction_id,

            amount=entry.amount,

            currency=entry.currency,

            entry_type=entry.entry_type
        )



    async def find_by_account(
        self,
        account_id
    ):

        result = []

        queryset = LedgerEntryModel.objects.filter(
            account_id=account_id
        )


        async for row in queryset:

            result.append(
                LedgerEntry(

                    account_id=row.account_id,

                    transaction_id=row.transaction_id,

                    amount=row.amount,

                    currency=row.currency,

                    entry_type=row.entry_type
                )
            )

        return result



    async def find_by_transaction(
        self,
        transaction_id
    ):

        result = []


        queryset = LedgerEntryModel.objects.filter(
            transaction_id=transaction_id
        )


        async for row in queryset:

            result.append(
                LedgerEntry(

                    account_id=row.account_id,

                    transaction_id=row.transaction_id,

                    amount=row.amount,

                    currency=row.currency,

                    entry_type=row.entry_type
                )
            )


        return result



    async def find_all(
        self
    ):

        result = []


        queryset = LedgerEntryModel.objects.all()


        async for row in queryset:

            result.append(
                LedgerEntry(

                    account_id=row.account_id,

                    transaction_id=row.transaction_id,

                    amount=row.amount,

                    currency=row.currency,

                    entry_type=row.entry_type
                )
            )


        return result