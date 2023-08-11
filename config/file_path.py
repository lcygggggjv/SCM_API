import os.path
import pathlib

from pymysql.cursors import DictCursor


class FilePath:

    base_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = pathlib.Path(__file__).absolute().parent   # 当前文件目录的父级 就是config

    root_path = config_path.parent    # 根路径

    # 根据项目分层路径  根路径/log/test_log 其他类推
    log_path = root_path / 'log' / 'test_log'   # 日志文件路径

    material_path = root_path / 'test_case' / 'material_case' / 'material.yaml'

    postgres_db = dict(
                       user='postgres',
                       password='postgres',
                       host='192.168.1.128',
                       port=30001,
                       database='test2_eam')

    tc_db = dict(user='postgres',
                 password='postgres',
                 host='192.168.1.128',
                 port=30001,
                 db='test2_eam')

    db = dict(user='lemon',
              password='lemon123',
              host='47.113.180.81',
              port=3306,
              cursorclass=DictCursor,   # 导入dictCursor类  得到字典
              db='yami_shops')


if __name__ == '__main__':

    path = FilePath()
    print(path.log_path)
