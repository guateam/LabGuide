from new_api.rights_control.models import RIGHTS_CODE_LIST
from new_api.rights_control.models.Base import Base


class AddAllTag(Base):
    def __init__(self):
        super().__init__(RIGHTS_CODE_LIST['AddAllTag'])

    def check(self) -> bool:
        return self.default_check()
