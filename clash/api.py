import json
import os
import traceback

import requests

from configruation import get_config


def proxies():
    res = request(method="GET", url="/proxies")
    return res.json()


def get_proxies_names(group_name: str = None) -> set:
    # noinspection PyBroadException
    try:
        proxies_properties = proxies()
        if group_name is None:
            group_name = "GLOBAL"
        return set(proxies_properties['proxies'][group_name]['all'])
    except:
        return set()


def get_proxy_url() -> str:
    res = request(method="GET", url="/configs")
    return f"http://127.0.0.1:{res.json()['mixed-port']}"


def switch_proxy(group_name: str, proxy_name: str):
    res = request(method="PUT", url=f"/proxies/{group_name}", data={'name': f"{proxy_name}"})
    print()


# noinspection PyBroadException
def request(method, url: str, data: dict = None):
    try:
        if url.startswith("/"):
            request_url = get_config().base_url + url
        else:
            request_url = get_config().base_url + "/" + url
        headers = {
            'Authorization': "Bearer " + get_config().secret
        }
        res = requests.request(method, request_url, headers=headers, data=json.dumps(data))
        res.raise_for_status()
        return res
    except:
        traceback.print_exc()
        return None
