import json
from json.decoder import JSONDecodeError
from urllib.parse import urljoin

import allure
from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import request


@allure.step('Выполнить запрос: {method}')
def make_request(method, base_url, endpoint, **kwargs):
    response = request(method, url=urljoin(base_url, endpoint), **kwargs)
    allure.attach(body=to_curl(response.request),
                  name='cURL',
                  attachment_type=AttachmentType.TEXT,
                  extension='txt')

    try:
        response_data = response.json()
        allure.attach(body=json.dumps(response_data, indent=4),
                      name='response body',
                      attachment_type=AttachmentType.JSON,
                      extension='json')
    except JSONDecodeError as e:
        response_data = ''

    return response
