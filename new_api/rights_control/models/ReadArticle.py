from flask import request

from new_api.db import database
from new_api.rights_control.models import RIGHTS_CODE_LIST
from new_api.rights_control.models.Base import Base


class ReadArticle(Base):
    def __init__(self):
        """
        允许阅读特定文章权限
        """
        super(ReadArticle, self).__init__(RIGHTS_CODE_LIST['ReadArticle'])
        self.article_id = int(request.form['article_id']) if request.method == 'POST' else \
            int(request.values.get('article_id'))

    def check(self) -> bool:
        check_model = {'right': self.id, 'right_type': 0, 'target': self.article_id}
        return True if check_model in self.get_rights_by_token() else False
