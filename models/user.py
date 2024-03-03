from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str]

    def __repr__(self):
        return f"User(@{self.username})"

# email = mapped_column(String, unique=True, index=True)

# 下面是关于用户的其他属性，例如头像、介绍等
# avatar_url = Column(String)
# bio = Column(String)
