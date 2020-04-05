from flask import request

from new_api.db import database
from new_api.rights_control.models import RIGHTS_CODE_LIST
from new_api.rights_control.models.Base import Base


class AddCommentByTag(Base):
    def __init__(self):
        super().__init__(RIGHTS_CODE_LIST['AddCommentByTag'])
        self.article_id = int(request.form['article_id']) if request.method == 'POST' else \
            int(request.values.get('article_id'))
        article = database.get('Article', [database.get_model('Article').ID == self.article_id])
        self.tag_id = int(article.tag.split(',')[-1])

    def check(self) -> bool:
        check_model = {'right': self.id, 'right_type': 0, 'target': self.tag_id}
        return True if check_model in self.get_rights_by_token() else False
