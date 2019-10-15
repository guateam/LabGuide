from flask import Blueprint, request

from new_api.db import database
from new_api.util.def_methods import reply_json, get_dicts_from_models, login_required
from new_api.util.right_methods import check_rights
from new_api.util.tags_methods import get_father_tag

tag = Blueprint('tag', __name__)


@tag.route('/get_tag_tree')
@login_required
def get_tag_tree():
    """
    获取tag树
    :return:
    """
    token = request.values.get('token')
    if check_rights(token=token, right=18):
        tags1 = database.get('Tag', [])  # 不知道为啥就这个不能用is None 来查找，没信心搞定的请不要乱动
        tags = []
        for item in tags1:
            if not item.father:
                tags.append(item)
        data = get_dicts_from_models(tags, get_children=True)
        return reply_json(1, data)
    return reply_json(-2)


@tag.route('/get_tag_list')
@login_required
def get_tag_list():
    """
    获取tag链
    :return:
    """
    token = request.values.get('token')
    if check_rights(token=token, right=18):
        tag_id = request.values.get('tag_id')
        tag_info = database.get('Tag', [database.get_model('Tag').ID == tag_id], first=True)
        if tag_info:
            data = [tag_info.ID]
            get_father_tag(tag_info.father, data)
            return reply_json(1, data)
        return reply_json(-5)
    return reply_json(-2)


@tag.route('/add_tag', methods=['POST'])
@login_required
def add_tag():
    """
    添加tag
    :return:
    """
    token = request.form['token']
    father = request.form['father']
    if check_rights(token=token, right=20, target=father):
        name = request.form['name']
        flag = database.add('Tag', {'name': name, 'father': father if father else None})
        if flag:
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-2)


@tag.route('/change_tag', methods=['POST'])
@login_required
def change_tag():
    """
    修改tag
    :return:
    """
    token = request.form['token']
    father = request.form['father']
    if check_rights(token=token, right=22, target=father):
        name = request.form['name']
        tag_id = request.form['tag_id']
        flag = database.update('Tag', [database.get_model('Tag').ID == tag_id],
                               {'name': name, 'father': father if father else None})
        if flag:
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-2)


@tag.route('/delete_tag', methods=['POST'])
@login_required
def delete_tag():
    """
    清除tag
    :return:
    """
    token = request.form['token']
    if check_rights(token=token, right=23):
        tag_id = request.form['tag_id']
        flag = database.delete('Tag', [database.get_model('Tag').ID == tag_id])
        if flag:
            return reply_json(1)
        return reply_json(-1)
    return reply_json(-2)
