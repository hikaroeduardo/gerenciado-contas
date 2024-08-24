from fastapi import status, Depends
from fastapi.responses import JSONResponse
from app.errors.global_error import GlobalError
from app.core.verify_token_middleware import verify_token
from app.models.schemas.account_schemas import NewAccount
from app.services.account.create_account_service import create

async def create_accounte(data: NewAccount, id_user: str = Depends(verify_token)):
    try:
        await create(data=data, id_user=id_user)

        return JSONResponse(
            content={"message": "Conta cadastrada com sucesso."},
            status_code=status.HTTP_201_CREATED
        )
    except GlobalError as error:
        return JSONResponse(
            content={"message_error": str(error)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    except Exception as error:
        return JSONResponse(
            content={"message_error": "Não foi possível criar uma nova conta, tente novamente."},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
