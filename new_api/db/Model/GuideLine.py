from sqlalchemy import Column, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER, TEXT

from new_api.db.database import Base
from new_api.util.def_methods import get_username


class Model(Base):
    __tablename__ = 'guide_line'
