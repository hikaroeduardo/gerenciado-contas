from fastapi import APIRouter
from app.controllers.account.create_account_controller import create_accounte
from app.controllers.account.get_all_accounts_controller import get_accounts
from app.controllers.account.get_account_by_id_controller import get_account
from app.controllers.account.pay_account_controller import pay_account

account_routes = APIRouter()

account_routes.post("/create-account")(create_accounte)
account_routes.post('/account/{account_id}/pay')(pay_account)
account_routes.get('/accounts')(get_accounts)
account_routes.get('/account/{account_id}')(get_account)