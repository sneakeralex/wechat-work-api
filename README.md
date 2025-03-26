# WeChat Work API Client

企业微信 API 客户端，提供简单易用的接口来调用企业微信的各种 API。

## 安装

```bash
pip install wechatapi
```

## 快速开始

### 初始化客户端

```python
from wechatapi import ServerClient, ContactClient, AgentClient, MessageClient, MediaClient, WecomClient

# 创建客户端实例
corp_id = "your_corp_id"
corp_secret = "your_corp_secret"

# 服务器 API 客户端
server_client = ServerClient(corp_id, corp_secret)

# 通讯录管理客户端
contact_client = ContactClient(corp_id, corp_secret)

# 应用管理客户端
agent_client = AgentClient(corp_id, corp_secret)

# 消息推送客户端
message_client = MessageClient(corp_id, corp_secret)

# 媒体文件客户端
media_client = MediaClient(corp_id, corp_secret)

# 企业微信专用接口客户端
wecom_client = WecomClient(corp_id, corp_secret)
```

## API 使用示例

### 服务器 API

```python
# 获取访问令牌
access_token = server_client.get_access_token()

# 获取服务器 IP 地址
server_ips = server_client.get_server_ip()

# 获取 API 域名 IP 地址
api_domain_ips = server_client.get_api_domain_ip()

# 获取 jsapi_ticket
jsapi_ticket = server_client.get_jsapi_ticket()

# 获取 api_ticket
api_ticket = server_client.get_api_ticket()

# 从 webhook URL 获取 key
webhook_key = server_client.get_webhook_key("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=your_key")
```

### 通讯录管理

```python
# 创建部门
department_id = contact_client.create_department(
    name="技术部",
    parentid=1,
    order=1
)

# 更新部门
contact_client.update_department(
    id=department_id,
    name="研发部",
    order=2
)

# 获取部门列表
departments = contact_client.get_department_list()

# 创建成员
contact_client.create_user(
    userid="zhangsan",
    name="张三",
    department=[department_id],
    mobile="13800138000",
    email="zhangsan@example.com"
)

# 更新成员
contact_client.update_user(
    userid="zhangsan",
    name="张三丰",
    mobile="13800138001"
)

# 获取部门成员
users = contact_client.get_department_users(department_id)

# 获取部门成员详情
user_details = contact_client.get_department_users_detail(department_id)

# userid 转 openid
openid = contact_client.convert_userid_to_openid("zhangsan")

# openid 转 userid
userid = contact_client.convert_openid_to_userid(openid)

# 获取用户信息
user_info = contact_client.get_user_info("code")
```

### 应用管理

```python
# 获取应用列表
agents = agent_client.get_agent_list()

# 获取应用信息
agent_info = agent_client.get_agent(agents[0]["agentid"])

# 设置应用
agent_client.set_agent(
    agentid=agents[0]["agentid"],
    name="测试应用",
    description="这是一个测试应用"
)

# 设置应用可见范围
agent_client.set_agent_scope(
    agentid=agents[0]["agentid"],
    allow_user=["zhangsan", "lisi"],
    allow_party=[1, 2],
    allow_tag=[1, 2]
)

# 获取应用可见范围
scope = agent_client.get_agent_scope(agents[0]["agentid"])

# 设置应用工作台自定义展示
agent_client.set_agent_workbench_template(
    agentid=agents[0]["agentid"],
    type="keydata",
    keydata={
        "items": [
            {
                "key": "待审批",
                "data": "2",
                "jump_url": "https://example.com/approve"
            }
        ]
    }
)

# 获取应用工作台自定义展示
template = agent_client.get_agent_workbench_template(agents[0]["agentid"])

# 设置应用工作台自定义展示数据
agent_client.set_agent_workbench_data(
    agentid=agents[0]["agentid"],
    userid="zhangsan",
    keydata={
        "items": [
            {
                "key": "待审批",
                "data": "3",
                "jump_url": "https://example.com/approve"
            }
        ]
    }
)
```

### 消息推送

```python
# 发送文本消息
message_client.send_text(
    agentid=agents[0]["agentid"],
    content="这是一条测试消息",
    touser="@all"
)

# 发送图片消息
message_client.send_image(
    agentid=agents[0]["agentid"],
    media_id="MEDIA_ID",
    touser="@all"
)

# 发送语音消息
message_client.send_voice(
    agentid=agents[0]["agentid"],
    media_id="MEDIA_ID",
    touser="@all"
)

# 发送视频消息
message_client.send_video(
    agentid=agents[0]["agentid"],
    media_id="MEDIA_ID",
    title="视频标题",
    description="视频描述",
    touser="@all"
)

# 发送文件消息
message_client.send_file(
    agentid=agents[0]["agentid"],
    media_id="MEDIA_ID",
    touser="@all"
)

# 发送文本卡片消息
message_client.send_textcard(
    agentid=agents[0]["agentid"],
    title="文本卡片标题",
    description="文本卡片描述",
    url="https://example.com",
    touser="@all"
)

# 发送图文消息
message_client.send_news(
    agentid=agents[0]["agentid"],
    articles=[
        {
            "title": "图文消息标题",
            "description": "图文消息描述",
            "url": "https://example.com",
            "picurl": "https://example.com/image.jpg"
        }
    ],
    touser="@all"
)

# 发送 markdown 消息
message_client.send_markdown(
    agentid=agents[0]["agentid"],
    content="""# 标题
> 引用
**加粗**
*斜体*
[链接](https://example.com)""",
    touser="@all"
)
```

### 媒体文件

```python
# 上传临时素材
with open("image.jpg", "rb") as f:
    media_id = media_client.upload_image(f)

# 上传语音
with open("voice.mp3", "rb") as f:
    media_id = media_client.upload_voice(f)

# 上传视频
with open("video.mp4", "rb") as f:
    media_id = media_client.upload_video(f)

# 上传普通文件
with open("document.pdf", "rb") as f:
    media_id = media_client.upload_file(f)

# 获取临时素材
media_content = media_client.get(media_id)

# 上传永久素材
with open("image.jpg", "rb") as f:
    media_id = media_client.upload_permanent("image", f)

# 获取永久素材
media_content = media_client.get_permanent(media_id)

# 删除永久素材
media_client.delete_permanent(media_id)

# 获取永久素材数量
counts = media_client.get_permanent_count()

# 获取永久素材列表
materials = media_client.get_permanent_list("image", offset=0, count=20)
```

### 企业微信专用接口

```python
# 判断接口支持情况
interface_support = wecom_client.get_interface_support()

# 获取企业成员信息
member_info = wecom_client.get_member_info("zhangsan")

# 获取企业通讯录与会话
session_info = wecom_client.get_address_book_session("zhangsan")

# 获取 NFC 信息
nfc_info = wecom_client.get_nfc_info("nfc_id")

# 发送小程序通知
wecom_client.send_miniprogram_notice(
    touser="zhangsan",
    template_id="template_id",
    page="pages/index/index",
    data={
        "first": {"value": "您好"},
        "keyword1": {"value": "测试内容"},
        "remark": {"value": "感谢使用"}
    }
)

# 语音转文字
speech_result = wecom_client.speech_to_text(
    media_id="MEDIA_ID",
    language="zh_CN",
    voice_type=1
)

# 获取 OAuth2.0 用户信息
oauth_info = wecom_client.get_oauth_user_info("code")

# 获取 Web 登录信息
web_login_info = wecom_client.get_web_login_info("code")

# 获取扫一扫登录信息
scan_login_info = wecom_client.get_scan_login_info("code")

# 获取移动端登录信息
mobile_login_info = wecom_client.get_mobile_login_info("code")

# HTTP 回调登录
callback_login = wecom_client.http_callback_login(
    callback_url="https://example.com/callback",
    state="state",
    userid="zhangsan"
)

# 第三方 APP 登录
app_login = wecom_client.third_party_app_login(
    app_id="app_id",
    app_secret="app_secret",
    code="code"
)

# 第三方系统接入
system_login = wecom_client.third_party_system_login(
    system_id="system_id",
    system_secret="system_secret",
    code="code"
)

# 短信网关接入
sms_login = wecom_client.sms_gateway_login(
    gateway_id="gateway_id",
    gateway_secret="gateway_secret",
    phone="13800138000"
)

# 语音转文字网关接入
speech_login = wecom_client.speech_gateway_login(
    gateway_id="gateway_id",
    gateway_secret="gateway_secret",
    phone="13800138000"
)

# 获取操作日志
operation_logs = wecom_client.get_operation_logs(
    start_time=1625097600,
    end_time=1625184000,
    userids=["zhangsan", "lisi"],
    partyids=[1, 2]
)

# 导出统计数据
statistics_data = wecom_client.export_statistics_data(
    start_time=1625097600,
    end_time=1625184000,
    data_type="daily"
)

# 获取会话内容
session_content = wecom_client.get_session_content(
    info=[
        {
            "userid": "zhangsan",
            "chat_type": "single",
            "msg_type": "text"
        }
    ],
    cursor="cursor"
)

# 获取会话同意情况
agree_info = wecom_client.get_session_agree_info(
    info=[
        {
            "userid": "zhangsan",
            "chat_type": "single"
        }
    ]
)

# 账号解密
decrypted_account = wecom_client.decrypt_account(
    encrypted_data="encrypted_data",
    iv="iv"
)

# 消息关键字过滤
filter_result = wecom_client.filter_message_keywords(
    content="这是一条测试消息",
    keywords=["测试", "敏感词"]
)
```

## 异常处理

```python
from wechatapi import WeChatAPIError, WeChatConfigError, WeChatAuthError

try:
    # API 调用
    result = client.some_api_call()
except WeChatAPIError as e:
    print(f"API 调用失败: {e}")
except WeChatConfigError as e:
    print(f"配置错误: {e}")
except WeChatAuthError as e:
    print(f"认证错误: {e}")
```

## 注意事项

1. 所有 API 调用都需要提供有效的 `corp_id` 和 `corp_secret`
2. 媒体文件上传时需要使用二进制模式打开文件
3. 部分 API 可能需要特定的权限，请确保应用有相应的权限
4. 建议在生产环境中实现 access_token 的缓存机制，避免频繁请求

## 许可证

MIT License 