from flask import Blueprint, request, redirect
from sqlalchemy import or_

from new_api.db import database
from new_api.util.def_methods import reply_json, generate_password, new_token
from new_api.util.util import LOGIN_REQUIRED_LIST

user = Blueprint('user', __name__)


@user.before_request
def before_request():
    if request.path not in LOGIN_REQUIRED_LIST:
        return None
    else:
        token = request.form['token'] if request.method == 'POST' else request.values.get('token')
        user_info = database.get('User', [database.get_model('User').token == token], first=True)
        return redirect('/require_login') if user_info else None


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
            return reply_json(1, {'token': res.token})
        else:
            return reply_json(-1)
    return reply_json(0)
