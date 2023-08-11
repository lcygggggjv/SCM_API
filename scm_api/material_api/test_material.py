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

        if case['data']['category_id'] == 'category_id':
            case['data']['category_id'] = get_data[0]
        if case['data']['unit_id'] == 'unit_id':
            case['data']['unit_id'] = get_data[1]
        if case['data']['signal_id'] == 'signal_id':
            case['data']['signal_id'] = get_data[2]

        res = requests.post(url=self.url + 'createScmMaterial',
                            headers={"Authorization": f"bearer {get_token}"},
                            json={
                              "operationName": "createScmMaterial",
                              "variables": {
                                "input": {
                                  "category": {
                                    "id": case['data']['category_id']
                                  },
                                  "figureNo": self.mock.ran_py_str(),
                                  "inventoryUnit": {
                                    "id": case['data']['unit_id']
                                  },
                                  "materialQuality": self.mock.ran_py_str(),
                                  "materialSignal": {
                                    "id": case['data']['signal_id']
                                  },
                                  "materialType": "PURCHASE",
                                  "model": self.mock.ran_py_str(),
                                  "name": self.mock.ran_py_str(),
                                  "no": self.mock.ran_py_str(),
                                  "specification": self.mock.ran_py_str()
                                }
                              },
                              "query": "mutation createScmMaterial($input: CreateScmMaterialInput!) "
                                       "{\n  createScmMaterial(input: $input)\n}"
                            })

        actual = res.json()
        expected = case['expected']

        if expected in actual:
            logger.info(f"预期结果：{expected}, 符合实际结果:{actual}")
        else:
            logger.info(f"预期结果：{expected}, 不符合实际结果:{actual}")
