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
