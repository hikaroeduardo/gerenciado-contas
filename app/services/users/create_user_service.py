import bcrypt
from sqlalchemy import select
from app.core.database import session
from app.models.global_models import User
from app.models.schemas.user_schemas import NewUser
from app.errors.global_error import GlobalError
from app.errors.user_already_exists_error import UserAlreadyExistsError

async def create(new_user: NewUser):
    user_exist = session.execute(select(User).where(User.email == new_user.email)).scalar()

    if user_exist:
        raise UserAlreadyExistsError("Este usuário ja está cadastrado.")
    
    encode_password = new_user.password.encode()
    
    hash_password = bcrypt.hashpw(encode_password, bcrypt.gensalt(8))

    user = User(name=new_user.name, email=new_user.email, password=hash_password)

    try:
        session.add(user)
        session.commit()
    except:
        raise GlobalError("Não foi possível criar um novo usuário, tente novamente.")
