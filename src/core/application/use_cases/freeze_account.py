# src/core/application/use_cases/freeze_account.py

class FreezeAccountUseCase:

    def __init__(self, repository):
        self.repository = repository


    async def execute(self, account_id):

        account = await self.repository.find_by_id(
            account_id
        )

        if account is None:
            return None


        account.freeze()


        await self.repository.save(
            account
        )

        return account