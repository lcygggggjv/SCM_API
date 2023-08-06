import requests
from config.read_env import EnvironMent


class Api:

    env = EnvironMent()

    env_url = env.get_env_url()
    tenant_code = env.tenant_code()
    account = env.account()
    password = env.password()

    @classmethod
    def login_token(cls):

        res = requests.request('post',
                               url=Api.env_url + "login",
                               json={
                                  "operationName": "login",
                                  "variables": {
                                    "input": {
                                      "account": Api.account,
                                      "password": Api.password,
                                      "tenantCode": Api.tenant_code
                                    }
                                  },
                                  "query": "mutation login($input: LoginInput!) {\n  login(input: $input) "
                                           "{\n    token\n    userId\n    __typename\n  }\n}"
                                 })

        result = res.json()
        login_token = result['data']['login']['token']
        return login_token


if __name__ == '__main__':

    ao = Api()
    OD = ao.login_token()
    print(OD)
