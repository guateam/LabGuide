from flask import request

from new_api.db import database
from new_api.rights_control.models import RIGHTS_CODE_LIST
from new_api.rights_control.models.Base import Base


class DeleteComment(Base):
    def __init__(self):
        super().__init__(RIGHTS_CODE_LIST['DeleteComment'])
        self.comment_id = int(request.form['comment_id']) if request.method == 'POST' else \
            int(request.values.get('comment_id'))
        self.comment = database.get('Comment', [database.get_model('Comment').ID == self.comment_id])
        if not self.comment:
            raise self.RightInitFailException()

    def check(self) -> bool:
        if self.comment.user_id == self.user_id:
            return True
        check_model = {'right': self.id, 'right_type': 0, 'target': self.comment.article_id}
        return True if check_model in self.get_rights_by_token() else False
