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
            ),
            is_frozen=model.is_frozen
        )

    async def save(self, account: Account) -> None:

        await AccountModel.objects.aupdate_or_create(
            id=account.account_id,
            defaults={
                "owner": account.owner,
                "balance": account.balance.amount,
                "currency": account.balance.currency,
                "is_frozen": account.is_frozen,
            },
        )

    async def update(self, account: Account) -> None:

        await AccountModel.objects.filter(id=account.account_id).aupdate(
            owner=account.owner,
            balance=account.balance.amount,
            currency=account.balance.currency,
            is_frozen=account.is_frozen
        )

    async def delete(self, account_id: str) -> None:

        await AccountModel.objects.filter(id=account_id).adelete()

    async def freeze(self, account_id: str) -> None:

        await AccountModel.objects.filter(id=account_id).aupdate(
            is_frozen=True
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
                    ),
                    is_frozen=model.is_frozen
                )
            )

        return accounts