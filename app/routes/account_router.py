from fastapi import APIRouter
from app.controllers.account.create_account_controller import create_accounte

account_routes = APIRouter()

account_routes.post("/create-account")(create_accounte)