import os
import jwt
from jwt import PyJWTError
from fastapi import Request, status, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

bearer_token = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_token)):
    try:
        token = credentials.credentials
        SECRET_KEY = os.getenv("SECRET_KEY")

        data_user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        id_user = data_user.get("sub")

        if not id_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido."
            )
        
        return id_user

    except PyJWTError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido."
            )