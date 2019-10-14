import os
import time

from flask import Blueprint, request
from werkzeug.utils import secure_filename

from new_api.util.def_methods import reply_json, allowed_file
from new_api.util.main_init_methods import upload_dir
from new_api.util.util import HOST_NAME

upload = Blueprint('upload', __name__)


@upload.route('/upload_picture', methods=['POST'])
def upload_picture():
    """
    上传图片
    :return:
    """
    f = request.files['picture']
    if f and allowed_file(f.filename):
        new_filename = str(int(time.time())) + secure_filename(f.filename)
        upload_path = os.path.join(upload_dir, new_filename)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return reply_json(1, HOST_NAME + '/static/uploads/' + new_filename)
    return reply_json(-4)
