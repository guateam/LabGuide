from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from new_api.db.database import Base
from new_api.util.def_methods import get_username


class Model(Base):
    __tablename__ = 'history'

    id = Column(INTEGER(10), primary_key=True, autoincrement=True)
    article_id = Column(INTEGER(10), nullable=False)
    user_id = Column(INTEGER(10), nullable=False)
    type = Column(INTEGER(2), nullable=False)
    date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    content = Column(TEXT, nullable=False)

    def get_dict(self, formatted=False):
        """
        获取字典
        :return:
        """
        return {
            'id': self.id,
            'article_id': self.article_id,
            'user_id': self.user_id,
            'type': self.type,
            'data': self.date,
            'content': self.content
        } if not formatted else {
            'id': self.id,
            'article_id': self.article_id,
            'user_id': self.user_id,
            'type': self.type,
            'content': self.content,
            'username': get_username(self.user_id),
            'date': self.date.strftime("%Y-%m-%d %H:%M:%S")
        }
