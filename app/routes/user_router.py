from fastapi import APIRouter
from app.controllers.users.create_user_controller import create_user
from app.controllers.users.login_user_controller import login_user
from app.controllers.users.profile_user_controller import profile_user_controller

user_routes = APIRouter(tags=['Users'])

user_routes.post("/sign-up")(create_user)
user_routes.post("/login")(login_user)
user_routes.get("/profile")(profile_user_controller)