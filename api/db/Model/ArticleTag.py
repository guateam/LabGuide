from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from api.db.database import Base


class Model(Base):
    __tablename__ = 'article_tag'

    id = Column(INTEGER(10), primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    description = Column(VARCHAR(50), nullable=False)
    icon = Column(VARCHAR(50), nullable=False)
    tag_type = Column(VARCHAR(20), nullable=False)
    article_id = Column(INTEGER(10), nullable=False)

    def get_dict(self):
        """
        获取字典类型
        :return:
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'icon': self.icon,
            'tag_type': self.tag_type,
            'article_id': self.article_id
        }
