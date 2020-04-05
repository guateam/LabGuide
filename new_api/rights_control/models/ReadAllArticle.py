from new_api.rights_control.models.Base import Base


class ReadAllArticle(Base):
    def __init__(self):
        """
        允许阅读所有文章权限
        """
        super(ReadAllArticle, self).__init__(1)

    def check(self) -> bool:
        check_model = {'right': self.id, 'right_type': 0, 'target': None}
        return True if check_model in self.get_rights_by_token() else False
