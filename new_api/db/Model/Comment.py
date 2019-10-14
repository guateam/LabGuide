from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from new_api.db.database import Base
from new_api.util.def_methods import get_user_head, get_user_desc


class Model(Base):
    __tablename__ = 'comment'

    ID = Column(INTEGER(10), primary_key=True, autoincrement=True)
    content = Column(TEXT)
    article_id = Column(INTEGER(10), nullable=False)
    user_id = Column(INTEGER(10), nullable=False)
    father = Column(INTEGER(10))
    time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    def get_dict(self, formatted=False):
        """
        获取字典
        :return:
        """
        return {
            'ID': self.ID,
            'content': self.content,
            'article_id': self.article_id,
            'user_id': self.user_id,
            'father': self.father,
            'time': self.time
        } if not formatted else {
            'ID': self.ID,
            'content': self.content,
            'article_id': self.article_id,
            'user_id': self.user_id,
            'father': self.father,
            'time': self.time.strftime("%Y-%m-%d"),
            'head': get_user_head(user_id=self.user_id),
            'desc': get_user_desc(user_id=self.user_id)
        }
