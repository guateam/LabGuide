import inspect

from sqlalchemy import Column, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from new_api.db.database import Base


class Model(Base):
    __tablename__ = 'user'

    ID = Column(INTEGER(10), primary_key=True, nullable=False, autoincrement=True)
    Snum = Column(VARCHAR(20), primary_key=True, nullable=False, comment='学号')
    username = Column(VARCHAR(20), comment='账号')
    password = Column(VARCHAR(255), comment='密码')
    phone = Column(VARCHAR(20), comment='手机号')
    group = Column(INTEGER(2), comment='用户组')
    token = Column(VARCHAR(40), nullable=False, server_default=text("''"))
    face = Column(VARCHAR(255), comment='人脸图片名')
    desc = Column(VARCHAR(45), nullable=False, comment='签名')
    head = Column(VARCHAR(255), nullable=False, server_default=text("'/api/api/static/default.jpg'"), comment='头像')
    face_vector = Column(TEXT, nullable=False)

    def get_info_dict(self):
        """
        获取info格式的dict
        :return:
        """
        return {
            'id': self.ID,
            'username': self.username,
            'head': self.head,
            'desc': self.desc,
            's_num': self.Snum,
            'phone': self.phone,
        }
