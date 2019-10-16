from flask import Blueprint, request
from sqlalchemy import or_

from api.db import database
from api.util.def_methods import reply_json, get_user_id, get_dicts_from_models, login_required
from api.util.right_methods import check_rights

comment = Blueprint('comment', __name__)


@comment.route('/add_comment', methods=['POST'])
@login_required
def add_comment():
    """
    添加评论
    :return:
    """
    token = request.form['token']
    article_id = request.form['article_id']
    if check_rights(token=token, right=17, target=article_id):
        content = request.form['content']
        father = request.form['father']
        flag = database.add('Comment', {'content': content, 'article_id': article_id, 'user_id': get_user_id(token),
                                        'father': father})
        if flag:
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-2)


@comment.route('/get_comment')
@login_required
def get_comment():
    """
    获取评论
    :return:
    """
    token = request.values.get('token')
    article_id = request.values.get('article_id')
    if check_rights(token=token, right=5, target=article_id):
        comments = database.get('Comment', [
            or_(database.get_model('Comment').father is None, database.get_model('Comment').father == ''),
            database.get_model('Comment').article_id == article_id])
        data = []
        for item in comments:
            children = database.get('Comment', [database.get_model('Comment').father == item.ID])
            father = item.get_dict(formatted=True)
            father.update({'children': get_dicts_from_models(children, formatted=True)})
            data.append(father)
        return reply_json(1, data)
    return reply_json(-2)
