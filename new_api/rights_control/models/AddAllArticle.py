from flask import request

from new_api.rights_control.models import RIGHTS_CODE_LIST
from new_api.rights_control.models.Base import Base


class AddAllArticle(Base):
    def __init__(self):
        """
        允许添加所有文章
        """
        super().__init__(RIGHTS_CODE_LIST['AddAllArticle'])

    def check(self) -> bool:
        check_model = {'right': self.id, 'right_type': 0, 'target': None}
        return True if check_model in self.get_rights_by_token() else False
