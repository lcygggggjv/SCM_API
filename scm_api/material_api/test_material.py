import pytest
import requests
from common.mock import Mock
from config.read_env import EnvironMent
from scm_api.base_api import Api
from config.file_path import FilePath
import allure


class TestMaterial(Api):
    """物料通用数据测试"""

    env = EnvironMent()
    url = env.get_env_url()

    mock = Mock()

    """读取yaml文件测试数据"""
    yaml = FilePath()
    # 新增物料用例
    create_cases = Api.read_yaml(yaml.create_material_path)
    # 编辑物料用例
    update_cases = Api.read_yaml(yaml.update_material_path)
    # 删除物料用例
    delete_cases = Api.read_yaml(yaml.delete_material_path)

    @allure.title('新增物料全部用例')
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

    @allure.title('编辑物料全部用例')
    @pytest.mark.parametrize("up_case", update_cases)
    def test_update_material(self, get_token, up_case, get_data):

        cate_id2, unit_id2, signal_id2 = None, None, None

        if up_case['data']['category_id'] == 'category_id':
            cate_id2 = get_data[0]
        if up_case['data']['unit_id'] == 'unit_id':
            unit_id2 = get_data[1]
        if up_case['data']['signal_id'] == 'signal_id':
            signal_id2 = get_data[2]

        if up_case["data"]["name"] == "name":
            name = self.mock.ran_py_str()
        else:
            name = up_case["data"]["name"]

        res = requests.post(url=self.url + 'updateScmMaterial',
                            headers={"Authorization": f"bearer {get_token}"},
                            json={
                              "operationName": "updateScmMaterial",
                              "variables": {
                                "input": {
                                  "category": {
                                    "id": cate_id2
                                  },
                                  "figureNo": self.mock.ran_py_str(),
                                  "id": Api.get_create_material_id(),
                                  "inventoryUnit": {
                                    "id": unit_id2
                                  },
                                  "materialQuality": "123",
                                  "materialSignal": {
                                    "id": signal_id2
                                  },
                                  "materialType": up_case["data"]["material_type"],
                                  "model": self.mock.ran_py_str(),
                                  "name": name,
                                  "specification": self.mock.ran_py_str()
                                }
                              },
                              "query": "mutation updateScmMaterial($input: UpdateScmMaterialInput!)"
                                       " {\n  updateScmMaterial(input: $input)\n}"
                            })

        resp = res.json()

        expected = up_case['expected']

        actual = self.review_actual(resp)
        self.assert_actual(expected, actual)

    @allure.title('删除物料全部用例')
    @pytest.mark.parametrize("delete_case", delete_cases)
    def test_delete_material(self, get_token, delete_case):
        # 设置默认值
        create_id = None

        if delete_case["data"]["id"] == "id":
            create_id = Api.get_create_material_id()

        res = requests.post(url=self.url + 'deleteScmMaterial',
                            headers={"Authorization": f"bearer {get_token}"},
                            json={
                              "operationName": "deleteScmMaterial",
                              "variables": {
                                "ids": [
                                  create_id
                                ]
                              },
                              "query": "mutation deleteScmMaterial($ids: [String!]!) "
                                       "{\n  deleteScmMaterial(ids: $ids) {\n    isUsed\n    __typename\n  }\n}"
                            })
        resp = res.json()

        actual = self.review_actual(resp)
        expected = delete_case["expected"]
        self.assert_actual(expected, actual)
