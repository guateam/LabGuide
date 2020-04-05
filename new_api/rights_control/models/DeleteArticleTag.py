from flask import request

from new_api.rights_control.models import RIGHTS_CODE_LIST
from new_api.rights_control.models.Base import Base


class DeleteArticleTag(Base):
    def __init__(self):
        super().__init__(RIGHTS_CODE_LIST['DeleteArticleTag'])
        self.tag_id = int(request.form['tag_id']) if request.method == 'POST' else \
            int(request.values.get('tag_id'))

    def check(self) -> bool:
        check_model = {'right': self.id, 'right_type': 0, 'target': self.tag_id}
        return True if check_model in self.get_rights_by_token() else False
