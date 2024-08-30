from fastapi import Depends, status
from fastapi.responses import JSONResponse
from app.core.verify_token_middleware import verify_token
from app.services.account.get_account_by_id_service import get
from app.errors.account_not_found_error import AccountNotFoundError

async def get_account(account_id: str, id_user: str = Depends(verify_token)):
    try:
        account = await get(account_id, id_user)

        return {"account": account}
    except AccountNotFoundError as error:
        return JSONResponse(
            content={"message_error": str(error)},
            status_code=status.HTTP_404_NOT_FOUND
        )