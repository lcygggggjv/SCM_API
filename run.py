import pytest
from config.file_path import FilePath
import configparser
import os


# 运行所有
pytest.main()

# 指定模块, -s 输出调试信息，包括打印信息 ， -v 显示更详细信息，可以放在一起 -vs
# pytest.main(['-s', '-v', FilePath.create_material_api_path])

# os.path.dirname 获取当前文件的所在目录，前面所有级目录
# root_path = os.path.dirname(os.path.abspath(__file__))
#
# ini_path = os.path.join(root_path, 'config', 'env.ini')
#
# config_parser = configparser.ConfigParser()
#
# config_parser.read(ini_path, encoding='utf-8')

