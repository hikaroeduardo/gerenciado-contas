from fastapi import Depends, status
from fastapi.responses import JSONResponse
from app.errors.paid_account_error import PaidAccountError
from app.errors.account_not_found_error import AccountNotFoundError
from app.services.account.pay_account_service import pay
from app.core.verify_token_middleware import verify_token

async def pay_account(account_id: str, id_user: str = Depends(verify_token)):
    try:
        await pay(account_id, id_user)

        return JSONResponse(
            content={"message": "Conta paga com sucesso."},
            status_code=status.HTTP_200_OK
        )
    
    except PaidAccountError as error:
        return JSONResponse(
            content={"message_error": str(error)},
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    except AccountNotFoundError as error:
        return JSONResponse(
            content={"message_error": str(error)},
            status_code=status.HTTP_404_NOT_FOUND
        )