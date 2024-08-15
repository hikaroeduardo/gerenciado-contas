
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Numeric, ForeignKey
from datetime import date
from typing import List

def current_date():
    return date.today()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    accounts: Mapped[List["Account"]] = relationship(back_populates="user", cascade="all")


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_account: Mapped[str] = mapped_column(String(30))
    value_account = mapped_column(Numeric(precision=7, scale=2))
    due_date: Mapped[date] = mapped_column(Date)
    status: Mapped[bool] = mapped_column(default=False)
    in_the_box: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[date] = mapped_column(Date, default=current_date)
    updated_at: Mapped[date] = mapped_column(Date, default=current_date)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="accounts")