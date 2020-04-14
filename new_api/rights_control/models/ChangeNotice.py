from flask import request

from new_api.rights_control.models import RIGHTS_CODE_LIST
from new_api.rights_control.models.Base import Base


class ChangeNotice(Base):
    def __init__(self):
        super().__init__(RIGHTS_CODE_LIST['ChangeNotice'])

    def check(self) -> bool:
        return self.default_check()
