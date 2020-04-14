from flask import request

from new_api.rights_control.models import RIGHTS_CODE_LIST
from new_api.rights_control.models.Base import Base


class DeleteComment(Base):
    def __init__(self):
        super().__init__(RIGHTS_CODE_LIST['DeleteComment'])
        self.comment_id = request.form['comment_id'] if request.method == 'POST' else request.values.get('comment_id')

    def check(self) -> bool:
        return False
