# tests/fakes/fake_account_repository.py

class FakeAccountRepository:

    def __init__(self):
        self.accounts = {}

    def save_sync(self, account):
        self.accounts[account.account_id] = account

    def get_for_update_sync(self, account_id):
        return self.accounts.get(account_id)

    def update_sync(self, account):
        self.accounts[account.account_id] = account

    async def get_by_id(self, account_id):
        return self.accounts.get(account_id)