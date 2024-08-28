from app.core.database import session
from app.models.global_models import User
from sqlalchemy import select

async def get(id_user: str):
    user = session.execute(select(User).where(User.id == id_user)).scalar()

    accounts = []

    for account in user.accounts:
        data = {
            'name_account': account.name_account,
            'value_account': account.value_account,
            "due_date": account.due_date,
            "in_the_box": account.in_the_box,
            'status': account.status,
        }

        accounts.append(data)
    
    return accounts