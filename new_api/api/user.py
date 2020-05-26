from flasgger import swag_from
from flask import Blueprint, request
from sqlalchemy import or_

from new_api.db import database
from new_api.rights_control.models.AddUser import AddUser
from new_api.rights_control.models.DeleteUser import DeleteUser
from new_api.rights_control.rights_control import right_required
from new_api.util.def_methods import reply_json, generate_password, new_token, get_user_model, login_required, \
    get_dicts_from_models
from new_api.util.face_methods import check_face_vector
from new_api.util.user_action_methods import record_user_action

user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'])
@swag_from('docs/user/login.yml')
def login():
    user_name = request.form['username']
    password = request.form['password']
    user_info = database.get('User', [
        or_(database.get_model('User').username == user_name, database.get_model('User').Snum == user_name, ),
        database.get_model('User').password == generate_password(password), ], first=True)
    if user_info:
        face_vector = request.form['face_vector'].split(',')
        face_vector1 = []
        for i in face_vector:
            face_vector1.append(float(i))
        if user_info.face_vector:
            standard_vector = user_info.face_vector.split(',')
            standard_vector1 = []
            for i in standard_vector:
                standard_vector1.append(float(i))
            if check_face_vector(face_vector1, standard_vector1):
                res = database.update('User', [or_(database.get_model('User').username == user_name,
                                                   database.get_model('User').Snum == user_name, )],
                                      {'token': new_token()})
                if res:
                    record_user_action(2, user_id=user_info.ID)
                    return reply_json(1, {'token': res.token})
                else:
                    return reply_json(-1)
            return reply_json(-8)
        return reply_json(-8)
    return reply_json(-6)


@user.route('/get_face_vector', methods=['POST'])
@swag_from('docs/user/get_face_vector.yml')
def get_face_vector():
    """
    获取面部向量
    :return:
    """
    user_name = request.form['username']
    password = request.form['password']
    user_info = database.get('User', [
        or_(database.get_model('User').username == user_name, database.get_model('User').Snum == user_name, ),
        database.get_model('User').password == generate_password(password), ], first=True)
    if user_info:
        if user_info.face_vector:
            vector = user_info.face_vector.split(',')
            data = []
            for i in vector:
                data.append(float(i))
            return reply_json(1, {'face_vector': data})
        return reply_json(3)
    return reply_json(-6)


@user.route('/get_user')
@login_required
@swag_from('docs/user/get_user.yml')
def get_user():
    """
    获取用户信息
    :return:
    """
    token = request.values.get('token')
    user_info = get_user_model(token=token)
    if user_info:
        data = user_info.get_info_dict()
        return reply_json(1, data)
    return reply_json(404)


@user.route('/get_user_info')
@login_required
@swag_from('docs/user/get_user_info.yml')
def get_user_info():
    """
    获取用户信息
    :return:
    """
    user_id = request.values.get('user_id')
    user_info = get_user_model(user_id=user_id)
    if user_info:
        data = user_info.get_info_dict()
        return reply_json(1, data)
    return reply_json(404)


@user.route('/change_password', methods=['POST'])
@login_required
@swag_from('docs/user/change_password.yml')
def change_password():
    """
    修改密码
    :return:
    """
    token = request.form['token']
    password = request.form['password']
    user_info = database.update('User', [database.get_model('User').token == token],
                                {'password': generate_password(password)})
    if user_info:
        return reply_json(1)
    return reply_json(-1)


@user.route('/change_face_vector', methods=['POST'])
@login_required
@swag_from('docs/user/change_face_vector.yml')
def change_face_vector():
    """
    修改人脸识别信息
    :return:
    """
    token = request.form['token']
    if database.get('User', [database.get_model('User').token == token], first=True):
        face_vector = request.form['face_vector']
        user_info = database.update('User', [database.get_model('User').token == token],
                                    {'face_vector': face_vector})
        if user_info:
            return reply_json(1)
        return reply_json(-1)
    return reply_json(0)


@user.route('/register', methods=['POST'])
@swag_from('docs/user/register.yml')
def register():
    """
    注册功能
    :return:
    """
    s_num = request.form['s_num']
    user_info = database.get('User', [database.get_model('User').Snum == s_num], first=True)
    if user_info:
        if not user_info.password:
            username = request.form['username']
            if database.get('User', [database.get_model('User').username == username]):
                return reply_json(-11)
            password = request.form['password']
            face_vector = request.form['face_vector']

            flag = database.update('User', [database.get_model('User').Snum == s_num],
                                   {'password': generate_password(password), 'username': username,
                                    'face_vector': face_vector})
            if flag:
                database.add('UserRight', {'user_right': flag.group, 'user_id': flag.ID, 'right_type': 1})
                return reply_json(1)
            return reply_json(-1)
        return reply_json(-9)
    return reply_json(-10)


@user.route('/check_s_num')
@swag_from('docs/user/check_s_num.yml')
def check_s_num():
    """
    检查学号是否可以被注册
    :return:
    """
    s_num = request.values.get('s_num')
    user_info = database.get('User', [database.get_model('User').Snum == s_num], first=True)
    if user_info:
        return reply_json(1) if not user_info.password else reply_json(-9)
    return reply_json(-10)


@user.route('/update_new_api', methods=['POST'])
@swag_from('docs/user/update_new_api.yml')
def update_new_api():
    """
    从旧new_api升级到新new_api
    :return:
    """
    username = request.form['username']
    password = request.form['password']
    user_info = database.get('User', [
        or_(database.get_model('User').username == username, database.get_model('User').Snum == username, ),
        database.get_model('User').password == generate_password(password), ], first=True)
    if user_info:
        face_vector = request.form['face_vector']
        flag = database.update('User', [database.get_model('User').ID == user_info.ID],
                               {'face_vector': face_vector})
        if flag:
            database.add('UserRight', {'user_right': -1 if user_info.group == 1 else 0, 'user_id': user_info.ID})
            return reply_json(1)
        return reply_json(-1)
    return reply_json(0)


@user.route('/add_user', methods=['POST'])
@login_required
@right_required([AddUser])
@swag_from('docs/user/add_user.yml')
def add_user():
    """
    添加新用户
    :return:
    """
    s_num = request.form['s_num']
    if not database.get('User', [database.get_model('User').Snum == s_num], first=True):
        group = request.form['group']
        flag = database.add('User', {'Snum': s_num, 'group': group, 'face_vector': ''})
        if flag:
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-9)


@user.route('/get_users')
@login_required
@swag_from('docs/user/get_users.yml')
def get_users():
    """
    获取所有用户
    :return:
    """
    users = database.get('User', [], first=False)
    return reply_json(1, get_dicts_from_models(users))


@user.route('/delete_user', methods=['POST'])
@login_required
@right_required([DeleteUser])
@swag_from('docs/user/delete_user.yml')
def delete_user():
    """
    清除用户
    :return:
    """
    user_id = request.form['user_id']
    flag = database.delete('User', [database.get_model('User').ID == user_id])
    if flag:
        return reply_json(1)
    return reply_json(-1)
