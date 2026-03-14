from django.urls import path

from .views import (
    CreateAccountView,
    GetAccountView,
    GetBalanceView
)

urlpatterns = [
    path("accounts", CreateAccountView.as_view()),
    path("accounts/<uuid:account_id>", GetAccountView.as_view()),
    path("accounts/<uuid:account_id>/balance", GetBalanceView.as_view()),
]