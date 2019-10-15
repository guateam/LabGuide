# coding: utf-8
from sqlalchemy import Column, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Article(Base):
    __tablename__ = 'article'

    ID = Column(INTEGER(10), primary_key=True)
    title = Column(VARCHAR(50), nullable=False, comment='文章名')
    content = Column(LONGTEXT, comment='文章内容')
    time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='修改时间')
    author = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='作者的ID')
    tag = Column(VARCHAR(255), comment='包含的tag,逗号隔开')
    changer = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


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
    token = Column(VARCHAR(40), server_default=text("''"))
    face = Column(VARCHAR(255), comment='人脸图片名')
    desc = Column(VARCHAR(45), comment='签名')
    head = Column(VARCHAR(255), server_default=text("'/api/api/static/default.jpg'"), comment='头像')
    face_vector = Column(TEXT)


class UserAction(Base):
    __tablename__ = 'user_action'

    ID = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), nullable=False)
    type = Column(INTEGER(10), nullable=False)
    desc = Column(VARCHAR(255))
    target = Column(VARCHAR(255))
    date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class UserRight(Base):
    __tablename__ = 'user_right'

    ID = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), nullable=False)
    user_right = Column(INTEGER(10), nullable=False)
    desc = Column(VARCHAR(255))
    target = Column(INTEGER(10))
