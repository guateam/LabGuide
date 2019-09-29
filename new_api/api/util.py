from flask import Blueprint, jsonify

from new_api.util.DefMethods import reply_json

util = Blueprint('util', __name__)


@util.route('/')
def server_state():
    return reply_json(1)
