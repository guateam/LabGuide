import random
import string

from flask import Flask, jsonify, request
from flask_cors import CORS
from db import Database, generate_password

app = Flask(__name__)
CORS(app, supports_credentials=True)

"""
    常量区
"""


@app.route('/')
def base():
    """
    基础回应
    :return:
    """
    return jsonify({'code': 1, 'msg': 'success'})


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
    db = Database()
    token = random_char()
    check = db.get({'token': token}, 'user')  # 检查token是否可用
    if check:
        return new_token()  # 递归调用
    return token


@app.route('/api/account/login', methods=['POST'])
def login():
    """
    登录
    :return:
    """
    username = request.form['username']
    password = request.form['password']
    db = Database()
    user = db.get({'username': username, 'password': generate_password(password)}, 'user')
    if user:
        result = db.update({'username': username, 'password': generate_password(password)}, {'token': new_token()},
                           'user')  # 更新token
        if result:
            return jsonify(
                {'code': 1, 'msg': 'success', 'data': {'token': result['token']}})
        return jsonify({'code': -1, 'msg': 'unable to update token'})  # 失败返回
    return jsonify({'code': 0, 'msg': 'unexpected user'})  # 失败返回


@app.route('/api/account/add_account', methods=['POST'])
def add_account():
    """
    添加账户
    :return:
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token, 'group': 0}, 'user')
    if user:
        username = request.form['username']
        password = request.form['password']
        s_num = request.form['Snum']
        group = request.form['group']
        flag = db.insert({'username': username, 'password': generate_password(password), 'Snum': s_num, 'group': group},
                         'user')
        if flag:
            return jsonify({'code': 1, 'msg': 'success'})
        return jsonify({'code': -1, 'msg': 'unknown error'})
    return jsonify({'code': 0, 'msg': 'permission denied'})


@app.route('/api/account/change_password', methods=['POST'])
def change_password():
    """
    修改密码
    :return:
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token}, 'user')
    if user:
        password = request.form['password']
        flag = db.update({'password': generate_password(password), 'token': token}, 'user')
        if flag:
            return jsonify({'code': 1, 'msg': 'success'})
        return jsonify({'code': -1, 'msg': 'unknown error'})
    return jsonify({'code': 0, 'msg': 'permission denied'})


@app.route('/api/article/add_article', methods=['POST'])
def add_article():
    """
    添加文章
    :return:
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token, 'group': 0}, 'user')
    if user:
        content = request.form['content']
        title = request.form['title']
        tag = request.form['tag']
        flag = db.insert({'content': content, 'title': title, 'tag': tag}, 'article')
        if flag:
            return jsonify({'code': 1, 'msg': 'success'})
        return jsonify({'code': -1, 'msg': 'unknown error'})
    return jsonify({'code': 0, 'msg': 'permission denied'})


@app.route('/api/article/change_article', methods=['POST'])
def change_article():
    """
    修改文章
    :return:
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token, 'group': 0}, 'user')
    if user:
        article_id = request.form['article_id']
        content = request.form['content']
        title = request.form['title']
        tag = request.form['tag']
        flag = db.update({'ID': article_id, 'content': content, 'title': title, 'tag': tag}, 'article')
        if flag:
            return jsonify({'code': 1, 'msg': 'success'})
        return jsonify({'code': -1, 'msg': 'unknown error'})
    return jsonify({'code': 0, 'msg': 'permission denied'})


@app.route('/api/article/delete_article', methods=['POST'])
def delete_article():
    """
    清除文章
    :return:
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token, 'group': 0}, 'user')
    if user:
        article_id = request.form['article_id']
        flag = db.delete({'ID': article_id}, 'article')
        if flag:
            return jsonify({'code': 1, 'msg': 'success'})
        return jsonify({'code': -1, 'msg': 'unknown error'})
    return jsonify({'code': 0, 'msg': 'permission denied'})


@app.route('/api/article/get_article')
def get_article():
    """
    获取文章
    :return:
    """
    token = request.values.get('token')
    db = Database()
    user = db.get({'token': token}, 'user')
    if user:
        article_id = request.values.get('article_id')
        article = db.get({'ID': article_id}, 'article')
        return jsonify({'code': 1, 'msg': 'success', 'data': article})
    return jsonify({'code': 0, 'msg': 'permission denied'})


@app.route('/api/tag/get_articles')
def get_articles():
    """
    获取tag下的文章
    :return:
    """
    token = request.values.get('token')
    db = Database()
    user = db.get({'token': token}, 'user')
    if user:
        tag_id = request.values.get('tag_id')
        articles = db.get({'tag': tag_id}, 'article', 0)
        return jsonify({'code': 1, 'msg': 'success', 'data': articles})
    return jsonify({'code': 0, 'msg': 'permission denied'})


@app.route('/api/tag/get_tag_tree')
def get_tag_tree():
    """
    获取tag树
    :return:
    """
    token = request.values.get('token')
    db = Database()
    user = db.get({'token': token}, 'user')
    if user:
        tags = db.get({'father': db.MYSQL_NULL}, 'tag', 0)
        for tag in tags:
            tag.update({'children': get_tag_child(tag)})
        return jsonify({'code': 1, 'msg': 'success', 'data': tags})
    return jsonify({'code': 0, 'msg': 'permission denied'})


def get_tag_child(tag):
    """
    获取tag的子tag
    :param tag: tag
    :return: children
    """
    db = Database()
    tags = db.get({'father': tag['ID']}, 'tag', 0)
    for item in tags:
        item.update({'children': get_tag_child(item)})
    return tags


@app.route('/api/tag/add_tag', methods=['POST'])
def add_tag():
    """
    添加tag
    :return:
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token, 'group': 0}, 'user')
    if user:
        name = request.form['name']
        father = request.form['father']
        flag = db.insert({'name': name, 'father': father}, 'tag')
        if flag:
            return jsonify({'code': 1, 'msg': 'success'})
        return jsonify({'code': -1, 'msg': 'unknown error'})
    return jsonify({'code': 0, 'msg': 'permission denied'})


@app.route('/api/tag/change_tag', methods=['POST'])
def change_tag():
    """
    修改tag
    :return:
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token, 'group': 0}, 'user')
    if user:
        name = request.form['name']
        father = request.form['father']
        tag_id = request.form['tag_id']
        flag = db.update({'name': name, 'father': father, 'ID': tag_id}, 'tag')
        if flag:
            return jsonify({'code': 1, 'msg': 'success'})
        return jsonify({'code': -1, 'msg': 'unknown error'})
    return jsonify({'code': 0, 'msg': 'permission denied'})


@app.route('/api/tag/delete_tag', methods=['POST'])
def delete_tag():
    """
    清除tag
    :return:
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token, 'group': 0}, 'user')
    if user:
        tag_id = request.form['tag_id']
        flag = db.delete({'ID': tag_id}, 'tag')
        if flag:
            return jsonify({'code': 1, 'msg': 'success'})
        return jsonify({'code': -1, 'msg': 'unknown error'})
    return jsonify({'code': 0, 'msg': 'permission denied'})


if __name__ == '__main__':
    # 开启调试模式，修改代码后不需要重新启动服务即可生效
    # 请勿在生产环境下使用调试模式
    # Flask服务将默认运行在localhost的5000端口上

    # with open('static\\upload\\36.txt', 'rb') as file:
    #     result = pred(file.read())
    #     print(result[0])
    app.run(host='0.0.0.0', port=5000, debug=False)
    # app.run(host='0.0.0.0', port=5000, debug=False)
