from flasgger import swag_from
from flask import Blueprint, request

from new_api.db import database
from new_api.rights_control.models.Base import Base
from new_api.rights_control.models.RightControl import RightControl
from new_api.rights_control.rights_control import right_required
from new_api.util.def_methods import reply_json, login_required, get_dicts_from_models
from new_api.util.right_methods import get_right_group_dict
from new_api.util.user_action_methods import record_user_action

right = Blueprint('right', __name__)


@right.route('/add_right', methods=['POST'])
@login_required
@right_required([RightControl])
@swag_from('docs/right/add_right.yml')
def add_right():
    token = request.form['token']
    right_id = request.form['right']
    user_id = request.form['user_id']
    target = request.form['target']
    right_type = request.form['right_type']
    if database.add('UserRight',
                    {'user_right': right_id, 'user_id': user_id, 'target': target, 'right_type': right_type}):
        record_user_action(token=token, code=0, target=user_id)
        return reply_json(1)
    return reply_json(-1)


@right.route('/delete_right', methods=['POST'])
@login_required
@right_required([RightControl])
@swag_from('docs/right/delete_right.yml')
def delete_right():
    token = request.form['token']
    right_id = request.form['right']
    user_id = request.form['user_id']
    right_type = request.form['right_type']
    if database.delete('UserRight', [database.get_model('UserRight').user_right == right_id,
                                     database.get_model('UserRight').user_id == user_id,
                                     database.get_model('UserRight').right_type == right_type,
                                     ]):
        record_user_action(token=token, code=1, target=user_id)
        return reply_json(1)
    return reply_json(-1)


@right.route('/get_right')
@login_required
@swag_from('docs/right/get_right.yml')
def get_right():
    """
    获取权限是否存在
    :return:
    """
    right_id = request.values.get('right_id')
    target = request.values.get('target')
    if not target:
        target = None
    base = Base(right_id=right_id)
    check_model = {'right': base.id, 'right_type': 0, 'target': target}
    return reply_json(1) if check_model in base.get_rights_by_token() else reply_json(-2)


@right.route('/add_right_group', methods=['POST'])
@login_required
@right_required([RightControl])
@swag_from('docs/right/add_right_group.yml')
def add_right_group():
    """
    新建一个用户权限组
    :return:
    """
    name = request.form['name']
    desc = request.form['desc']
    if database.add('UserGroup', {'name': name, 'desc': desc}):
        return reply_json(1)
    return reply_json(-1)


@right.route('/change_right_group', methods=['POST'])
@login_required
@right_required([RightControl])
@swag_from('docs/right/change_right_group.yml')
def change_right_group():
    """
    修改一个用户权限组
    :return:
    """
    group_id = request.form['group_id']
    name = request.form['name']
    desc = request.form['desc']
    if database.update('UserGroup', [database.get_model('UserGroup').ID == group_id], {'name': name, 'desc': desc}):
        return reply_json(1)
    return reply_json(-1)


@right.route('/delete_right_group', methods=['POST'])
@login_required
@right_required([RightControl])
@swag_from('docs/right/delete_right_group.yml')
def delete_right_group():
    """
    清除一个用户权限组
    :return:
    """
    group_id = request.form['group_id']
    if database.delete('UserGroup', database.get_model('UserGroup').ID == group_id):
        return reply_json(1)
    return reply_json(-1)


@right.route('/get_right_group')
@login_required
@swag_from('docs/right/get_right_group.yml')
def get_right_group():
    """
    获取一个用户权限组
    :return:
    """
    group_id = request.values.get('group_id')
    group = database.get('UserGroup', [database.get_model('UserGroup').ID == group_id], first=True)
    if group:
        return reply_json(1, group.get_dict())
    return reply_json(-12)


@right.route('/get_right_groups')
@login_required
@swag_from('docs/right/get_right_groups.yml')
def get_right_groups():
    """
    获取所有用户权限组
    :return:
    """
    groups = database.get('UserGroup', [])
    return reply_json(1, get_dicts_from_models(groups))


@right.route('/add_right_group_right', methods=['POST'])
@login_required
@right_required([RightControl])
@swag_from('docs/right/add_right_group_right.yml')
def add_right_group_right():
    """
    为用户权限组添加权限
    :return:
    """
    group_right = request.form['right']
    group_id = request.form['group_id']
    target = request.form['target']
    right_type = request.form['right_type']
    if database.add('UserGroupRights', {
        'group_right': group_right,
        'group_id': group_id,
        'target': target,
        'right_type': right_type
    }):
        return reply_json(1)
    return reply_json(-1)


@right.route('/change_right_group_right', methods=['POST'])
@login_required
@right_required([RightControl])
@swag_from('docs/right/change_right_group_right.yml')
def change_right_group_right():
    """
    修改特定用户组的特定权限
    :return:
    """
    group_right_id = request.form['group_right_id']
    group_right = request.form['right']
    group_id = request.form['group_id']
    target = request.form['target']
    right_type = request.form['right_type']
    if database.update('UserGroupRights', [database.get_model('UserGroupRights').ID == group_right_id], {
        'group_right': group_right,
        'group_id': group_id,
        'target': target,
        'right_type': right_type
    }):
        return reply_json(1)
    return reply_json(-1)


@right.route('/delete_right_group_right', methods=['POST'])
@login_required
@right_required([RightControl])
@swag_from('docs/right/delete_right_group_right.yml')
def delete_right_group_right():
    """
    清除特定用户组的特定权限
    :return:
    """
    group_right_id = request.form['group_right_id']
    if database.delete('UserGroupRights', [database.get_model('UserGroupRights').ID == group_right_id]):
        return reply_json(1)
    return reply_json(-1)


@right.route('/get_right_group_rights')
@login_required
@right_required([RightControl])
@swag_from('docs/right/get_right_group_rights.yml')
def get_right_group_rights():
    """
    获取特定用户组的所有权限
    :return:
    """
    group_id = request.values.get('group_id')
    rights = database.get('UserGroupRights', [database.get_model('UserGroupRights').group_id == group_id])
    return reply_json(1, get_dicts_from_models(rights))

