from fastapi import status
from fastapi.responses import JSONResponse
from app.models.schemas.user_schemas import NewUser
from app.services.users.create_user_service import create
from app.errors.user_already_exists_error import UserAlreadyExistsError
from app.errors.global_error import GlobalError

async def create_user(new_user: NewUser):
    try:
        await create(new_user)
        
        return JSONResponse(
            content={"message": "Usuário cadastrado com sucesso."},
            status_code=status.HTTP_201_CREATED
        )
    except UserAlreadyExistsError as error:
        return JSONResponse(
            content={"message_error": str(error)},
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    except GlobalError as error:
        return JSONResponse(
            content={"message_error": str(error)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    except Exception as error:
        return JSONResponse(
            content={"message_error": "Não foi possível criar um novo usuário, tente novamente."},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )