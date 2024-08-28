from fastapi import APIRouter
from app.controllers.account.create_account_controller import create_accounte
from app.controllers.account.get_all_accounts_controller import get_accounts

account_routes = APIRouter()

account_routes.post("/create-account")(create_accounte)
account_routes.get('/accounts')(get_accounts)