from flasgger import Swagger
from flask import Flask
from flask_cors import CORS

from new_api.api.article import article
from new_api.api.comment import comment
from new_api.api.guide_line import guide_line
from new_api.api.notice import notice
from new_api.api.right import right
from new_api.api.tag import tag
from new_api.api.upload import upload
from new_api.api.user import user
from new_api.api.util import util
from new_api.util.main_init_methods import init_dir
from new_api.util.util import HOST, PORT, DEBUG, SWAGGER_TITLE, SWAGGER_DESC, SWAGGER_HOST, SWAGGER_WEBSITE, \
    VERSION

init_dir(debug=DEBUG)

app = Flask(__name__)

# 注册相关蓝图
app.register_blueprint(blueprint=user, url_prefix='/user')
app.register_blueprint(blueprint=article, url_prefix='/article')
app.register_blueprint(blueprint=util, url_prefix='/')
app.register_blueprint(blueprint=upload, url_prefix='/upload')
app.register_blueprint(blueprint=comment, url_prefix='/comment')
app.register_blueprint(blueprint=tag, url_prefix='/tag')
app.register_blueprint(blueprint=right, url_prefix='/right')
app.register_blueprint(blueprint=notice, url_prefix='/notice')
app.register_blueprint(blueprint=guide_line, url_prefix='/guide_line')
swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['title'] = SWAGGER_TITLE  # 配置大标题
swagger_config['description'] = SWAGGER_DESC  # 配置公共描述内容
swagger_config['host'] = SWAGGER_HOST  # 请求域名
swagger_config['termsOfService'] = SWAGGER_WEBSITE
swagger_config['version'] = VERSION
Swagger(app, config=swagger_config)
CORS(app, supports_credentials=True)

if __name__ == '__main__':
    # 开启调试模式，修改代码后不需要重新启动服务即可生效
    # 请勿在生产环境下使用调试模式
    # Flask服务将默认运行在localhost的5000端口上
    app.run(host=HOST, port=PORT, debug=DEBUG)
