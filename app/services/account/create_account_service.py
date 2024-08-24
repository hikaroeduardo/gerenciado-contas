from datetime import datetime
from app.core.database import session
from app.models.global_models import Account
from app.models.schemas.account_schemas import NewAccount
from app.errors.global_error import GlobalError

async def create(data: NewAccount, id_user: str):
    date = datetime.strptime(data.due_date, "%d/%m/%Y").date()

    new_account = Account(name_account=data.name_account, value_account=data.value_account, due_date=date, user_id=id_user)

    try:
        session.add(new_account)
        session.commit()
    except:
        raise GlobalError("Não foi possível criar uma nova conta, tente novamente.")
