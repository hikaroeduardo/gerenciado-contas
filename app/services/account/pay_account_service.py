from sqlalchemy import select
from app.core.database import session
from app.models.global_models import User
from app.errors.paid_account_error import PaidAccountError
from app.errors.account_not_found_error import AccountNotFoundError

async def pay(account_id: str, id_user: str):
    user = session.execute(select(User).where(User.id == id_user)).scalar()

    existing_account = []

    for account in user.accounts:
        if account.id == int(account_id):
            if account.status == True:
                raise PaidAccountError("Esta conta ja está paga.")
            
            account.status = True

            existing_account.append(account)

            session.commit()

    if len(existing_account) == 0:
        raise AccountNotFoundError("Esta conta não existe para este usuário.")
