from flask import Blueprint

from new_api.db import database
from new_api.util.def_methods import reply_json, get_dicts_from_models

notice = Blueprint('notice', __name__)


@notice.route('/get_notice')
def get_notice():
    """
    获取通知
    :return:
    """
    notice_info = database.get('Notice', [], first=False)
    return reply_json(1, get_dicts_from_models(notice_info, formatted=True))
