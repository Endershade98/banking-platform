# src/core/application/unit_of_work.py

from django.db import transaction


class DjangoUnitOfWork:


    async def __aenter__(self):

        self.atomic = transaction.atomic()
        self.atomic.__enter__()

        return self



    async def __aexit__(
        self,
        exc_type,
        exc,
        tb
    ):

        self.atomic.__exit__(
            exc_type,
            exc,
            tb
        )