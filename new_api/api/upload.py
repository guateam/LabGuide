import os
import time

from flasgger import swag_from
from flask import Blueprint, request
from werkzeug.utils import secure_filename

from new_api.util.def_methods import reply_json, allowed_file
from new_api.util.main_init_methods import upload_dir
from new_api.util.util import HOST_NAME
from PIL import Image

upload = Blueprint('upload', __name__)


@upload.route('/upload_picture', methods=['POST'])
@swag_from('docs/upload/upload_picture.yml')
def upload_picture():
    """
    上传图片
    :return:
    """
    f = request.files['picture']
    if f and allowed_file(f.filename):
        img = Image.open(f)
        new_filename = str(int(time.time())) + secure_filename(f.filename.rsplit('.', 1)[0]) + '.webp'
        upload_path = os.path.join(upload_dir, new_filename)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        # f.save(upload_path)
        img.save(upload_path)
        return reply_json(1, HOST_NAME + '/static/uploads/' + new_filename)
    return reply_json(-4)
