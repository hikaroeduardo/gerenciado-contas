from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database.db")

session = Session(engine)