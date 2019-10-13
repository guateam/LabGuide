from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from new_api.db.database import Base


class Model(Base):
    __tablename__ = 'article'

    ID = Column(INTEGER(10), primary_key=True, autoincrement=True)
    title = Column(VARCHAR(50), nullable=False, comment='文章名')
    content = Column(LONGTEXT, comment='文章内容')
    time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='修改时间')
    author = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='作者的ID')
    tag = Column(VARCHAR(255), comment='包含的tag,逗号隔开')
    changer = Column(INTEGER(10), nullable=False, server_default=text("'0'"))

    def get_dict(self):
        return {
            'ID': self.ID,
            'title': self.title,
            'content': self.content,
            'time': self.time,
            'author': self.author,
            'tag': self.tag,
            'changer': self.changer
        }
