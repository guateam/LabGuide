import functools

from werkzeug.utils import redirect

from new_api.rights_control.models.Base import Base


def check_rights(rights_class: Base) -> bool:
    return rights_class.check()


def right_required(rights_classes: list):
    """
    权限检测装饰器，只要有一个通过即为通过
    :param rights_classes:权限列表
    :return:
    """

    def right_decorator(func):
        @functools.wraps(func)  # 修饰内层函数，防止当前装饰器去修改被装饰函数__name__的属性
        def inner(*args, **kwargs):
            try:
                for rights_class in rights_classes:
                    if check_rights(rights_class()):
                        return func(*args, **kwargs)
                return redirect('/right_check_fail')
            except Base.RightInitFailException as e:
                return redirect('/right_check_fail')

        return inner

    return right_decorator
