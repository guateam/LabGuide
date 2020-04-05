from flask import request

from new_api.rights_control.models.Base import Base


class ReadArticle(Base):
    def __init__(self, article_id):
        """
        允许阅读特定文章权限
        :param article_id:
        """
        super(ReadArticle, self).__init__(0)
        self.article_id = article_id

    def check(self) -> bool:
        check_model = {'right': self.id, 'right_type': 0, 'target': self.article_id}
        return True if check_model in self.get_rights_by_token() else False
