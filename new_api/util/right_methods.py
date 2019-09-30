from sqlalchemy import or_

from new_api.db import database
from new_api.util.util import USER_RIGHTS

user_rights_for_com = {}


def init_rights():
    """
    初始化权限列表
    :return:
    """
    for item in USER_RIGHTS.items():
        if len(item[1]['children']) == 0:
            data = []
            for item1 in USER_RIGHTS.items():
                if item[0] in item1[1]['children']:
                    data.append(item1[0])
            item[1].update({'children': data})
            user_rights_for_com.update({item[0]: item[1]})
    return user_rights_for_com


def check_right(right, target_right, target=None, permit=None):
    """
    检查权限是否包含目标权限，并检查附加值是否相等
    :param right:当前权限
    :param target_right:目标权限
    :param target: 目标附加值（可选）
    :param permit: 当前附加值（可选）
    :return:boolean
    """
    if right in (user_rights_for_com[target_right]['children'] or right == target_right) and (
            target == permit or not target):
        return True
    return False


def check_rights(right, target=None, token=None, user_id=None):
    """
    检查权限
    :param right:目标权限
    :param target: 目标附加值（可选）
    :param token: token（可选）
    :param user_id: 用户id（可选）
    :return:boolean
    """
    if not token and not user_id:
        return False
    user_info = database.get('User',
                             [or_(database.get_model('User').ID == user_id, database.get_model('User').token == token)],
                             first=True)
    rights_info = database.get('UserRight', [database.get_model('UserRight').user_id == user_info.ID])
    for item in rights_info:
        if check_right(item.user_right, right, target, item.target):
            return True
    return False
