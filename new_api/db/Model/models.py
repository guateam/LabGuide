# coding: utf-8
from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata




class ArticleTag(Base):
    __tablename__ = 'article_tag'

    id = Column(INTEGER(10), primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    description = Column(VARCHAR(50), nullable=False)
    icon = Column(VARCHAR(50), nullable=False)
    tag_type = Column(VARCHAR(20), nullable=False)
    article_id = Column(INTEGER(10), nullable=False)


class Comment(Base):
    __tablename__ = 'comment'

    ID = Column(INTEGER(10), primary_key=True)
    content = Column(TEXT)
    article_id = Column(INTEGER(10), nullable=False)
    user_id = Column(INTEGER(10), nullable=False)
    father = Column(INTEGER(10))
    time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


t_comment_info = Table(
    'comment_info', metadata,
    Column('ID', INTEGER(10), server_default=text("'0'")),
    Column('content', Text),
    Column('article_id', INTEGER(10)),
    Column('user_id', INTEGER(10)),
    Column('father', INTEGER(10)),
    Column('time', TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column('username', String(20)),
    Column('group', INTEGER(2)),
    Column('head', String(255), server_default=text("'/api/static/default.jpg'")),
    Column('desc', String(45))
)


class History(Base):
    __tablename__ = 'history'

    id = Column(INTEGER(10), primary_key=True)
    article_id = Column(INTEGER(10), nullable=False)
    user_id = Column(INTEGER(10), nullable=False)
    type = Column(INTEGER(2), nullable=False)
    date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    content = Column(TEXT, nullable=False)


class Tag(Base):
    __tablename__ = 'tag'

    ID = Column(INTEGER(5), primary_key=True)
    name = Column(VARCHAR(20), nullable=False, comment='tag名')
    father = Column(INTEGER(5))


class User(Base):
    __tablename__ = 'user'

    ID = Column(INTEGER(10), primary_key=True, nullable=False)
    Snum = Column(VARCHAR(20), primary_key=True, nullable=False, comment='学号')
    username = Column(VARCHAR(20), comment='账号')
    password = Column(VARCHAR(255), comment='密码')
    phone = Column(VARCHAR(20), comment='手机号')
    group = Column(INTEGER(2), comment='用户组')
    token = Column(VARCHAR(40), nullable=False, server_default=text("''"))
    face = Column(VARCHAR(255), comment='人脸图片名')
    desc = Column(VARCHAR(45), nullable=False, comment='签名')
    head = Column(VARCHAR(255), nullable=False, server_default=text("'/api/static/default.jpg'"), comment='头像')


class UserAction(Base):
    __tablename__ = 'user_action'

    ID = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), nullable=False)
    type = Column(INTEGER(10), nullable=False)
    desc = Column(VARCHAR(255))
    target = Column(VARCHAR(255))


class UserRight(Base):
    __tablename__ = 'user_right'

    ID = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), nullable=False)
    user_right = Column(INTEGER(10), nullable=False)
    desc = Column(VARCHAR(255))
    state = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
