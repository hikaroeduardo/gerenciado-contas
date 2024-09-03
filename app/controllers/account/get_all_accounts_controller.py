from fastapi import Depends, status
from fastapi.responses import JSONResponse
from app.core.verify_token_middleware import verify_token
from app.services.account.get_all_accounts_service import get
from app.models.schemas.account_schemas import ResponseDataAccounts

async def get_accounts(id_user: str = Depends(verify_token)) -> ResponseDataAccounts:
    try:
        accounts = await get(id_user)

        if len(accounts) == 0:
            return JSONResponse(
                content={
                    "message": "Este usuário não possui nenhuma conta cadastrada."
                },
                status_code=status.HTTP_200_OK
            )

        return {"data": accounts}
    
    except Exception:
        return JSONResponse(
            content={"message_error": "Não foi possível buscar contas deste usuário, tente novamente."},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
