from flasgger import swag_from
from flask import Blueprint, jsonify

from new_api.db import database
from new_api.util.def_methods import reply_json

util = Blueprint('util', __name__)


@util.route('/')
@swag_from('docs/util/server_state.yml')
def server_state():
    info = database.get('User', [], first=True)
    if info:
        return reply_json(1)
    return reply_json(-3)


@util.route('/require_login')
@swag_from('docs/util/require_login.yml')
def require_login():
    return reply_json(0)


@util.route('/right_check_fail')
@swag_from('docs/util/right_check_fail.yml')
def right_check_fail():
    return reply_json(-2)


@util.route('/doc_definitions')
@swag_from('docs/util/util.yml')
def doc_definitions():
    """
    用于定位doc中的definitions
    :return:
    """
    return reply_json(1)
