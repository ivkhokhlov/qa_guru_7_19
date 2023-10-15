import pytest

from config import REQRES_BASE_URL
from src.base_request import make_request


@pytest.fixture(scope='session')
def reqres_request():
    base_url = REQRES_BASE_URL
    return lambda method, endpoint, **kwargs: make_request(method, base_url, endpoint, **kwargs)