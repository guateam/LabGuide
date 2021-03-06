from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from new_api.db.database import Base
from new_api.util.def_methods import get_username


class Model(Base):
    __tablename__ = 'article'

    ID = Column(INTEGER(10), primary_key=True, autoincrement=True)
    title = Column(VARCHAR(50), nullable=False, comment='文章名')
    content = Column(LONGTEXT, comment='文章内容')
    time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='修改时间')
    author = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='作者的ID')
    tag = Column(VARCHAR(255), comment='包含的tag,逗号隔开')
    changer = Column(INTEGER(10), nullable=False, server_default=text("'0'"))

    def get_dict(self, formatted=False):
        """
        获取字典
        :return:
        """
        return {
            'ID': self.ID,
            'title': self.title,
            'content': self.content,
            'time': self.time,
            'author': self.author,
            'tag': self.tag,
            'changer': self.changer
        } if not formatted else {
            'ID': self.ID,
            'title': self.title,
            'content': self.content,
            'tag': self.tag,
            'time': self.time.strftime("%Y-%m-%d"),
            'author': get_username(self.author),
            'changer': get_username(self.changer)
        }

    def get_history_format(self, user_id=None):
        """
        获取用于历史记录的字典形式
        :return:
        """
        return {
            'article_id': self.ID,
            'content': self.content,
            'type': 0,
            'user_id': user_id if user_id else self.author,
        }

    def get_tag_format(self):
        """
        获取侧边栏所需的字典格式
        :return:
        """
        return {
            'name': self.title,
            'ID': self.ID,
            'children': [],
            'type': 1
        }
