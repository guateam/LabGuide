from flask import Blueprint, request
from sqlalchemy import or_

from api.db import database
from api.util.def_methods import reply_json, generate_password, new_token, get_user_model, login_required
from api.util.face_methods import check_face_vector
from api.util.user_action_methods import record_user_action

user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'])
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
                return reply_json(1)
            return reply_json(-1)
        return reply_json(-9)
    return reply_json(-10)


@user.route('/check_s_num')
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


@user.route('/update_api', methods=['POST'])
def update_api():
    """
    从旧api升级到新api
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
