from flask import Blueprint, jsonify

from new_api.db import database
from new_api.util.def_methods import reply_json

util = Blueprint('util', __name__)


@util.route('/')
def server_state():
    info = database.get('User', [], first=True)
    if info:
        return reply_json(1)
    return reply_json(-3)


@util.route('/require_login')
def require_login():
    return reply_json(0)
