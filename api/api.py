import random
import string
import time
import urllib, sys
import ssl
import json
import base64
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from db import Database, generate_password
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, supports_credentials=True)

"""
    常量区
"""
ALLOWED_EXTENSIONS = ['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF']  # 允许上传的格式
HOST_NAME = 'http://localhost:5000'
ACCESS_TOKEN = "24.cd50fc3b214bd87bd7adef96b8399ea2.2592000.1560230556.282335-16225579"
FILE_PATH = 'D:/labguide/LabGuide'


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
    way = request.form['way']
    if way == "用户名":
        way = "username"
    elif way == "学号":
        way = "Snum"
    else:
        return jsonify({'code': 0, 'msg': 'no way'})

    db = Database()
    user = db.get({way: username, 'password': generate_password(password)}, 'user')
    if user:
        result = db.update({way: username, 'password': generate_password(password)}, {'token': new_token()},
                           'user')  # 更新token
        return jsonify({'code': 1, 'msg': 'success',
                        'data': {'token': result['token'], 'username': result['username'], 'id': result['ID'],
                                 'group': result['group']}})
    return jsonify({'code': 0, 'msg': 'unexpected user'})  # 失败返回


@app.route('/api/account/check_account', methods=['POST'])
def check_account():
    """
    人脸检测之前的账号密码核对
    :return:
    """
    username = request.form['username']
    password = request.form['password']
    way = request.form['way']
    db = Database()
    if way == "用户名":
        way = "username"
    elif way == "学号":
        way = "Snum"
    else:
        return jsonify({'code': 0, 'msg': 'no way'})

    user = db.get({way: username, 'password': generate_password(password)}, 'user')
    if user:
        return jsonify({'code': 1, 'msg': 'success'})
    return jsonify({'code': 0, 'msg': 'unexpected user'})  # 失败返回


@app.route('/api/account/get_all_student_info')
def get_all_student_info():
    """
    获取所有学生的基本信息
    :return:
    """
    token = request.values.get('token')
    db = Database()
    user = db.get({'token': token, 'group': 0}, 'user')
    if user:

        data = db.get({}, 'user')
        if data:
            for it in data:
                it.pop("password")
                it.pop("token")
                it.pop("ID")
                it.pop("face")
                tp = it['group']
                if tp == 1:
                    tp = "学生"
                elif tp == 0:
                    tp = "管理员"

                it.update({'group': tp})
        return jsonify({'code': 1, 'msg': 'success', 'data': data})

    return jsonify({'code': 0, 'msg': 'unexpected user'})  # 失败返回


@app.route('/api/account/modify_info')
def modify_info():
    """
    修改用户自身的信息
    :return:
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token}, 'user')
    if user:
        password = request.form['password']
        phone = request.form['phone']
        face = request.form['face']
        # base64转图片
        imgdata = base64.b64decode(face)
        filename = random_char() + ".bmp"
        # 改成绝对路径
        file = open(FILE_PATH + "/face/" + filename, 'wb')
        file.write(imgdata)
        file.close()
        res = db.update({'token': token}, {'password': generate_password(password), 'phone': phone, 'face': filename},
                        'user')
        return jsonify({'code': 1, 'msg': 'success'})
    return jsonify({'code': 0, 'msg': 'unexpected user'})  # 失败返回


@app.route('/api/account/admin_modify_info', methods=['POST'])
def admin_modify_info():
    """
    管理员修改他人信息
    :return:
    """
    db = Database()

    token = request.form['token']
    user = db.get({'token': token, 'group': 0}, 'user')
    if not user:
        return jsonify({'code': 0, 'msg': 'unexpected user'})  # 失败返回

    username = request.form['username']
    snum = request.form['snum']
    exist = db.get({'username': username}, 'user')
    if exist:
        if exist['Snum'] != snum:
            return jsonify({'code': -1, 'msg': 'username is already exist'})

    phone = request.form['phone']
    group = request.form['group']
    res = db.update({'Snum': snum}, {'username': username, 'phone': phone, 'group': group},
                    'user')
    if res:
        return jsonify({'code': 1, 'msg': 'success'})

    return jsonify({'code': -2, 'msg': 'fail'})


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


@app.route('/api/account/register', methods=['POST'])
def register():
    db = Database()
    snum = request.form['snum']
    username = request.form['username']
    password = request.form['password']
    repeat_by_username = db.get({'Snum': username}, 'user')
    if repeat_by_username:
        if repeat_by_username['Snum'] != snum:
            return jsonify({'code': -2, 'msg': 'repeat Snum'})

    face = request.form['face']
    # base64转图片
    imgdata = base64.b64decode(face)
    filename = random_char() + ".bmp"
    file = open(FILE_PATH + "/face/" + filename, 'wb')
    file.write(imgdata)
    file.close()

    user = db.get({'Snum': snum}, 'user')
    if user:
        repeat = db.get({'username': username}, 'user')
        if repeat:
            return jsonify({'code': -2, 'msg': 'repeat username'})

        flag = db.update({'Snum': snum},
                         {'username': username, 'password': generate_password(password), 'face': filename, 'group': 1},
                         'user')
        if flag:
            return jsonify({'code': 1, 'msg': 'success'})
        return jsonify({'code': 0, 'msg': 'unknown error'})
    return jsonify({'code': -1, 'msg': 'user not found'})


@app.route('/api/account/add_new_student', methods=['POST'])
def add_new_student():
    snum = request.form['snum']
    token = request.form['token']

    db = Database()
    admin = db.get({'token': token, 'group': 0}, 'user')
    if admin:
        exist = db.get({'Snum': snum, 'group': 1}, 'user')
        if exist:
            return jsonify({"code": -2, 'msg': "user exist"})
        result = db.insert({'Snum': snum, 'group': 1}, 'user')
        if result:
            return jsonify({"code": 1, 'msg': "success"})
        return jsonify({"code": 0, 'msg': "error"})
    return jsonify({"code": -1, 'msg': "permission denied"})


@app.route('/api/account/check_snum', methods=['POST'])
def check_snum():
    snum = request.form['snum']
    db = Database()
    user = db.get({'Snum': snum}, 'user')
    if user:
        if user['username'] and user['password'] and user['face']:
            return jsonify({'code': -1, 'msg': 'already exist'})
        return jsonify({'code': 1, 'msg': 'success'})
    return jsonify({'code': 0, 'msg': 'user not found'})


@app.route('/api/account/get_basic_info', methods=['POST'])
def get_basic_info():
    token = request.form['token']
    db = Database()
    user = db.get({'token': token}, 'user')
    if user:
        data = {
            'username': user['username'],
            'group': user['group'],
            'snum': user['Snum']
        }
        return jsonify({'code': 1, 'msg': 'success', 'data': data})
    return jsonify({'code': 0, 'msg': 'user not found'})


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


@app.route('/api/account/delete_account', methods=['POST'])
def delete_account():
    """
    删除账号
    :return:
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token, 'group': 0}, 'user')
    if not user:
        return jsonify({'code': 0, 'msg': 'permission denied'})

    snum = request.form['snum']
    if user['Snum'] == snum:
        return jsonify({'code': -2, 'msg': 'cant delete self'})

    flag = db.delete({'Snum': snum}, 'user')
    if flag:
        return jsonify({'code': 1, 'msg': 'success'})

    return jsonify({'code': -1, 'msg': 'unknown error'})


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
        flag = db.insert({'content': content, 'title': title, 'tag': tag, 'author': user['ID']}, 'article')
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
        flag = db.new_update({'ID': article_id},
                             {'content': content, 'title': title, 'tag': tag, 'changer': user['ID']}, 'article')
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
        if article:
            article.update({'time': article['time'].strftime("%Y-%m-%d"), 'author': get_user(article['author']),
                            'changer': get_user(article['changer'])})
            return jsonify({'code': 1, 'msg': 'success', 'data': article})
        return jsonify({'code': -1, 'msg': 'unknown article'})
    return jsonify({'code': 0, 'msg': 'permission denied'})


def get_user(id):
    """
    获取用户名称
    :param id:
    :return:
    """
    db = Database()
    user = db.get({'ID': id}, 'user')
    if user:
        return user['username']
    return ''


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
        for article in articles:
            article.update({'time': article['time'].strftime("%Y-%m-%d"), 'author': get_user(article['author']),
                            'changer': get_user(article['changer'])})
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
        tags1 = db.get({'father': ''}, 'tag', 0)
        tags = tags + tags1
        for tag in tags:
            tag.update({'children': get_tag_child(tag) + in_get_articles(tag), 'type': 0})
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
        item.update({'children': get_tag_child(item) + in_get_articles(item), 'type': 0})
    return tags


def in_get_articles(tag):
    """
    获取tag下的文章
    :param tag:
    :return:
    """
    db = Database()
    articles = db.get({'tag': tag['ID']}, 'article', 0)
    data = []
    for item in articles:
        data.append({
            'name': item['title'],
            'ID': item['ID'],
            'children': [],
            'type': 1
        })
    return data


@app.route('/api/tag/get_tag_list')
def get_tag_list():
    """
    获取tag列表
    :return:
    """
    token = request.values.get('token')
    db = Database()
    user = db.get({'token': token}, 'user')
    if user:
        tag_id = request.values.get('tag_id')
        tag = db.get({'ID': tag_id}, 'tag')
        if tag:
            tag_list = [tag['ID']]
            get_father_tag(tag, tag_list)
            return jsonify({'code': 1, 'msg': 'success', 'data': tag_list})
        return jsonify({'code': -1, 'msg': 'unknown tag'})
    return jsonify({'code': 0, 'msg': 'permission denied'})


def get_father_tag(tag, tag_list):
    """
    获取某个tag的上级tag
    :return:
    """
    db = Database()
    if tag['father']:
        father = db.get({'ID': tag['father']}, 'tag')
        if father:
            tag_list.insert(0, father['ID'])
            get_father_tag(father, tag_list)


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
        if father == '':
            flag = db.insert({'name': name}, 'tag')
            if flag:
                return jsonify({'code': 1, 'msg': 'success'})
            return jsonify({'code': -1, 'msg': 'unknown error'})
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
        flag = db.update({'ID': tag_id}, {'name': name, 'father': father}, 'tag')
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


@app.route('/api/face/get_token', methods=['POST'])
def get_face_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=GNvUXmnO4rXK54k3Kz6YMFfe&client_secret=GrYreYLF4YhHvUCh8duwFLQGadHVtl3O'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if (content):
        # 更新access_token
        ACCESS_TOKEN = content['access_token']
        return jsonify({'code': 1, 'msg': 'success', 'data': content})
    return jsonify({'code': 0, 'msg': 'fail'})


@app.route('/api/face/face_check', methods=['POST'])
def face_check():
    username = request.form['username']
    way = request.form['way']
    if way == "用户名":
        way = 'username'
    elif way == "学号":
        way = 'Snum'
    # 传入图片的base64编码，不包含图片头，如data:image/jpg;base64
    img1 = ""
    img2 = request.form['face']
    # 获取用户的人脸照片，转换为base64编码
    db = Database()
    user = db.get({way: username}, 'user')
    if user:
        with open(FILE_PATH + "/face/" + user['face'], 'rb') as f:
            base64_data = base64.b64encode(f.read())
            img1 = base64_data.decode()

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    params = json.dumps(
        [{"image": img1, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
         {"image": img2, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"}])
    params = bytes(params, encoding="utf8")
    request_url = request_url + "?access_token=" + ACCESS_TOKEN
    rq = urllib.request.Request(url=request_url, data=params)
    rq.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(rq)
    content = response.read()
    if content:
        content = str(content, encoding="utf8")
        content = json.loads(content)
        errcode = content['error_code']
        if errcode == 100 or errcode == 110 or errcode == 111:
            return jsonify({'code': 0, 'msg': 'access token was invalid'})
        elif errcode == 18:
            return jsonify({'code': -1, 'msg': 'QPS limit'})
        elif errcode == 0:
            similarity = content['result']['score']
            return jsonify({'code': 1, 'msg': 'success', 'data': similarity})

        return jsonify({'code': -3, 'msg': 'fail', 'data': content})
    return jsonify({'code': -2, 'msg': 'fail', 'data': content})


@app.route('/api/face/face_exist', methods=['POST'])
def face_exist():
    # 传入图片的base64编码，不包含图片头，如data:image/jpg;base64
    img = request.form['face']
    height = float(request.form['h'])
    width = float(request.form['w'])
    # 水平方向的边界空余空间
    margin_horizen = width * 0.1
    # 垂直方向的边界空余空间
    margin_vertical = height * 0.1
    # 获取用户的人脸照片，转换为base64编码
    db = Database()

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params = json.dumps({"image": img, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"})
    params = bytes(params, encoding="utf8")
    request_url = request_url + "?access_token=" + ACCESS_TOKEN
    rq = urllib.request.Request(url=request_url, data=params)
    rq.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(rq)
    content = response.read()
    if content:
        content = str(content, encoding="utf8")
        content = json.loads(content)
        errcode = content['error_code']
        if errcode == 0:
            face_num = content['result']['face_num']
            if face_num == 1:
                top = content['result']['face_list'][0]['location']['top']
                left = content['result']['face_list'][0]['location']['left']
                face_width = content['result']['face_list'][0]['location']['width']
                face_height = content['result']['face_list'][0]['location']['height']

                if face_width > width * 0.6 or face_height > height * 0.6:
                    return jsonify({'code': -4, 'msg': 'fail,face too big', 'data': content, 'num': face_num})

                if top > margin_vertical and left > margin_horizen and top + face_height < height - margin_vertical and left + face_width < width - margin_horizen:
                    return jsonify({'code': 1, 'msg': 'success', 'data': content, 'num': face_num})
                else:
                    return jsonify({'code': 0, 'msg': 'fail', 'data': content, 'num': face_num})
            else:
                return jsonify({'code': -1, 'msg': 'fail', 'data': content, 'num': face_num})

        return jsonify({'code': -2, 'msg': 'success', 'data': errcode})

    return jsonify({'code': -3, 'msg': 'fail', 'data': content})


# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/api/upload/upload_picture', methods=['POST'])
def upload_picture():
    """
    上传图片
    :return: code(0=失败，1=成功)
    """
    f = request.files['picture']
    if f and allowed_file(f.filename):
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        new_filename = str(int(time.time())) + secure_filename(f.filename)
        upload_path = os.path.join(basepath, 'static/uploads', new_filename)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return jsonify({'code': 1, 'msg': 'success', 'data': HOST_NAME + '/static/uploads/' + new_filename})
    return jsonify({'code': 0, 'msg': 'unexpected type'})


"""
    评论功能
"""


@app.route('/api/comment/add_comment', methods=['POST'])
def add_comment():
    """
    添加评论
    :return:
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token}, 'user')
    if user:
        article_id = request.form['article_id']
        content = request.form['content']
        father = request.form['father']
        flag = db.insert({'content': content, 'article_id': article_id, 'user_id': user['ID'], 'father': father},
                         'comment')
        if flag:
            return jsonify({'code': 1, 'msg': 'success'})
        return jsonify({'code': -1, 'msg': 'unknown error'})
    return jsonify({'code': 0, 'msg': 'permission denied'})


@app.route('/api/comment/get_comment')
def get_comment():
    """
    获取评论
    :return:
    """
    token = request.values.get('token')
    db = Database()
    user = db.get({'token': token}, 'user')
    if user:
        article_id = request.values.get('article_id')
        comments = db.get({'father': db.MYSQL_NULL, 'article_id': article_id}, 'comment', 0) + db.get(
            {'father': '', 'article_id': article_id}, 'comment_info', 0)
        for item in comments:
            children = db.get({'father': item['ID']}, 'comment_info', 0)
            for child in children:
                child.update({'time': child['time'].strftime("%Y-%m-%d")})
            item.update({'children': children, 'time': item['time'].strftime("%Y-%m-%d")})
        return jsonify({'code': 1, 'msg': 'success', 'data': comments})
    return jsonify({'code': 0, 'msg': 'permission denied'})


if __name__ == '__main__':
    # 开启调试模式，修改代码后不需要重新启动服务即可生效
    # 请勿在生产环境下使用调试模式
    # Flask服务将默认运行在localhost的5000端口上

    # with open('static\\upload\\36.txt', 'rb') as file:
    #     result = pred(file.read())
    #     print(result[0])
    app.run(host='127.0.0.1', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=5000, debug=False)
