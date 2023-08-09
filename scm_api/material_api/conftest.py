import pytest
from scm_api.base_api import Api


@pytest.fixture()
def get_token():

    api = Api()
    token = api.login_token()

    yield token


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

