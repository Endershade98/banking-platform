# src/core/application/use_cases/close_account.py

class CloseAccountUseCase:


    def __init__(self, repository):

        self.repository = repository



    async def execute(
        self,
        account_id
    ):

        account = await self.repository.get_by_id(
            account_id
        )


        if account is None:
            return None


        account.close()


        await self.repository.update(
            account
        )


        return account