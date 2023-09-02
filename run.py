import pytest
import os


if __name__ == '__main__':

    # 指定模块, -vs 输出调试信息，包括打印详细信息， --alluredir 输出json文件报告  后面输出目录
    pytest.main(['-vs', '--alluredir', './report/temp'])
    # 产生报告，将报告保存，./report/temp获取这个目录中的json文件进行渲染，-o report/rep  生成的html文件，保存到这个目录中 clean清除
    os.system('allure generate ./report/temp  -0  ./report/temp --clean ')

