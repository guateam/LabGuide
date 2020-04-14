from flasgger import swag_from
from flask import Blueprint

from new_api.rights_control.rights_control import right_required
from new_api.util.def_methods import login_required

guide_line = Blueprint('guide_line', __name__)


@guide_line.route('/add_guide_line', methods=['POST'])
@login_required
@right_required([])
@swag_from('docs/guide_line/add_guide_line.yml')
def add_guide_line():
    """
    添加导航
    :return:
    """


@guide_line.route('/change_guide_line', methods=['POST'])
@login_required
@right_required([])
@swag_from('docs/guide_line/change_guide_line.yml')
def change_guide_line():
    """
    修改导航
    :return:
    """


@guide_line.route('/delete_guide_line', methods=['POST'])
@login_required
@right_required([])
@swag_from('docs/guide_line/delete_guide_line.yml')
def delete_guide_line():
    """
    清除导航
    :return:
    """


@guide_line.route('/add_node', methods=['POST'])
@login_required
@right_required([])
@swag_from('docs/guide_line/add_node.yml')
def add_node():
    """
    为导航添加节点
    :return:
    """


@guide_line.route('/change_node', methods=['POST'])
@login_required
@right_required([])
@swag_from('docs/guide_line/change_node.yml')
def change_node():
    """
    修改特定节点
    :return:
    """


@guide_line.route('/delete_node', methods=['POST'])
@login_required
@right_required([])
@swag_from('docs/guide_line/delete_node.yml')
def delete_node():
    """
    清除特定节点
    :return:
    """


@guide_line.route('/get_nodes')
@login_required
@right_required([])
@swag_from('docs/guide_line/get_nodes.yml')
def get_nodes():
    """
    获取特定导航的所有节点
    :return:
    """
