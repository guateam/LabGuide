from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from new_api.db.database import Base


class Model(Base):
    __tablename__ = 'user_group'

    ID = Column(INTEGER(10), primary_key=True, autoincrement=True)
    desc = Column(VARCHAR(255))
    name = Column(VARCHAR(40), nullable=False)
