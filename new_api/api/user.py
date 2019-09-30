from flask import Blueprint, request
from sqlalchemy import or_

from new_api.db import database
from new_api.util.right_methods import check_rights
from new_api.util.def_methods import reply_json, generate_password, new_token, login_confirm
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
        res = database.update('User', [database.get_model('User').username == user_name], {'token': new_token()})
        if res:
            record_user_action(2, user_id=user_info.ID)
            return reply_json(1, {'token': res.token})
        else:
            return reply_json(-1)
    return reply_json(0)


@user.route('/get_user_info')
def get_user_info():
    token = request.values.get('token')
    user_info = database.get('User', [database.get_model('User').token == token], first=True)
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


@user.route('/get_user')
def get_user():
    user_id = request.values.get('user_id')
    user_info = database.get('User', [database.get_model('User').ID == user_id], first=True)
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
    token = request.form['token']
    password = request.form['password']
    user_info = database.update('User', [database.get_model('User').token == token],
                                {'password': generate_password(password)})
    if user_info:
        return reply_json(1)
    return reply_json(-1)


@user.route('/set_right', methods=['POST'])
def set_right():
    token = request.form['token']
    if check_rights(token=token, right=1):
        right = request.form['right']
        user_id = request.form['user_id']
        if database.add('UserRight', {'user_right': right, 'user_id': user_id}):
            record_user_action(token=token, code=0, target=user_id)
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-2)


@user.route('/delete_right', methods=['POST'])
def delete_right():
    token = request.form['token']
    if check_rights(token=token, right=1):
        right = request.form['right']
        user_id = request.form['user_id']
        if database.delete('UserRight', [database.get_model('UserRight').user_right == right,
                                         database.get_model('UserRight').user_id == user_id]):
            record_user_action(token=token, code=1, target=user_id)
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-2)
