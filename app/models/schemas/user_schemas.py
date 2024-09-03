from pydantic import BaseModel

class NewUser(BaseModel):
    name: str
    email: str
    password: str

class LoginUser(BaseModel):
    email: str
    password: str

class ResponseProfileUser(BaseModel):
    name: str
    email: str