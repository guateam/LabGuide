import importlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from new_api.db.config import USER_NAME, PASSWORD, HOST_ADDRESS, PORT, DATABASE, CHARSET

engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=%s' % (
    USER_NAME, PASSWORD, HOST_ADDRESS, PORT, DATABASE, CHARSET))
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


def get_model(name):
    """
    导入model
    :param name:model名
    :return: model
    """
    return importlib.import_module('new_api.db.Model.' + name).Model


def add(table, **options):
    """
    添加数据库
    :param table:表名
    :param options:参数
    :return:
    """
    try:
        model = get_model(table)(**options)
        session.add(model)
        session.commit()
        return model
    except Exception as e:
        return None


def update(table, where, value):
    """
    修改数据库
    :param table: 表名
    :param value: 更新的值
    :param where: 查找的值
    :return:
    """
    try:
        model = get_model(table)
        session.query(model).filter(*where).update(value)
        session.commit()
        return session.query(model).filter(*where).first()
    except Exception as e:
        return None


def delete(table, where):
    """
    清除数据库
    :param table: 表名
    :param where: 查找的值
    :return:
    """
    try:
        model = get_model(table)
        session.query(model).filter(*where).delete()
        session.commit()
        return True
    except Exception as e:
        return False


def get(table, where, first=False):
    """
    查找数据库
    :param table: 表名
    :param where: 查找的值
    :param first: 是否只获取第一个
    :return:
    """
    try:
        model = get_model(table)
        return session.query(model).filter(*where).all() if not first else session.query(model).filter(*where).first()
    except Exception as e:
        return None


if __name__ == '__main__':
    username = 'hanerx'
    res = get('User', [get_model('User').username == username], first=True)
    print(res)
