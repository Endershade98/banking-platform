from apps.accounts.models import AccountModel
from core.domain.entities.account import Account
from core.domain.value_objects.money import Money
from core.domain.repositories.account_repository import AccountRepository


class DjangoAccountRepository(AccountRepository):

    async def get_by_id(self, account_id: str) -> Account:

        model = await AccountModel.objects.aget(id=account_id)

        return Account(
            account_id=str(model.id),
            owner=model.owner,
            balance=Money(
                amount=float(model.balance),
                currency=model.currency
            )
        )

    async def save(self, account: Account) -> None:

        await AccountModel.objects.aupdate_or_create(
            id=account.account_id,
            defaults={
                "owner": account.owner,
                "balance": account.balance.amount,
                "currency": account.balance.currency
            }
        )

    async def list_all(self):

        models = AccountModel.objects.all()

        accounts = []

        async for model in models:
            accounts.append(
                Account(
                    account_id=str(model.id),
                    owner=model.owner,
                    balance=Money(
                        amount=float(model.balance),
                        currency=model.currency
                    )
                )
            )

        return accounts