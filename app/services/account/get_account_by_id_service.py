from sqlalchemy import select
from app.core.database import session
from app.models.global_models import User
from app.errors.account_not_found_error import AccountNotFoundError

async def get(account_id: str, id_user: str):
    user = session.execute(select(User).where(User.id == id_user)).scalar()

    account_data = []

    for account in user.accounts:
        if account.id == int(account_id):
            data = {
                'name_account': account.name_account,
                'value_account': account.value_account,
                "due_date": account.due_date,
                "in_the_box": account.in_the_box,
                'status': account.status,
            }

            account_data.append(data)

    if len(account_data) == 0:
        raise AccountNotFoundError("Esta conta não existe para este usuário.")

    return account_data