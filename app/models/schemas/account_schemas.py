from pydantic import BaseModel

class NewAccount(BaseModel):
    name_account: str
    value_account: float
    due_date: str

class ResponseCreateAccount(BaseModel):
    message: str
