import importlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from new_api.db.config import USER_NAME, PASSWORD, HOST_ADDRESS, PORT, DATABASE, CHARSET

engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=%s' % (
    USER_NAME, PASSWORD, HOST_ADDRESS, PORT, DATABASE, CHARSET))
Base = declarative_base()

Session = sessionmaker(bind=engine)


def get_model(name):
    """
    导入model
    :param name:model名
    :return: model
    """
    return importlib.import_module('new_api.db.Model.' + name).Model


def add(table, options):
    """
    添加数据库
    :param table:表名
    :param options:参数
    :return:
    """
    session = Session()
    try:
        model = get_model(table)(**options)
        session.add(model)
        session.commit()
        model = session.merge(model)
        session.refresh(model)
        session.close()
        return model
    except Exception as e:
        print(e.args)
        session.rollback()
        session.close()
        return None


def update(table, where, value):
    """
    修改数据库
    :param table: 表名
    :param value: 更新的值
    :param where: 查找的值
    :return:
    """
    session = Session()
    try:
        model = get_model(table)
        session.query(model).filter(*where).update(value)
        session.commit()
        data = session.query(model).filter(*where).first()
        session.close()
        return data
    except Exception as e:
        print(e.args)
        session.rollback()
        session.close()
        return None


def delete(table, where):
    """
    清除数据库
    :param table: 表名
    :param where: 查找的值
    :return:
    """
    session = Session()
    try:
        model = get_model(table)
        session.query(model).filter(*where).delete()
        session.commit()
        session.close()
        return True
    except Exception as e:
        print(e.args)
        session.rollback()
        session.close()
        return False


def get(table, where, first=False):
    """
    查找数据库
    :param table: 表名
    :param where: 查找的值
    :param first: 是否只获取第一个
    :return:
    """
    session = Session()
    try:
        model = get_model(table)
        data = session.query(model).filter(*where).all() if not first else session.query(model).filter(*where).first()
        session.close()
        return data
    except Exception as e:
        print(e.args)
        session.rollback()
        session.close()
        return None


if __name__ == '__main__':
    username = 'hanerx'
    res = get('User', [get_model('User').username == username], first=True)
    print(res)
