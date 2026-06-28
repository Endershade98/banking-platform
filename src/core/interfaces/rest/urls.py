# src/core/interfaces/rest/urls.py

from django.urls import path

from .views import (
    CreateAccountView,
    GetAccountView,
    GetBalanceView,
    TransferMoneyView,
    LedgerView,
    FreezeAccountView
)

urlpatterns = [
    path("accounts", CreateAccountView.as_view()),
    path("accounts/<uuid:account_id>", GetAccountView.as_view()),
    path("accounts/<uuid:account_id>/balance", GetBalanceView.as_view()),
    path("accounts/<uuid:account_id>/freeze", FreezeAccountView.as_view()),
    path("transactions/transfer", TransferMoneyView.as_view()),
    path("ledger", LedgerView.as_view())   
]