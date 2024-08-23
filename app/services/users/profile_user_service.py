from sqlalchemy import select
from app.models.global_models import User
from app.core.database import session

async def get_profile(id_user: str):
    response = session.execute(select(User).where(User.id == id_user)).scalar()

    user_data = {
        "name": response.name,
        "email": response.email
    }

    return user_data