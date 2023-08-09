import random
import string

from faker import Faker


class Mock:

    @staticmethod
    def rand_str(strs='sc'):
        """random,string方法获取随机字符串"""

        ran_str = string.digits + string.ascii_letters

        all_str = ''.join(random.sample(ran_str, 3))

        return all_str + strs

    @staticmethod
    def ran_py_str():
        """Faker随机获取字符串"""

        faker = Faker()

        strs = faker.pystr(max_chars=5)

        return strs

    @staticmethod
    def ran_phone():
        """156开头的手机号"""

        head_num = '156'
        # 生成后8位随机数字 choice取序列随机一个元素返回,
        # ‘_’ 是一个常用习惯用法，在循环中表示一个临时变量，通常用于表示在循环中不需要使用到的值。
        suffix = ''.join(random.choice('0123456789') for _ in range(8))
        # 拼接前缀和后缀
        return head_num + suffix


if __name__ == '__main__':

    mock = Mock()
    ud = mock.ran_py_str()
    print(ud)
