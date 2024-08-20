import os
import jwt
from jwt import PyJWTError
from fastapi import Request, status, HTTPException

async def verify_token(request: Request):
    try:
        bearer_token = request.headers.get("authorization")

        if not bearer_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido."
            )
        
        token = bearer_token.split(" ")[1]

        SECRET_KEY = os.getenv("SECRET_KEY")

        data_user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        
        id_user = data_user.get("sub")

        return id_user

    except PyJWTError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido."
            )