from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from new_api.db.database import Base


class Model(Base):
    __tablename__ = 'user_group_right'

    ID = Column(INTEGER(10), primary_key=True, autoincrement=True)
    group_id = Column(INTEGER(10), nullable=False)
    group_right = Column(INTEGER(10), nullable=False)
    desc = Column(VARCHAR(255))
    target = Column(INTEGER(10))
    right_type = Column(INTEGER(10))

    def get_dict(self, check=False):
        """
        获取字典
        :param check: 是否用于对比
        :return:
        """
        return {
            'id': self.ID,
            'group_id': self.group_id,
            'group_right': self.group_right,
            'desc': self.desc,
            'target': self.target,
            'right_type': self.right_type
        } if not check else {
            'right': self.group_right,
            'right_type': self.right_type,
            'target': self.target,
        }
