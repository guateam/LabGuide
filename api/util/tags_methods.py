from api.db import database
from api.util.def_methods import get_dicts_from_models


def get_tag_children(tag_id):
    """
    获取tag的子目录
    :param tag_id: tag id
    :return: dict
    """
    children = database.get('Tag', [database.get_model('Tag').father == tag_id])
    return get_dicts_from_models(children, get_children=True)


def get_tag_article(tag_id):
    """
    获取tag树中的文章
    :param tag_id:tag id
    :return:dict
    """
    articles = database.get('Article', [database.get_model('Article').tag == tag_id])
    data = []
    for article in articles:
        data.append(article.get_tag_format())
    return data


def get_father_tag(father_id, tag_list):
    """
    获取父tag
    :return:
    """
    father = database.get('Tag', [database.get_model('Tag').ID == father_id], first=True)
    if father:
        tag_list.insert(0, father.ID)
        get_father_tag(father.father, tag_list)
