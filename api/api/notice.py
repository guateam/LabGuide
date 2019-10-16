from flask import Blueprint

from api.db import database
from api.util.def_methods import reply_json, get_dicts_from_models

notice = Blueprint('notice', __name__)


@notice.route('/get_notice')
def get_notice():
    """
    获取通知
    :return:
    """
    notice_info = database.get('Notice', [])
    return reply_json(1, get_dicts_from_models(notice_info, formatted=True))
