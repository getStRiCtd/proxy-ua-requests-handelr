import random

from cfg import (
    PATH_TO_PROXY, PATH_TO_UA
)


def rollover_proxy(proxies) -> dict:
    proxy = random.choice(proxies).split(':')
    proxy_login_pass = ':'.join(proxy[2:])
    proxy_host_port = ':'.join(proxy[:2])
    proxy = f'http://{"@".join([proxy_login_pass, proxy_host_port])}'
    proxy = {"http": proxy, 'https': proxy}
    return proxy


def rollover_ua(ua):
    ua = random.choice(ua)
    headers = {
        "User-Agent": ua.strip()}
    return headers


with open(PATH_TO_PROXY) as file:
    proxies = file.readlines()


with open(PATH_TO_UA, 'r') as file:
    ua = file.readlines()


def proxy_ua_handler(func):
    proxy = rollover_proxy(proxies)
    header = rollover_ua(ua)

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs,  headers=header, proxies=proxy)
    return wrapper
