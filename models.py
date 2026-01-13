from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import List


class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(20))
    roles: Mapped[str] = mapped_column(String(20))

class Ticket(Base):
    __tablename__ = "ticket"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(20))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    description: Mapped[str] = mapped_column(String(500))
    user: Mapped["User"] = relationship(back_populates="tickets")