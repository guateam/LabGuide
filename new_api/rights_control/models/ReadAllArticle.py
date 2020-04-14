from new_api.rights_control.models import RIGHTS_CODE_LIST
from new_api.rights_control.models.Base import Base


class ReadAllArticle(Base):
    def __init__(self):
        """
        允许阅读所有文章权限
        """
        super(ReadAllArticle, self).__init__(RIGHTS_CODE_LIST['ReadAllArticle'])

    def check(self) -> bool:
        return self.default_check()
