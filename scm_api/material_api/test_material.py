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
    create_cases = Api.read_yaml(yaml.create_material_path)

    update_cases = Api.read_yaml(yaml.create_material_path)

    @pytest.mark.parametrize("case", create_cases)
    def test_create_material(self, get_token, case, get_data):
        """新增物料通用数据"""

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

        # logger.info(category_id, signal_id, unit_id, code, name)   # 查看判断后的日志

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

    @pytest.mark.parametrize("up_case", update_cases)
    def test_update_material(self, get_token, up_case, get_data):

        res = requests.post(url=self.url + 'updateScmMaterial',
                            headers={"Authorization": f"bearer {get_token}"},
                            json={
                              "operationName": "updateScmMaterial",
                              "variables": {
                                "input": {
                                  "category": {
                                    "id": "894b1ca8-fe1a-4483-b4c7-229f21b6422e"
                                  },
                                  "figureNo": "2323",
                                  "id": "3e5eab1f-7b8d-41f6-a3ce-56020c733a77",
                                  "inventoryUnit": {
                                    "id": "4f328956-fe20-4a87-8129-e011542de156"
                                  },
                                  "materialQuality": "123",
                                  "materialSignal": {
                                    "id": "78b506b5-81c1-4523-9469-79436543a481"
                                  },
                                  "materialType": "PURCHASE",
                                  "model": "23",
                                  "name": "213",
                                  "specification": "33"
                                }
                              },
                              "query": "mutation updateScmMaterial($input: UpdateScmMaterialInput!)"
                                       " {\n  updateScmMaterial(input: $input)\n}"
                            })

        resp = res.json()
