import pytest
import requests
from common.mock import Mock
from config.read_env import EnvironMent
from scm_api.base_api import Api
from config.file_path import FilePath


class TestMaterial(Api):

    env = EnvironMent()
    url = env.get_env_url()

    mock = Mock()

    yaml = FilePath()
    cases = Api.read_yaml(yaml.material_path)

    @pytest.mark.parametrize("case", cases)
    def test_create_material(self, get_token, case):

        res = requests.post(url=self.url + 'createScmMaterial',
                            headers={"Authorization": f"bearer {get_token}"},
                            json={
                              "operationName": "createScmMaterial",
                              "variables": {
                                "input": {
                                  "category": {
                                    "id": case['category_id']
                                  },
                                  "figureNo": self.mock.ran_py_str(),
                                  "inventoryUnit": {
                                    "id": case['unit_id']
                                  },
                                  "materialQuality": self.mock.ran_py_str(),
                                  "materialSignal": {
                                    "id": case['signal_id']
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
