from flask import Blueprint, jsonify

from new_api.util.def_methods import reply_json

util = Blueprint('util', __name__)


@util.route('/')
def server_state():
    return reply_json(1)


@util.route('/require_login')
def require_login():
    return reply_json(0)
