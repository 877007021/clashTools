import requests

from configruation import get_config


# noinspection PyBroadException
def test_download():
    try:
        # 测试下载10M的文件
        test_url = f"https://speed.cloudflare.com/__down?during=download&bytes={get_config().max_size}"
        proxies = {"http": get_config().proxy_url, "https": get_config().proxy_url}
        requests.get(test_url, timeout=get_config().timeout, proxies=proxies)
        return True
    except:
        return False
