import functools
import hashlib
import random
import string

import numpy
from flask import jsonify, request, redirect
from sqlalchemy import or_

from api.db import database
from api.db.database import get_model
from api.util.util import REPLY_CODE_LIST, ALLOWED_EXTENSIONS


def reply_json(code, data=None):
    """
    封装的json返回机制
    :param code: util.py中定义好的统一代码
    :param data: payload
    :return: json
    """
    if data is None:
        data = []
    if code in REPLY_CODE_LIST:
        return jsonify({'code': code, 'msg': REPLY_CODE_LIST[code], 'data': data})
    return jsonify({'code': 405, 'msg': REPLY_CODE_LIST[405]})


def generate_password(original_password):
    """
    加密函数，使用sha256对密码进行加密处理
    :param original_password: 原密码
    :return: 加密后的二进制字符串
    """
    salt = 'project_agent'  # 加盐
    sha256 = hashlib.sha256()  # 创建sha256对象
    sha256.update((original_password + salt).encode('utf-8'))  # 加载密码
    return sha256.hexdigest()  # 返回十六进制字符串


def random_char(count=25):
    """
    获取随机25个字符的字符串
    :return: 字符串
    """
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, count))  # 获取随机25个字符
    return ran_str


def new_token():
    """
    获取一个不重复的token
    :return: token
    """
    token = random_char()
    check = database.get('User', [get_model('User').token == token])
    if check:
        return new_token()  # 递归调用
    return token


def get_user_model(user_id=None, token=None):
    """
    通过token或者用户id获取用户实例
    :param user_id: 用户id
    :param token: token
    :return: model(未知用户=None)
    """
    return database.get('User',
                        [or_(database.get_model('User').token == token, database.get_model('User').ID == user_id)],
                        first=True)


def get_username(user_id=None, token=None):
    """
    通过用户id或token获取用户名
    :param user_id: 用户id
    :param token: token
    :return: 用户名（未知用户=''）
    """
    user_info = get_user_model(user_id=user_id, token=token)
    if user_info:
        return user_info.username
    return ''


def get_user_id(token=None):
    """
    通过token获取用户id
    :param token: token
    :return: id（未知用户=-1）
    """
    user_info = get_user_model(token=token)
    if user_info:
        return user_info.ID
    return -1


def get_user_head(user_id=None, token=None):
    """
    通过用户id或者token获取头像
    :param token: token
    :param user_id: 用户id
    :return: 头像（位置用户=''）
    """
    user_info = get_user_model(user_id=user_id, token=token)
    if user_info:
        return user_info.head
    return ''


def get_user_desc(user_id=None, token=None):
    """
    通过用户id或者token获取签名
    :param token: token
    :param user_id: 用户id
    :return: 签名（位置用户=''）
    """
    user_info = get_user_model(user_id=user_id, token=token)
    if user_info:
        return user_info.desc
    return ''


def get_dicts_from_models(models, **args):
    data = []
    for model in models:
        data.append(model.get_dict(**args))
    return data


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def get_euclidean_distance(vec1, vec2):
    dist = numpy.sqrt(numpy.sum(numpy.square(vec1 - vec2)))
    return dist


def login_required(func):
    @functools.wraps(func)  # 修饰内层函数，防止当前装饰器去修改被装饰函数__name__的属性
    def inner(*args, **kwargs):
        token = request.form['token'] if request.method == 'POST' else request.values.get('token')
        user_info = database.get('User', [database.get_model('User').token == token], first=True)
        return redirect('/require_login') if not (
                user_info and token and user_info.face_vector) else func(*args, **kwargs)
    return inner
