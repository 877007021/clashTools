import json

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


def get_config():
    global _instance
    if _instance is None:
        _instance = Config()
    return _instance
