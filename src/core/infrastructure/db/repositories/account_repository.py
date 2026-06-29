# src/core/infrastructure/db/repositories/account_repository.py

from asgiref.sync import sync_to_async

from apps.accounts.models import AccountModel

from core.domain.entities.account import Account
from core.domain.value_objects.money import Money
from core.domain.repositories.account_repository import AccountRepository


class DjangoAccountRepository(AccountRepository):


    async def get_by_id(self, account_id):

        from django.core.exceptions import ObjectDoesNotExist

        try:

            model = await AccountModel.objects.aget(
                id=account_id
            )

        except ObjectDoesNotExist:

            return None

        return self._to_entity(model)



    async def save(self, account):

        await sync_to_async(
            self.save_sync,
            thread_sensitive=True
        )(account)



    def save_sync(self, account):

        AccountModel.objects.update_or_create(

            id=account.account_id,

            defaults={

                "owner": account.owner,

                "balance":
                    account.balance.amount,

                "currency":
                    account.balance.currency,

                "is_frozen":
                    account.is_frozen,

                "status":
                    account.status
            }
        )



    async def update(self, account):

        await sync_to_async(
            self.update_sync,
            thread_sensitive=True
        )(account)



    def update_sync(self, account):

        AccountModel.objects.filter(
            id=account.account_id
        ).update(

            balance=account.balance.amount,

            currency=account.balance.currency,

            is_frozen=account.is_frozen,

            status=account.status
        )



    def get_for_update_sync(
        self,
        account_id
    ):

        model = (
            AccountModel.objects
            .select_for_update()
            .get(id=account_id)
        )

        return self._to_entity(model)



    async def delete(self, account_id):

        await AccountModel.objects.filter(
            id=account_id
        ).adelete()



    async def freeze(self, account_id):

        await AccountModel.objects.filter(
            id=account_id
        ).aupdate(
            is_frozen=True
        )



    async def list_all(self):

        result=[]

        queryset = AccountModel.objects.all()

        async for model in queryset:

            result.append(
                self._to_entity(model)
            )

        return result



    def _to_entity(self, model):

        return Account(

            account_id=str(model.id),

            owner=model.owner,

            balance=Money(
                model.balance,
                model.currency
            ),

            is_frozen=model.is_frozen,

            status=model.status
        )