from flask import request

from new_api.db import database
from new_api.util.def_methods import get_user_id


class Base:
    def __init__(self, right_id):
        """
        所有权限类的基类，用于抽象化权限
        """
        self.id = right_id
        self.token = request.form['token'] if request.method == 'POST' else request.values.get('token')
        self.user_id = get_user_id(token=self.token)

    def check(self) -> bool:
        """
        检查实例是否符合
        :return: 权限检查是否通过
        """
        pass

    def get_rights_by_token(self) -> list:
        """
        通过token来获取对应用户的所有基础权限
        :return: 权限列表
        """
        data = []
        rights = database.get('Rights', [database.get_model('Rights').user_id == self.user_id])
        for item in rights:
            if item.type == 0:
                data.append()
        return []
