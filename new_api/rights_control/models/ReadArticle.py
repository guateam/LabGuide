from flask import request

from new_api.rights_control.models.Base import Base


class ReadArticle(Base):
    def __init__(self, article_id):
        super(ReadArticle, self).__init__(0)
        self.article_id = article_id

    def check(self) -> bool:

        return True
