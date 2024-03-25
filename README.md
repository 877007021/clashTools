# clashTools

利用 clash api 对 clash 进行增强。默认的 clash 是对节点延迟进行检查，但是低延迟并不一定有好的速度，多数时候不需要低延迟，而是要更好的速度。
该工具使用当前选择的节点进行测试，如果当前节点不可以用或不满足条件，则进行切换，使用本地网络寻找最适合当前网络的节点。

## 配置说明

初始化只需从一个入口设置即可，由于每个人的定义不一样，分组也不一样，最好在 启动时指定分组名称

#### 启动参数初始化

- base_url：clash api 地址
- secret：clash api 认证
- proxy_url：clash 代理地址
- group_name：clash 代理分组名称，如果名称中有图标，请Unicode编码
- timeout: 测试下载文件超时时间，默认10s
- max_size: 测试下载文件大小，默认10M

- 示例:

```shell
python main.py --base_url 127.0.0.1:55327 --secret 83fe3c0d-7652-46f5-9f15-xxxxxxxx --proxy_url 127.0.0.1:7890 --timeout 5 --max_size 10485760 --group_name "\ud83d\ude80\u0020\u8282\u70b9\u9009\u62e9"
```

#### 配置文件初始化

clash 相关的配置默认从 `~/.config/clash/config.yaml` 中获取 clash api 的地址与认证信息。如果获取失败就从环境变量中进行获取

#### 环境变量初始化

环境变量的优先级是最低的

- `BASE_URL`: clash api 的restful-api地址
- `SECRET`: clash api 的restful-api认证信息
- `GROUP_NAME`: clash 代理分组名称