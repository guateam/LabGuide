from flask import Blueprint, request

from new_api.db import database
from new_api.util.def_methods import reply_json, login_confirm, get_username, get_user_id
from new_api.util.right_methods import check_rights

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


@article.route('/add_article', methods=['POST'])
def add_article():
    """
    添加文章
    :return:
    """
    token = request.form['token']
    tag = request.form['tag']
    if check_rights(right=6, target=tag):
        content = request.form['content']
        title = request.form['title']
        flag = database.add('Article', {'content': content, 'title': title, 'tag': tag, 'author': get_user_id(token)})
        if flag:
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-2)


@article.route('/change_article', methods=['POST'])
def change_article():
    """
    修改文章
    :return:
    """
    token = request.form['token']
    article_id = request.form['article_id']
    if check_rights(right=9, target=article_id):
        content = request.form['content']
        title = request.form['title']
        tag = request.form['tag']
        flag = database.update('Article', [database.get_model('Article').ID == article_id],
                               {'content': content, 'title': title, 'tag': tag, 'changer': get_user_id(token)})
        if flag:
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-2)


@article.route('/delete_article', methods=['POST'])
def delete_article():
    """
    清除文章
    :return:
    """
    article_id = request.form['article_id']
    if check_rights(right=7, target=article_id):
        flag = database.delete('Article', [database.get_model('Article').ID == article_id])
        if flag:
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-2)
