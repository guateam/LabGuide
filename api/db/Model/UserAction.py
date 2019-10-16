from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from api.db.database import Base


class Model(Base):
    __tablename__ = 'user_action'

    ID = Column(INTEGER(10), primary_key=True,autoincrement=True)
    user_id = Column(INTEGER(10), nullable=False)
    type = Column(INTEGER(10), nullable=False)
    desc = Column(VARCHAR(255))
    target = Column(VARCHAR(255))
    date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
