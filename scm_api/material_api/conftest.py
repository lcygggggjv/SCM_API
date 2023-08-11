import pytest
from scm_api.base_api import Api


@pytest.fixture()
def get_token():

    api = Api()
    token = api.login_token()

    yield token


@pytest.fixture()
def get_data():

    api = Api()
    cate_id = api.get_category()
    unit_id = api.get_unit()
    signal = api.get_signal()

    yield cate_id, unit_id, signal


def test_get_data(get_token):

    print(get_token)


# @pytest.fixture()
# def tz_1():
#
#     print(1)
#
#
# def test_1(tz_1):
#
#     print(tz_1)

