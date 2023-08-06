import requests

from config.read_env import EnvironMent
from scm_api.base_api import Api


class TestMaterial(Api):

    env = EnvironMent()
    url = env.get_env_url()

    def test_create_material(self, ):

        res = requests.post(url=self.url + 'createScmMaterial',
                            headers={"Authorization": f"bearer {token}"})