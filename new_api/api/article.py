from flask import Blueprint, request
from sqlalchemy import or_

from new_api.db import database
from new_api.util.right_methods import check_rights
from new_api.util.def_methods import reply_json, generate_password, new_token, login_confirm, get_username
from new_api.util.user_action_methods import record_user_action

article = Blueprint('article', __name__)


@article.before_request
def before_request():
    return login_confirm()


@article.route('/get_article')
def get_article():
    """
    获取article
    :return:
    """
    token = request.values.get('token')
    article_id = request.values.get('article_id')
    if check_rights(token=token, right=5, target=article_id):
        article_info = database.get('Article', [database.get_model('Article').ID == article_id], first=True)
        if article_info:
            data = article_info.get_dict()
            data.update({
                'time': article_info.time.strftime("%Y-%m-%d"),
                'author': get_username(article_info.author),
                'changer': get_username(article_info.changer)
            })
            return reply_json(1, data)
        return reply_json(-7)
    return reply_json(-2)
