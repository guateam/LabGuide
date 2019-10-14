import os

from flask import Flask
from flask_cors import CORS

from new_api.api.article import article
from new_api.api.comment import comment
from new_api.api.tag import tag
from new_api.api.upload import upload
from new_api.api.util import util
from new_api.api.user import user
from new_api.util.main_init_methods import init_dir
from new_api.util.right_methods import init_rights
from new_api.util.util import HOST, PORT, DEBUG

init_rights(debug=DEBUG)
init_dir(debug=DEBUG)

app = Flask(__name__)
# 注册相关蓝图
app.register_blueprint(blueprint=user, url_prefix='/user')
app.register_blueprint(blueprint=article, url_prefix='/article')
app.register_blueprint(blueprint=util, url_prefix='/')
app.register_blueprint(blueprint=upload, url_prefix='/upload')
app.register_blueprint(blueprint=comment, url_prefix='/comment')
app.register_blueprint(blueprint=tag, url_prefix='/tag')

CORS(app, supports_credentials=True)

if __name__ == '__main__':
    # 开启调试模式，修改代码后不需要重新启动服务即可生效
    # 请勿在生产环境下使用调试模式
    # Flask服务将默认运行在localhost的5000端口上
    app.run(host=HOST, port=PORT, debug=DEBUG)
