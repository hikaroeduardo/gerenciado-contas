import os
import jwt
import bcrypt
import datetime
from sqlalchemy import select
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from app.core.database import engine
from app.models.global_models import User
from app.models.schemas.user_schemas import LoginUser
from app.errors.invalid_data_error import InvalidDataError

load_dotenv()

async def login(data_user: LoginUser):
    session = Session(engine)

    user = session.execute(select(User).where(User.email == data_user.email)).scalar()

    if not user:
        raise InvalidDataError("Dados inválidos.")
    
    check_password = bcrypt.checkpw(data_user.password.encode(), user.password)

    if not check_password:
        raise InvalidDataError("Dados inválidos.")
    
    one_day = datetime.datetime.utcnow() + datetime.timedelta(days=1)

    payload = {
        "email": user.email,
        "name": user.name,
        "sub": user.id,
        "exp": one_day
    }

    secret_key = os.getenv("SECRET_KEY")

    token = jwt.encode(payload, secret_key, algorithm="HS256")

    return token