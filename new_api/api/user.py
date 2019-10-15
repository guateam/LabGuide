from flask import Blueprint, request
from sqlalchemy import or_

from new_api.db import database
from new_api.util.def_methods import reply_json, generate_password, new_token, get_user_model, login_required
from new_api.util.face_methods import check_face_vector
from new_api.util.user_action_methods import record_user_action

user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'])
def login():
    user_name = request.form['username']
    password = request.form['password']
    user_info = database.get('User', [
        or_(database.get_model('User').username == user_name, database.get_model('User').Snum == user_name, ),
        database.get_model('User').password == generate_password(password), ], first=True)
    if user_info:
        face_vector = request.form['face_vector']
        standard_vector = user_info.face_vector.split(',')
        if check_face_vector(face_vector, standard_vector):
            res = database.update('User', [database.get_model('User').username == user_name], {'token': new_token()})
            if res:
                record_user_action(2, user_id=user_info.ID)
                return reply_json(1, {'token': res.token})
            else:
                return reply_json(-1)
        return reply_json(-8)
    return reply_json(-6)


@user.route('/get_face_vector', methods=['POST'])
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
        return reply_json(1, {'face_vector': user_info.face_vector.split(',')})
    return reply_json(-6)


@user.route('/get_user')
@login_required
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
def change_face_vector():
    """
    修改人脸识别信息
    :return:
    """
    token = request.form['token']
    face_vector = request.form['face_vector']
    user_info = database.update('User', [database.get_model('User').token == token],
                                {'face_vector': ','.join(face_vector)})
    if user_info:
        return reply_json(1)
    return reply_json(-1)


@user.route('/register')
def register():
    """
    注册功能
    :return:
    """
    s_num = request.form['s_num']
    user_info = database.get('User', [database.get_model('User').Snum == s_num], first=True)
    if user_info:
        if not user_info.password:
            password = request.form['password']
            face_vector = request.form['face_vector']
            username = request.form['username']
            flag = database.update('User', [database.get_model('User').Snum == s_num],
                                   {'password': generate_password(password), 'username': username,
                                    'face_vector': ','.join(face_vector)})
            if flag:
                return reply_json(1)
            return reply_json(-1)
        return reply_json(-9)
    return reply_json(-10)
