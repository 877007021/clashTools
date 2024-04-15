import json
import traceback

import requests

from configruation import get_config


def proxies():
    res = request(method="GET", url="/proxies")
    return res.json()


def get_proxies_names(group_name: str = None) -> list:
    # noinspection PyBroadException
    try:
        proxies_names = []
        proxies_dict = {}
        proxies_properties = proxies()
        if group_name is None:
            group_name = "GLOBAL"
        for name in proxies_properties['proxies'][group_name]['all']:
            try:
                history = proxies_properties['proxies'][name]['history']
                if not history or len(history) <= 0:
                    proxies_dict[name] = 9999
                    continue
                proxies_dict[name] = history[-1]['delay']
            except:
                pass
        proxies_tuple_list = sorted(proxies_dict.items(), key=lambda x: x[1])
        [proxies_names.append(name) for (name, delay) in proxies_tuple_list]
        return proxies_names
    except:
        return []


def get_proxy_url() -> str:
    res = request(method="GET", url="/configs")
    return f"http://127.0.0.1:{res.json()['mixed-port']}"


def switch_proxy(group_name: str, proxy_name: str):
    res = request(method="PUT", url=f"/proxies/{group_name}", data={'name': f"{proxy_name}"})
    if res.status_code != 204:
        raise Exception("切换 clash 配置失败")
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
