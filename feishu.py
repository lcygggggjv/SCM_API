
import sys
import requests
import datetime

# 定义python系统变量
JOB_URL = sys.argv[1]
JOB_NAME = sys.argv[2]
BUILD_NUMBER = sys.argv[3]

# 获取当前系统时间
times = datetime.datetime.now()
current_time = times.strftime('%Y-%m-%d %H:%M:%S')

# 飞书机器人的webhook地址
url = 'https://open.feishu.cn/open-apis/bot/v2/hook/f56721a6-3fff-46ab-89a9-ed478f6d29bc'
method = 'post'
headers = {'Content-Type': 'application/json'}

data = {
    "msg_type": "interactive",
    "card": {
        "config": {
            "wide_screen_mode": True,
            "enable_forward": True
        },
        "elements": [{
            "tag": "div",
            "text": {
                "content": f"项目名称: {JOB_NAME}",  # 这是卡片的内容，也可以添加其他的内容：比如构建分支，构建编号等
                "tag": "lark_md"
            }
        }, {
            "tag": "div",
            "text": {
                "content": "测试进度: 测试完成",
                "tag": "lark_md"
            }
        },
            {
            "tag": "div",
            "text": {
                "content": f"构建次数: {BUILD_NUMBER}",
                "tag": "lark_md"
            }
        },
            {
            "tag": "div",
            "text": {
                "content": f"完成时间:{current_time}",
                "tag": "lark_md"
            }
        },
            {
            "actions": [{
                "tag": "button",
                "text": {
                    "content": "查看测试报告",  # 这是卡片的按钮，点击可以跳转到url指向的allure路径
                    "tag": "lark_md"
                },
                "url": f"{JOB_URL}allure/",  # JOB_URL 调用python定义的变量，该url是服务器下的allure路径
                "type": "default",
                "value": {}
            }],
            "tag": "action"
        }],
        "header": {
            "title": {
                "content": JOB_NAME + "构建报告",  # JOB_NAME 调用python定义的变量，这是卡片的标题
                "tag": "plain_text"
            }
        }
    }
}
res = requests.request(method=method, url=url, headers=headers, json=data)
print(res)
print(res.json())
