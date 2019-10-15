from flask import Blueprint, request, redirect
from sqlalchemy import or_

from new_api.db import database
from new_api.util.face_methods import check_face_vector
from new_api.util.right_methods import check_rights
from new_api.util.def_methods import reply_json, generate_password, new_token, login_confirm, get_user_model
from new_api.util.user_action_methods import record_user_action

user = Blueprint('user', __name__)


@user.before_request
def before_request():
    return login_confirm()


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


@user.route('/get_user_info')
def get_user_info():
    """
    获取用户信息
    :return:
    """
    token = request.values.get('token')
    user_info = get_user_model(token=token)
    if user_info:
        data = {
            'id': user_info.ID,
            'username': user_info.username,
            'head': user_info.head,
            'desc': user_info.desc,
            's_num': user_info.Snum,
            'phone': user_info.phone,
        }
        return reply_json(1, data)
    return reply_json(404)


@user.route('/change_password', methods=['POST'])
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
def change_face_vector():
    """
    修改人脸识别信息
    :return:
    """
    token = request.form['token']
    face_vector = request.form['face_vector']
    user_info = database.update('User', [database.get_model('User').token == token], {'face_vector': face_vector})
    if user_info:
        return reply_json(1)
    return reply_json(-1)
