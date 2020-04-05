from flasgger import swag_from
from flask import Blueprint

from new_api.db import database
from new_api.rights_control.models.AddNotice import AddNotice
from new_api.rights_control.models.ChangeNotice import ChangeNotice
from new_api.rights_control.models.DeleteNotice import DeleteNotice
from new_api.rights_control.rights_control import right_required
from new_api.util.def_methods import reply_json, get_dicts_from_models, login_required

notice = Blueprint('notice', __name__)


@notice.route('/get_notice')
@swag_from('docs/notice/get_notice.yml')
def get_notice():
    """
    获取通知
    :return:
    """
    notice_info = database.get('Notice', [], first=False)
    return reply_json(1, get_dicts_from_models(notice_info, formatted=True))


@notice.route('/add_notice', methods=['POST'])
@login_required
@right_required([AddNotice])
@swag_from('docs/notice/add_notice.yml')
def add_notice():
    """
    添加通知
    :return:
    """


@notice.route('/change_notice', methods=['POST'])
@login_required
@right_required([ChangeNotice])
@swag_from('docs/notice/change_notice.yml')
def change_notice():
    """
    修改通知
    :return:
    """


@notice.route('/delete_notice', methods=['POST'])
@login_required
@right_required([DeleteNotice])
@swag_from('docs/notice/delete_notice.yml')
def delete_notice():
    """
    清除通知
    :return:
    """
