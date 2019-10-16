# coding: utf-8
from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Notice(Base):
    __tablename__ = 'notice'

    id = Column(INTEGER(10), primary_key=True)
    content = Column(String(255), nullable=False)
    time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    user_id = Column(INTEGER(10), nullable=False)
    type = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
