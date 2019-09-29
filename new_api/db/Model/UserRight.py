from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from new_api.db.database import Base


class Model(Base):
    __tablename__ = 'user_right'

    ID = Column(INTEGER(10), primary_key=True,autoincrement=True)
    user_id = Column(INTEGER(10), nullable=False)
    user_right = Column(INTEGER(10), nullable=False)
    desc = Column(VARCHAR(255))
    state = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
