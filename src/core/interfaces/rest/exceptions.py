# src/core/interfaces/rest/exceptions.py

from rest_framework.views import exception_handler


def api_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:

        return response


    from core.domain.exceptions.account_exceptions import (
        FrozenAccountError,
        ClosedAccountError,
        InsufficientBalanceError,
        NegativeBalanceError
    )

    from core.domain.exceptions.transaction_exceptions import (
        SelfTransferError,
        NegativeAmountError,
        CurrencyMismatchError,
    )


    error_map = {

        FrozenAccountError: (
            "ACCOUNT_FROZEN",
            400
        ),

        ClosedAccountError: (
            "ACCOUNT_CLOSED",
            400
        ),

        InsufficientBalanceError: (
            "INSUFFICIENT_BALANCE",
            400
        ),

        SelfTransferError: (
            "INVALID_TRANSFER",
            400
        ),

        NegativeAmountError: (
            "INVALID_AMOUNT",
            400
        ),

        CurrencyMismatchError: (
            "CURRENCY_MISMATCH",
            400
        ),

        NegativeBalanceError: (
            "INVALID_BALANCE",
            400
        ),
    }


    for exception, (code, status) in error_map.items():

        if isinstance(exc, exception):

            return response_error(
                code,
                str(exc),
                status
            )


    return response_error(
        "INTERNAL_ERROR",
        "Unexpected server error",
        500
    )



def response_error(
    code,
    message,
    status
):

    from rest_framework.response import Response


    return Response(
        {
            "error": code,
            "message": message,
            "status": status
        },
        status=status
    )