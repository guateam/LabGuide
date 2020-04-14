from flasgger import swag_from
from flask import Blueprint, request
from sqlalchemy import or_

from new_api.db import database
from new_api.rights_control.models.AddAllComment import AddAllComment
from new_api.rights_control.models.AddComment import AddComment
from new_api.rights_control.models.AddCommentByTag import AddCommentByTag
from new_api.rights_control.models.DeleteAllComment import DeleteAllComment
from new_api.rights_control.models.DeleteComment import DeleteComment
from new_api.rights_control.models.ReadAllArticle import ReadAllArticle
from new_api.rights_control.models.ReadArticle import ReadArticle
from new_api.rights_control.rights_control import right_required
from new_api.util.def_methods import reply_json, get_user_id, get_dicts_from_models, login_required

comment = Blueprint('comment', __name__)


@comment.route('/add_comment', methods=['POST'])
@login_required
@right_required([AddComment, AddAllComment, AddCommentByTag])
@swag_from('docs/comment/add_comment.yml')
def add_comment():
    """
    添加评论
    :return:
    """
    token = request.form['token']
    article_id = request.form['article_id']
    content = request.form['content']
    father = request.form['father']
    flag = database.add('Comment', {'content': content, 'article_id': article_id, 'user_id': get_user_id(token),
                                    'father': father})
    if flag:
        return reply_json(1)
    return reply_json(-1)


@comment.route('/get_comment')
@login_required
@right_required([ReadArticle, ReadAllArticle])
@swag_from('docs/comment/get_comment.yml')
def get_comment():
    """
    获取评论
    :return:
    """
    article_id = request.values.get('article_id')
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


@comment.route('/delete_comment', methods=['POST'])
@login_required
@right_required([DeleteComment, DeleteAllComment])
@swag_from('docs/comment/delete_comment.yml')
def delete_comment():
    """
    删除评论
    :return:
    """
    comment_id = request.form['comment_id']
    if database.delete('Comment', [database.get_model('Comment').ID == comment_id]):
        return reply_json(1)
    return reply_json(-1)
