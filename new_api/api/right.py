from flask import Blueprint, request

from new_api.db import database
from new_api.util.def_methods import reply_json
from new_api.util.right_methods import check_rights
from new_api.util.user_action_methods import record_user_action

right = Blueprint('right', __name__)


@right.route('/set_right', methods=['POST'])
def set_right():
    token = request.form['token']
    if check_rights(token=token, right=1):
        right_id = request.form['right']
        user_id = request.form['user_id']
        target = request.form['target']
        if database.add('UserRight', {'user_right': right_id, 'user_id': user_id, 'target': target}):
            record_user_action(token=token, code=0, target=user_id)
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-2)


@right.route('/delete_right', methods=['POST'])
def delete_right():
    token = request.form['token']
    if check_rights(token=token, right=1):
        right_id = request.form['right']
        user_id = request.form['user_id']
        if database.delete('UserRight', [database.get_model('UserRight').user_right == right_id,
                                         database.get_model('UserRight').user_id == user_id]):
            record_user_action(token=token, code=1, target=user_id)
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-2)
