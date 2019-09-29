from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from new_api.db.database import Base


class Model(Base):
    __tablename__ = 'tag'

    ID = Column(INTEGER(5), primary_key=True,autoincrement=True)
    name = Column(VARCHAR(20), nullable=False, comment='tag名')
    father = Column(INTEGER(5))
