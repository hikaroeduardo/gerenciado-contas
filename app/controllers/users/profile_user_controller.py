from fastapi import Depends, status
from fastapi.responses import JSONResponse
from app.core.verify_token_middleware import verify_token
from app.services.users.profile_user_service import get_profile
from app.models.schemas.user_schemas import ResponseProfileUser

async def profile_user_controller(id_user: str = Depends(verify_token)) -> ResponseProfileUser:
    try:
        user = await get_profile(id_user=id_user)

        return JSONResponse(
            content=user,
            status_code=status.HTTP_200_OK
        )
    except:
        return JSONResponse(
            content={"message_error": "Não foi possível resgatar os dados de usuário, tente novamente."},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )