
import yaml
import requests
from common.mock import Mock
from config.read_env import EnvironMent
from common.setting import logger


class Api:

    env = EnvironMent()
    mock = Mock()

    @classmethod
    def login_token(cls):
        """获取登录 token """
        res = requests.request('post',
                               url=cls.env.get_env_url() + "login",
                               json={
                                  "operationName": "login",
                                  "variables": {
                                    "input": {
                                      "account": cls.env.account(),
                                      "password": cls.env.password(),
                                      "tenantCode": cls.env.tenant_code()
                                    }
                                  },
                                  "query": "mutation login($input: LoginInput!) {\n  login(input: $input) "
                                           "{\n    token\n    userId\n    __typename\n  }\n}"
                                 })

        result = res.json()
        login_token = result['data']['login']['token']
        return login_token

    @staticmethod
    def review_actual(actual):
        """判断获取的实际结果"""

        if "data" in actual and actual["data"]:
            # 使用get（）和data"in 更准确
            actual = actual["data"]
        elif "errors" in actual and actual["errors"]:
            # actual = actual["errors"][0]["message"]
            actual = actual["errors"][0]["extensions"]["code"]
        else:
            actual = actual["error"]["errors"][0]["message"]

        return actual

    @staticmethod
    def assert_actual(expected, actual):

        try:
            assert expected in actual

            logger.info(f"断言成功：预期结果：{expected}, 符合实际结果：{actual}")
        except AssertionError:
            error_msg = f"断言失败：预期结果：{expected}, 不符合实际结果：{actual}"
            logger.error(error_msg)
            raise AssertionError(error_msg)

    @classmethod
    def read_yaml(cls, yaml_path):
        """读取yaml测试用例"""

        with open(file=yaml_path, encoding='utf-8') as f:
            # 多个用例用safe_load_all，转换成list，否则返回的是对象
            cases = list(yaml.safe_load_all(f))

            return cases

    @classmethod
    def get_unit(cls):
        """获取物料单位 id """

        res = requests.post(url=cls.env.get_env_url() + 'scmUnitList',
                            headers={"Authorization": f"bearer {cls.login_token()}"},
                            json={
                                  "operationName": "scmUnitList",
                                  "variables": {
                                    "filter": {},
                                    "limit": 50,
                                    "offset": 0
                                  },
                                  "query": "query scmUnitList($filter: ScmUnitFilter, $limit: Int, $offset: Int, "
                                           "$orderBy: [String!]) {\n  scmUnitList(filter: $filter, limit: $limit, "
                                           "offset: $offset, orderBy: $orderBy) {\n    data {\n      id\n      "
                                           "name\n      remark\n      abbreviation\n      __typename\n    }\n    "
                                           "totalCount\n    __typename\n  }\n}"
                                })

        actual = res.json()

        return actual['data']['scmUnitList']['data'][0]['id']

    @classmethod
    def get_signal(cls):
        """获取信号 id """

        res = requests.post(url=cls.env.get_env_url() + "scmMaterialSignalList",
                            headers={"Authorization": f"bearer {cls.login_token()}"},
                            json={
                                  "operationName": "scmMaterialSignalList",
                                  "variables": {
                                    "filter": {},
                                    "limit": 50,
                                    "offset": 0
                                  },
                                  "query": "query scmMaterialSignalList($filter: ScmMaterialSignalFilter, "
                                           "$limit: Int, $offset: Int, $orderBy: [String!]) {\n  "
                                           "scmMaterialSignalList(\n    filter: $filter\n    limit: "
                                           "$limit\n    offset: $offset\n    orderBy: $orderBy\n  ) "
                                           "{\n    data {\n      id\n      no\n      name\n      "
                                           "srmUsageStatus\n      wmsUsageStatus\n      __typename\n    "
                                           "}\n    totalCount\n    __typename\n  }\n}"
                                })

        actual = res.json()

        return actual['data']['scmMaterialSignalList']['data'][0]['id']

    @classmethod
    def get_category(cls):
        """获取物料分类 id """

        res = requests.post(url=cls.env.get_env_url() + "scmMaterialCategoryList",
                            headers={"Authorization": f"bearer {cls.login_token()}"},
                            json={
                                  "operationName": "scmMaterialCategoryList",
                                  "variables": {
                                    "filter": {}
                                  },
                                  "query": "query scmMaterialCategoryList($filter: ScmMaterialCategoryFilter) "
                                           "{\n  scmMaterialCategoryList(filter: $filter) {\n    id\n    name\n    "
                                           "no\n    parentId\n    path {\n      id\n      name\n      "
                                           "__typename\n    }\n    __typename\n  }\n}"
                                })

        actual = res.json()

        return actual['data']['scmMaterialCategoryList'][0]['id']

    @classmethod
    def get_create_material_id(cls):

        res = requests.post(url=cls.env.get_env_url() + 'createScmMaterial',
                            headers={"Authorization": f"bearer {cls.login_token()}"},
                            json={
                                "operationName": "createScmMaterial",
                                "variables": {
                                    "input": {
                                        "category": {
                                            "id": "680ba59a-202c-4ff4-b8a5-d71af0f4e40a"
                                        },
                                        "figureNo": cls.mock.ran_py_str(),
                                        "inventoryUnit": {
                                            "id": "dc083f4b-7ebe-43ee-b837-aa8342f13d38"
                                        },
                                        "materialQuality": cls.mock.ran_py_str(),
                                        "materialSignal": {
                                            "id": "5f17aaf6-4973-437d-9f8a-f75902cbe2a2"
                                        },
                                        "materialType": "PURCHASE",
                                        "model": cls.mock.ran_py_str(),
                                        "name": cls.mock.ran_py_str(),
                                        "no": cls.mock.ran_py_str(),
                                        "specification": cls.mock.ran_py_str()
                                    }
                                },
                                "query": "mutation createScmMaterial($input: CreateScmMaterialInput!) "
                                         "{\n  createScmMaterial(input: $input)\n}"
                            })

        actual = res.json()
        return actual["data"]["createScmMaterial"]


if __name__ == '__main__':

    ao = Api()
    ox = ao.get_create_material_id()

    print(ox)
