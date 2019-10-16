from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER

from api.db.database import Base


class Model(Base):
    __tablename__ = 'notice'

    id = Column(INTEGER(10), primary_key=True)
    content = Column(String(255), nullable=False)
    time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    user_id = Column(INTEGER(10), nullable=False)
    type = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    status = Column(INTEGER(10), nullable=False, server_default=text("'0'"))

    def get_dict(self, formatted=False):
        """
        获取字典
        :return:
        """
        return {
            'id': self.id,
            'content': self.content,
            'time': self.time,
            'user_id': self.user_id,
            'type': self.type,
            'status': self.status
        } if not formatted else {
            'id': self.id,
            'content': self.content,
            'time': self.time.strftime("%Y-%m-%d"),
            'user_id': self.user_id,
            'type': self.type,
            'status': self.status
        }
