from app.models.schemas.user_schemas import LoginUser
from app.services.users.login_user_service import login
from app.errors.invalid_data_error import InvalidDataError
from fastapi.responses import JSONResponse
from fastapi import status

async def login_user(data_user: LoginUser):
    try:
        token = await login(data_user)

        return JSONResponse(
            content={"token": token},
            status_code=status.HTTP_200_OK
        )
    except InvalidDataError as error:
        return JSONResponse(
            content={"message_error": str(error)},
            status_code=status.HTTP_400_BAD_REQUEST
        )