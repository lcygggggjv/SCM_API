import pytest
import requests
from common.mock import Mock
from config.read_env import EnvironMent
from scm_api.base_api import Api
from config.file_path import FilePath
from common.setting import logger


class TestMaterial(Api):
    """物料通用数据测试"""

    env = EnvironMent()
    url = env.get_env_url()

    mock = Mock()

    """读取yaml文件测试数据"""
    yaml = FilePath()
    cases = Api.read_yaml(yaml.material_path)

    @pytest.mark.parametrize("case", cases)
    def test_create_material(self, get_token, case, get_data):
        """新增物料通用数据"""
        # 定义为局部变量
        category_id, unit_id, signal_id = None, None, None

        if case['data']['category_id'] == 'category_id':
            category_id = get_data[0]
        if case['data']['unit_id'] == 'unit_id':
            unit_id = get_data[1]
        if case['data']['signal_id'] == 'signal_id':
            signal_id = get_data[2]

        if case["data"]["code"] == 'code':
            code = self.mock.ran_py_str()
        else:
            code = case["data"]["code"]

        if case["data"]["name"] == "name":
            name = self.mock.ran_py_str()
        else:
            name = case["data"]["name"]

        logger.info(category_id, signal_id, unit_id, code, name)   # 查看判断后的日志

        res = requests.post(url=self.url + 'createScmMaterial',
                            headers={"Authorization": f"bearer {get_token}"},
                            json={
                              "operationName": "createScmMaterial",
                              "variables": {
                                "input": {
                                  "category": {
                                    "id": category_id
                                  },
                                  "figureNo": self.mock.ran_py_str(),
                                  "inventoryUnit": {
                                    "id": unit_id
                                  },
                                  "materialQuality": self.mock.ran_py_str(),
                                  "materialSignal": {
                                    "id": signal_id
                                  },
                                  "materialType": case["data"]["material_type"],
                                  "model": self.mock.ran_py_str(),
                                  "name": name,
                                  "no": code,
                                  "specification": self.mock.ran_py_str()
                                }
                              },
                              "query": "mutation createScmMaterial($input: CreateScmMaterialInput!) "
                                       "{\n  createScmMaterial(input: $input)\n}"
                            })

        res = res.json()
        expected = case['expected']

        actual = self.review_actual(res)
        self.assert_actual(expected, actual)
