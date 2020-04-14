from new_api.rights_control.models import RIGHTS_CODE_LIST
from new_api.rights_control.models.Base import Base


class DeleteAllComment(Base):
    def __init__(self):
        super().__init__(RIGHTS_CODE_LIST['DeleteAllComment'])

    def check(self) -> bool:
        return self.default_check()
