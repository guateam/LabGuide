import hashlib
import random
import string

from flask import jsonify

from new_api.db import database
from new_api.db.database import get_model
from new_api.util.util import REPLY_CODE_LIST


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


def random_char():
    """
    获取随机25个字符的字符串
    :return: 字符串
    """
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 25))  # 获取随机25个字符
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
