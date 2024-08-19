from fastapi import APIRouter
from app.controllers.users.create_user_controller import create_user
from app.controllers.users.login_user_controller import login_user

user_routes = APIRouter()

user_routes.post("/sign-up")(create_user)
user_routes.post("/login")(login_user)