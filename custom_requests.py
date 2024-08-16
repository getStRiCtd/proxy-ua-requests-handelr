from requests.api import request
from headers_handler import proxy_ua_handler


@proxy_ua_handler
def get(url, params=None, **kwargs):
    return request("get", url, params=params, **kwargs)


@proxy_ua_handler
def head(url, **kwargs):
    kwargs.setdefault("allow_redirects", False)
    return request("head", url, **kwargs)


print(get('https://fastapi.tiangolo.com/python-types/').status_code)
