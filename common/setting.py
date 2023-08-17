from pymysql.cursors import DictCursor
import psycopg2
from config.file_path import FilePath
from loguru import logger
import pymysql


"""sink文件路径，level日志等级"""
# logger.add(sink=FilePath.log_path, encoding='utf-8', level='INFO')

import logging
import colorlog

# 创建一个logger对象
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# 创建一个StreamHandler来输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 创建并设置颜色输出格式
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'white',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
console_handler.setFormatter(formatter)

# 将StreamHandler添加到logger中
logger.addHandler(console_handler)

# 示例断言
assert 1 == 2, "断言失败"

# 记录断言失败的日志
logger.error("断言失败")



class ConnectMysql:
    """DictCursor是用于设置pymysql游标的类，它指定了返回结果的格式为字典类型。
    使用DictCursor可以将查询结果以字典的形式返回，其中列名作为键，对应的值作为值。
    cursorclass参数只能在连接MySQL数据库时使用，对于其他数据库如PostgreSQL并没有类似的参数。"""

    def __init__(self, host=None, user=None, password=None, port=None, db=None, **kwargs):

        self.conn = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    port=port,
                                    cursorclass=DictCursor,  # 将返回结果以字典形式返回
                                    db=db)

    def query_all(self, sql):
        """首先实例属性conn连接数据库，获取游标对象,
        使用execute方法传入sql，再使用cursor，fetchall获取全部数据，并关闭游标，关闭连接数据库
        """

        cursor = self.conn.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return result

    def query_one(self, sql):

        cursor = self.conn.cursor()
        cursor.execute(sql)

        result = cursor.fetchone()
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return result


class ConnectPostgres:

    def __init__(self, host=None, user=None, password=None, port=None, database=None, **kwargs):

        self.conn = psycopg2.connect(
                                     user=user,
                                     password=password,
                                     host=host,
                                     port=port,
                                     database=database)

    def query_all(self, sql):
        """首先实例属性conn连接数据库对象，获取游标对象，,
        使用execute方法传入sql，再使用cursor.fetchall获取全部数据，commit提交事务，并关闭游标,关闭连接数据库
        """
        cursor = self.conn.cursor()

        cursor.execute(sql)
        result = cursor.fetchall()
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return result

    def query_one(self, sql):

        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return result


# if __name__ == '__main__':
#
#     con = ConnectMysql(**FilePath.db)
#     res = con.query_one('select user_id, mobile_code from tz_sms_log limit 5')
#
#     # conn = ConnectPostgres(db='test2_eam.public', user='postgres', password='postgres',
#     # port=30001,host='192.168.1.128')
#
#     # conn = ConnectPostgres(**FilePath.tc_db)
#     # res = conn.query_one("select id, name from thing where code='931929'")
#
#     print(res)
