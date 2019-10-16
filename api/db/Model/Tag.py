from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from api.db.database import Base
from api.util.tags_methods import get_tag_children, get_tag_article


class Model(Base):
    __tablename__ = 'tag'

    ID = Column(INTEGER(5), primary_key=True, autoincrement=True)
    name = Column(VARCHAR(20), nullable=False, comment='tag名')
    father = Column(INTEGER(5), nullable=True)

    def get_dict(self, get_children=False):
        """
        获取字典
        :param get_children: 是否获取子目录
        :return:
        """
        return {
            'ID': self.ID,
            'name': self.name,
            'father': self.father
        } if not get_children else {
            'ID': self.ID,
            'name': self.name,
            'father': self.father,
            'type': 0,
            'children': get_tag_children(self.ID) + get_tag_article(self.ID)
        }
