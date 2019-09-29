from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from new_api.db.database import Base


class Model(Base):
    __tablename__ = 'history'

    id = Column(INTEGER(10), primary_key=True,autoincrement=True)
    article_id = Column(INTEGER(10), nullable=False)
    user_id = Column(INTEGER(10), nullable=False)
    type = Column(INTEGER(2), nullable=False)
    date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    content = Column(TEXT, nullable=False)
