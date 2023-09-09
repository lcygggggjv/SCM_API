import schedule
import time
from config.file_path import FilePath


def delete_log_contents():
    """定时删除日志文件"""

    with open(FilePath.log_path, 'w') as f:
        f.write('')


"""设置定时任务, 每月第一天10点执行， do是需要函数做为参数，不是调用函数的结果"""
schedule.every().day.at('10:00').do(delete_log_contents)

while True:
    schedule.run_pending()
    time.sleep(1)
