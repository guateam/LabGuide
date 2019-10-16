import numpy

from new_api.util.def_methods import get_euclidean_distance
from new_api.util.util import PASS_DIST


def check_face_vector(vec1, vec2):
    """
    检查两个面部向量是否足够相近
    :param vec1:
    :param vec2:
    :return:
    """
    vec1 = numpy.array(vec1)
    vec2 = numpy.array(vec2)
    dist = get_euclidean_distance(vec1, vec2)
    if dist < PASS_DIST:
        return True
    return False
