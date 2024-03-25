import os
import yaml
from loguru import logger
import argparse
from clash import api, test
from configruation import get_config


# noinspection PyBroadException
def get_user_config():
    try:
        clash_config_path = os.path.join(os.path.expanduser('~'), ".config", "clash", "config.yaml")
        with open(clash_config_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except:
        return None


# noinspection HttpUrlsUsage
def init_config():
    if get_config().base_url and get_config().secret and get_config().proxy_url:
        return
    clash_config = get_user_config()
    if clash_config is not None:
        get_config().base_url = f"http://{clash_config['external-controller']}"
        get_config().secret = clash_config['secret']
        get_config().proxy_url = f"http://127.0.0.1:{clash_config['mixed-port']}"
    if get_config().group_name is None:
        get_config().group_name = "🚀 手动切换"


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='clash tools')
    parser.add_argument('--base_url', help='clash api 地址')
    parser.add_argument('--secret', help='clash api 认证')
    parser.add_argument('--proxy_url', help='clash 代理地址')
    parser.add_argument('--group_name', help='clash 代理分组名称')
    parser.add_argument('--timeout', help='节点测试超时时间')
    parser.add_argument('--max_size', help='节点测试下载文件大小')
    get_config().set_args(parser.parse_args())
    init_config()
    proxies_names = api.get_proxies_names(get_config().group_name)
    if get_config().proxy_url is None:
        get_config().proxy_url = api.get_proxy_url()
    for proxies_name in proxies_names:
        if not test.test_download():
            api.switch_proxy(get_config().group_name, proxies_name)
            logger.warning(f"当前代理测试失败，切换代理[{get_config().group_name} -> {proxies_name}]")
        else:
            logger.info("当前代理测试成功")
            break
