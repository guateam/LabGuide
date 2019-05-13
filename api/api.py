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
        return jsonify({'code': 1, 'msg': 'success', 'data': {'token': result['token'],'username':result['username'],'id':result['ID']}})
    return jsonify({'code': 0, 'msg': 'unexpected user'})  # 失败返回


@app.route('/api/account/check_account', methods=['POST'])
def check_account():
    """
    人脸检测之前的账号密码核对
    :return:
    """
    username = request.form['username']
    password = request.form['password']
    db = Database()
    user = db.get({'username': username, 'password': generate_password(password)}, 'user')
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

        data = db.get({'group':1},'user')
        if data:
            for it in data:
                it.pop("password")
                it.pop("token")
                it.pop("ID")
                it.pop("face")
                it.update({'group':"学生"})
        return jsonify({'code': 1, 'msg': 'success', 'data':data})

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


@app.route('/api/account/register', methods=['POST'])
def register():
    snum = request.form['snum']
    username = request.form['username']
    password = request.form['password']
    face = request.form['face']
    # base64转图片
    imgdata = base64.b64decode(face)
    filename = random_char() + ".bmp"
    file = open("../face/" + filename, 'wb')
    file.write(imgdata)
    file.close()
    db = Database()
    user = db.get({'Snum': snum}, 'user')
    if user:
        flag = db.update({'Snum': snum},
                         {'username': username, 'password': generate_password(password), 'face': filename, 'group': 1},
                         'user')
        return jsonify({'code': 1, 'msg': 'success'})
    return jsonify({'code': -1, 'msg': 'user not found'})


@app.route('/api/account/add_new_student', methods=['POST'])
def add_new_student():
    snum = request.form['snum']
    token = request.form['token']

    db = Database()
    admin = db.get({'token':token,'group':0},'user')
    if admin:
        exist = db.get({'Snum':snum, 'group':1}, 'user')
        if exist:
            return jsonify({"code": -2, 'msg':"user exist"})
        result = db.insert({'Snum':snum, 'group':1}, 'user')
        if result:
            return jsonify({"code": 1, 'msg':"success"})
        return jsonify({"code": 0, 'msg':"error"})
    return jsonify({"code": -1, 'msg':"permission denied"})

@app.route('/api/account/check_snum', methods=['POST'])
def check_snum():
    snum =  request.form['snum']
    db = Database()
    user = db.get({'Snum': snum}, 'user')
    if user:
        if user['username'] and user['password'] and user['face']:
            return jsonify({'code': -1, 'msg': 'already exist'})
        return jsonify({'code': 1, 'msg': 'success'})
    return jsonify({'code': 0, 'msg': 'user not found'})


@app.route('/api/account/get_basic_info', methods=['POST'])
def get_basic_info():
    token =  request.form['token']
    db = Database()
    user = db.get({'token': token}, 'user')
    if user:
        data = {
            'username':user['username'],
            'group':user['group'],
            'snum':user['Snum']
        }
        return jsonify({'code': 1, 'msg': 'success','data':data})
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
        for article in articles:
            article.update({'time':article['time'].strftime("%Y-%m-%d")})
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


@app.route('/api/face/get_token', methods=['POST'])
def get_face_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=GNvUXmnO4rXK54k3Kz6YMFfe&client_secret=GrYreYLF4YhHvUCh8duwFLQGadHVtl3O'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if (content):
        #更新access_token
        ACCESS_TOKEN = content['access_token']
        return jsonify({'code': 1, 'msg': 'success', 'data':content })
    return jsonify({'code':0, 'msg':'fail'})


@app.route('/api/face/face_check', methods=['POST'])
def face_check():
    username = request.form['username']
    #传入图片的base64编码，不包含图片头，如data:image/jpg;base64
    img1 = ""
    img2 = request.form['face']
    # 获取用户的人脸照片，转换为base64编码
    db = Database()
    user = db.get({'username': username, 'group': 0}, 'user')
    if user:
        with open("../face/"+user['face'], 'rb') as f:
            base64_data = base64.b64encode(f.read())
            img1 = base64_data.decode()

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    params = json.dumps(
        [{"image": img1, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
        {"image": img2, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"}])
    params = bytes(params,encoding="utf8")
    request_url = request_url + "?access_token=" + ACCESS_TOKEN
    rq = urllib.request.Request(url=request_url, data=params)
    rq.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(rq)
    content = response.read()
    if content:
        content = str(content,encoding="utf8")
        content = content.split(",")
        for idx in range(len(content)):
            content[idx] = content[idx].replace('"','')
        errcode = content[0].split(':')
        errcode = errcode[1]

        if errcode == '100' or errcode == '110'or errcode == '111':
            return jsonify({'code': 0, 'msg': 'access token was invalid'})
        elif errcode == 18 :
            return jsonify({'code': -1, 'msg': 'QPS limit'})

        similarity = content[5]
        similarity = similarity.split(':')
        similarity = similarity[2]
        similarity = float(similarity)
        return jsonify({'code': 1, 'msg': 'success', 'data':similarity })

    return jsonify({'code':0, 'msg':'fail'})


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


if __name__ == '__main__':
    # 开启调试模式，修改代码后不需要重新启动服务即可生效
    # 请勿在生产环境下使用调试模式
    # Flask服务将默认运行在localhost的5000端口上

    # with open('static\\upload\\36.txt', 'rb') as file:
    #     result = pred(file.read())
    #     print(result[0])
    app.run(host='0.0.0.0', port=5000, debug=False)
    # app.run(host='0.0.0.0', port=5000, debug=False)
