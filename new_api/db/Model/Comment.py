from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from new_api.db.database import Base


class Model(Base):
    __tablename__ = 'comment'

    ID = Column(INTEGER(10), primary_key=True,autoincrement=True)
    content = Column(TEXT)
    article_id = Column(INTEGER(10), nullable=False)
    user_id = Column(INTEGER(10), nullable=False)
    father = Column(INTEGER(10))
    time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

t_comment_info = Table(
    'comment_info', Base.metadata,
    Column('ID', INTEGER(10), server_default=text("'0'")),
    Column('content', Text),
    Column('article_id', INTEGER(10)),
    Column('user_id', INTEGER(10)),
    Column('father', INTEGER(10)),
    Column('time', TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column('username', String(20)),
    Column('group', INTEGER(2)),
    Column('head', String(255), server_default=text("'/api/api/static/default.jpg'")),
    Column('desc', String(45))
)
