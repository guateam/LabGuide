from new_api.rights_control.models import RIGHTS_CODE_LIST
from new_api.rights_control.models.Base import Base


class AddAllArticleTag(Base):
    def __init__(self):
        """
        允许阅读所有文章权限
        """
        super().__init__(RIGHTS_CODE_LIST['AddAllArticleTag'])

    def check(self) -> bool:
        return self.default_check()
