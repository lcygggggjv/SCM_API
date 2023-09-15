import pytest
import requests

from common.mock import Mock
from config.read_env import EnvironMent
from scm_api.base_api import Api


# class TestSignal(Api):
#
#     env = EnvironMent()
#     url = env.get_env_url()
#
#     mock = Mock()
#
#     @pytest.mark.parametrize('cases', )
#     def test_create_signal(self, get_token, cases):
#
#         if case["data"]["code"] == 'code':
#             code = self.mock.ran_py_str()
#         else:
#             code = case["data"]["code"]
#
#         if case["data"]["name"] == "name":
#             name = self.mock.ran_py_str()
#         else:
#             name = case["data"]["name"]
#
#         ress = requests.post(url=self.url+'createScmMaterialSignal',
#                              headers={"Authorization": f"bearer {get_token}"},
#                              json={
#                               "operationName": "createScmMaterialSignal",
#                               "variables": {
#                                 "input": {
#                                   "name": "erewrh",
#                                   "no": "dcyh",
#                                   "srmUsageStatus": "NORMAL",
#                                   "wmsUsageStatus": "NORMAL"
#                                 }
#                               },
#                               "query": "mutation createScmMaterialSignal($input: "
#                                        "CreateScmMaterialSignalInput!) {\n  createScmMaterialSignal(input: $input)\n}"
#                             })