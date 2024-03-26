import json
import os

_instance = None


# noinspection HttpUrlsUsage
class Config:
    def __init__(self):
        self.timeout = 10
        self.proxy_url = None
        self.secret = None
        self.base_url = None
        self.args = None
        self.group_name = None
        self.max_size = 10485760
        self.scheduler_time = 15

    def set_args(self, args):
        self.args = args
        if hasattr(args, 'base_url') and args.base_url:
            if args.base_url.startswith('http'):
                self.base_url = args.base_url
            else:
                self.base_url = "http://" + args.base_url
        self.secret = args.secret
        self.proxy_url = args.proxy_url
        self.group_name = args.group_name

        if args.group_name:
            self.group_name = json.loads('"%s"' % args.group_name)

        if hasattr(args, 'timeout') and args.timeout:
            self.timeout = int(args.timeout)
        else:
            self.timeout = 10

        if hasattr(args, "max_size") and args.max_size:
            self.max_size = int(args.max_size)
        if hasattr(args, "scheduler_time") and args.scheduler_time:
            self.scheduler_time = int(args.scheduler_time)

    def set_args_of_env(self):
        if os.environ.get("base_url", None):
            if os.environ.get("base_url").startswith('http'):
                self.base_url = os.environ.get("base_url")
            else:
                self.base_url = "http://" + os.environ.get("base_url")
        if os.environ.get("secret", None):
            self.secret = os.environ.get("secret")
        if os.environ.get("timeout", None):
            self.timeout = int(os.environ.get("timeout", 10))
        if os.environ.get("proxy_url"):
            if os.environ.get("proxy_url").startswith('http'):
                self.proxy_url = os.environ.get("proxy_url")
            else:
                self.proxy_url = "http://" + os.environ.get("proxy_url")
        if os.environ.get("group_name"):
            self.group_name = json.loads('"%s"' % os.environ.get("group_name"))
        if os.environ.get("max_size"):
            self.max_size = int(os.environ.get("max_size", 10485760))
        if os.environ.get("scheduler_time"):
            self.scheduler_time = int(os.environ.get("scheduler_time"))


def get_config():
    global _instance
    if _instance is None:
        _instance = Config()
    return _instance
