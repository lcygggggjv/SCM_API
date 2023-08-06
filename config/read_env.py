
import configparser
import os.path

# dirname当前文件父级目录，__file__当前文件路径， abspath转换绝对路径， 最终获取当前文件父级的目录绝对路径
base_dir = os.path.dirname(os.path.abspath(__file__))

# 获取ini文件路径
env_dir = os.path.join(base_dir, 'env.ini')

config_path = configparser.ConfigParser()

config_path.read(env_dir, encoding='utf-8')

pick = config_path.get("pick", 'env')  # 获取配置项[pick] env键，就是test4  传给pick变量

env = config_path.get(pick, 'env')  # 再[test4]里，获取对应的信息，如环境，账号，密码
tenant_code = config_path.get(pick, 'tenant_code')
account = config_path.get(pick, 'account')
password = config_path.get(pick, 'password')


class EnvironMent:
    """env, account全局变量，类里可直使用"""

    @staticmethod
    def get_env_url():

        return "https://" + env + ".tele" + "tr" + "aan.io" + "/gra" + "phql/?"

    @staticmethod
    def account():

        return account

    @staticmethod
    def password():

        return password

    @staticmethod
    def tenant_code():

        return tenant_code


if __name__ == '__main__':

    c = EnvironMent()

    ss = c.get_env_url()

    d = c.account()
    print(ss)
