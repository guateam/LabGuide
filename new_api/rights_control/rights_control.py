import functools

from werkzeug.utils import redirect

from new_api.rights_control.models.Base import Base


def check_rights(rights_class: Base) -> bool:
    return rights_class.check()


def right_required(rights_class: Base):
    def right_decorator(func):
        @functools.wraps(func)  # 修饰内层函数，防止当前装饰器去修改被装饰函数__name__的属性
        def inner(*args, **kwargs):
            return redirect('/right_check_fail') if not check_rights(rights_class) else func(*args, **kwargs)

        return inner

    return right_decorator
