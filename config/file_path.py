import os.path
import pathlib


class FilePath:

    base_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = pathlib.Path(__file__).absolute().parent   # 当前文件目录的父级 就是config

    root_path = config_path.parent    # 根路径

    # 根据项目分层路径  根路径/log/test_log 其他类推
    log_path = root_path / 'log' / 'test_log'   # 日志文件路径

    material_path = root_path / 'test_case' / 'material_case' / 'material.yaml'


if __name__ == '__main__':

    path = FilePath()
    print(path.log_path)
