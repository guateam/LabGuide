class Base:
    def __init__(self):
        """
        所有权限类的基类，用于抽象化权限
        """
        pass

    def check(self) -> bool:
        """
        检查实例是否符合
        :return: 权限检查是否通过
        """
        pass
