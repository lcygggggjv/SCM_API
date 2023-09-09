import pytest
from scm_api.base_api import Api


@pytest.fixture()
def get_token():

    api = Api()
    tokens = api.login_token()

    yield tokens


@pytest.fixture()
def get_data():

    api = Api()
    cate_id = api.get_category()
    unit_id = api.get_unit()
    signal = api.get_signal()

    create_id = api.get_create_material_id()
    yield cate_id, unit_id, signal, create_id


if __name__ == '__main__':

    token = get_token
    print(token)
