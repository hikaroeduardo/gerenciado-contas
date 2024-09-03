from pydantic import BaseModel
from datetime import date
from typing import List

class NewAccount(BaseModel):
    name_account: str
    value_account: float
    due_date: str

class ResponseAccountDefault(BaseModel):
    message: str

class DataAccounts(BaseModel):
    name_account: str
    value_account: float
    due_date: date
    in_the_box: bool
    status: bool

class ResponseDataAccounts(BaseModel):
    data: List[DataAccounts]

class ResponseDataAccountsById(BaseModel):
    account: List[DataAccounts]