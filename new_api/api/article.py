from flasgger import swag_from
from flask import Blueprint, request

from new_api.db import database
from new_api.rights_control.models.AddAllArticle import AddAllArticle
from new_api.rights_control.models.AddAllArticleTag import AddAllArticleTag
from new_api.rights_control.models.AddArticle import AddArticle
from new_api.rights_control.models.AddArticleTag import AddArticleTag
from new_api.rights_control.models.ChangeAllArticle import ChangeAllArticle
from new_api.rights_control.models.ChangeAllArticleTag import ChangeAllArticleTag
from new_api.rights_control.models.ChangeArticle import ChangeArticle
from new_api.rights_control.models.ChangeArticleTag import ChangeArticleTag
from new_api.rights_control.models.DeleteAllArticle import DeleteAllArticle
from new_api.rights_control.models.DeleteAllArticleTag import DeleteAllArticleTag
from new_api.rights_control.models.DeleteArticle import DeleteArticle
from new_api.rights_control.models.DeleteArticleTag import DeleteArticleTag
from new_api.rights_control.models.ReadAllArticle import ReadAllArticle
from new_api.rights_control.models.ReadArticle import ReadArticle
from new_api.rights_control.rights_control import right_required
from new_api.util.def_methods import reply_json, get_user_id, get_dicts_from_models, \
    login_required

article = Blueprint('article', __name__)


@article.route('/get_article')
@login_required
@right_required([ReadArticle, ReadAllArticle])
@swag_from('docs/article/get_article.yml')
def get_article():
    """
    获取article
    :return:
    """
    article_id = request.values.get('article_id')
    article_info = database.get('Article', [database.get_model('Article').ID == article_id], first=True)
    if article_info:
        data = article_info.get_dict(formatted=True)
        return reply_json(1, data)
    return reply_json(-7)


@article.route('/add_article', methods=['POST'])
@login_required
@right_required([AddArticle, AddAllArticle])
@swag_from('docs/article/add_article.yml')
def add_article():
    """
    添加文章
    :return:
    """
    token = request.form['token']
    tag = request.form['tag']
    content = request.form['content']
    title = request.form['title']
    flag = database.add('Article', {'content': content, 'title': title, 'tag': tag, 'author': get_user_id(token)})
    if flag:
        database.add('History', flag.get_history_format())
        return reply_json(1)
    return reply_json(-1)


@article.route('/change_article', methods=['POST'])
@login_required
@right_required([ChangeArticle, ChangeAllArticle])
@swag_from('docs/article/change_article.yml')
def change_article():
    """
    修改文章
    :return:
    """
    token = request.form['token']
    article_id = request.form['article_id']
    content = request.form['content']
    title = request.form['title']
    tag = request.form['tag']
    flag = database.update('Article', [database.get_model('Article').ID == article_id],
                           {'content': content, 'title': title, 'tag': tag, 'changer': get_user_id(token)})
    if flag:
        database.add('History', flag.get_history_format(user_id=get_user_id(token)))
        return reply_json(1)
    return reply_json(-1)


@article.route('/delete_article', methods=['POST'])
@login_required
@right_required([DeleteArticle, DeleteAllArticle])
@swag_from('docs/article/delete_article.yml')
def delete_article():
    """
    清除文章
    :return:
    """
    article_id = request.form['article_id']
    flag = database.delete('Article', [database.get_model('Article').ID == article_id])
    if flag:
        return reply_json(1)
    return reply_json(-1)


@article.route('/add_article_tag', methods=['POST'])
@login_required
@right_required([AddArticleTag, AddAllArticleTag])
@swag_from('docs/article/add_article_tag.yml')
def add_article_tag():
    """
    添加文章标签
    :return:
    """
    article_id = request.form['article_id']
    name = request.form['name']
    tag_type = request.form['tag_type']
    icon = request.form['icon']
    description = request.form['description']
    flag = database.add('ArticleTag',
                        {'article_id': article_id, 'name': name, 'description': description, 'icon': icon,
                         'tag_type': tag_type})
    if flag:
        return reply_json(1)
    return reply_json(-1)


@article.route('/change_article_tag', methods=['POST'])
@login_required
@right_required([ChangeArticleTag, ChangeAllArticleTag])
@swag_from('docs/article/change_article_tag.yml')
def change_article_tag():
    """
    修改文章标签
    :return:
    """
    tag_id = request.form['tag_id']
    name = request.form['name']
    tag_type = request.form['tag_type']
    icon = request.form['icon']
    description = request.form['description']
    flag = database.update('ArticleTag', [database.get_model('ArticleTag').id == tag_id],
                           {'name': name, 'description': description, 'icon': icon, 'tag_type': tag_type})
    if flag:
        return reply_json(1)
    return reply_json(-1)


@article.route('/delete_article_tag', methods=['POST'])
@login_required
@right_required([DeleteArticleTag, DeleteAllArticleTag])
@swag_from('docs/article/delete_article_tag.yml')
def delete_article_tag():
    """
    清除文章标签
    :return:
    """
    tag_id = request.form['tag_id']
    flag = database.delete('ArticleTag', [database.get_model('ArticleTag').id == tag_id])
    if flag:
        return reply_json(1)
    return reply_json(-1)


@article.route('/get_article_tag')
@login_required
@right_required([ReadArticle, ReadAllArticle])
@swag_from('docs/article/get_article_tag.yml')
def get_article_tag():
    """
    获取文章标题
    :return:
    """
    article_id = request.values.get('article_id')
    tags = database.get('ArticleTag', [database.get_model('ArticleTag').article_id == article_id])
    data = get_dicts_from_models(tags)
    return reply_json(1, data=data)


@article.route('/get_history')
@login_required
@right_required([ReadArticle, ReadAllArticle])
@swag_from('docs/article/get_history.yml')
def get_history():
    """
    获取历史列表
    :return:
    """
    article_id = request.values.get('article_id')
    history = database.get('History', [database.get_model('History').article_id == article_id])
    data = get_dicts_from_models(history, formatted=True)
    return reply_json(1, data)


@article.route('/get_history_article')
@login_required
@right_required([ReadArticle, ReadAllArticle])
@swag_from('docs/article/get_history_article.yml')
def get_history_article():
    """
    获取历史文章
    :return:
    """
    history_id = request.values.get('history_id')
    history = database.get('History', [database.get_model('History').id == history_id], first=True)
    return reply_json(1, history.get_dict(formatted=True)) if history else reply_json(-7)
