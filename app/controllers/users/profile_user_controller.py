from fastapi import Depends
from app.core.verify_token_middleware import verify_token

async def profile_user_controller(id_user: str = Depends(verify_token)):
    return id_user