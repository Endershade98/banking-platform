from asgiref.sync import async_to_sync
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.application.use_cases.get_balance import GetBalanceUseCase
from core.infrastructure.db.repositories.account_repository import DjangoAccountRepository
from core.application.use_cases.create_account import CreateAccountUseCase

from .serializers import (
    BalanceResponseSerializer,
    CreateAccountSerializer,
    AccountResponseSerializer
)
from drf_spectacular.utils import extend_schema


class CreateAccountView(APIView):
    
    @extend_schema(
        summary="Create a new account",
        description="Creates a new bank account with an initial balance",
        request=CreateAccountSerializer,
        responses=AccountResponseSerializer,
    )
    def post(self, request):
        serializer = CreateAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        repo = DjangoAccountRepository()
        use_case = CreateAccountUseCase(repo)

        try:
            account = async_to_sync(use_case.execute)(
                owner=serializer.validated_data["owner"],
                initial_balance=serializer.validated_data["initial_balance"],
                currency=serializer.validated_data["currency"],
            )
        except ValueError as e:
            # qui trasformiamo l'errore di business in un 400
            raise ValidationError({"initial_balance": str(e)})

        response = AccountResponseSerializer({
            "account_id": account.account_id,
            "owner": account.owner,
            "balance": account.balance.amount,
            "currency": account.balance.currency,
            "is_frozen": account.is_frozen,
        })

        return Response(response.data, status=status.HTTP_201_CREATED)


class GetAccountView(APIView):

    @extend_schema(
        summary="Get account details",
        description="Retrieves the details of a specific bank account",
        responses=AccountResponseSerializer,
    )
    def get(self, request, account_id):

        repo = DjangoAccountRepository()

        account = async_to_sync(repo.get_by_id)(account_id)

        serializer = AccountResponseSerializer({
            "account_id": account.account_id,
            "owner": account.owner,
            "balance": account.balance.amount,
            "currency": account.balance.currency,
            "is_frozen": account.is_frozen,
        })

        return Response(serializer.data)


class GetBalanceView(APIView):

    @extend_schema(
        summary="Get account balance",
        description="Retrieves the balance of a specific bank account",
        responses=BalanceResponseSerializer,
    )
    def get(self, request, account_id):

        repo = DjangoAccountRepository()
        use_case = GetBalanceUseCase(repo)

        balance = async_to_sync(use_case.execute)(account_id)

        serializer = BalanceResponseSerializer({
            "balance": balance.amount,
            "currency": balance.currency
        })

        return Response(serializer.data)