from flask import Blueprint

server = Blueprint('server', __name__)


@server.route('/get_server_status')
def get_server_status():
    """
    获取服务器状态
    :return:
    """
