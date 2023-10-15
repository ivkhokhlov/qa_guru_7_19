import pytest

from config import CATFACT_BASE_URL
from src.base_request import make_request


@pytest.fixture(scope='session')
def catfact_request():
    base_url = CATFACT_BASE_URL
    return lambda method, endpoint, **kwargs: make_request(method, base_url, endpoint, **kwargs)