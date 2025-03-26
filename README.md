# WeChat Work API Client

A comprehensive Python client for WeChat Work (企业微信) API that supports all available APIs including department management, user management, message sending, media management, and more.

## Features

- ✨ Complete API coverage
- 🔒 Secure authentication handling
- 🚀 Easy to use interface
- 📝 Type hints for better IDE support
- 📦 Modular design
- 🔄 Automatic access token management

## Installation

```bash
pip install wechat-work-api
```

## Quick Start

```python
from wechat_work import WeChatWorkAPI

# Initialize the API
api = WeChatWorkAPI(
    corp_id="your_corp_id",
    corp_secret="your_corp_secret",
    agent_id="your_agent_id"
)

# Use department APIs
departments = api.department.list()

# Send a message
api.message.send_text(
    agent_id="1",
    content="Hello!",
    to_user="user1|user2"
)

# Get user info
user_info = api.user.get("user1")

# Upload media
with open("image.jpg", "rb") as f:
    media_id = api.media.upload("image", f)

# Create external contact way
contact_way = api.external_contact.create_contact_way(
    type=1,
    scene=1,
    style=1,
    remark="Welcome"
)

# Get check-in data
checkin_data = api.checkin.get_checkin_data(
    open_checkin_data=[{"userid": "user1"}]
)
```

## Available APIs

The client provides access to all WeChat Work APIs through the following modules:

- `department`: Department management
  - Create, update, delete departments
  - List departments and their hierarchies

- `user`: User management
  - Create, update, delete users
  - Get user information
  - Convert OpenID to UserID

- `message`: Message management
  - Send text, image, voice messages
  - Send file, video messages
  - Send card messages
  - Send markdown messages

- `media`: Media management
  - Upload temporary media
  - Upload permanent media
  - Get media by ID

- `tag`: Tag management
  - Create, update, delete tags
  - Add/remove tag members
  - Get tag lists and members

- `agent`: Agent management
  - Get agent details
  - Set agent configurations
  - Get agent menu

- `menu`: Menu management
  - Create custom menus
  - Get menu configurations
  - Delete menus

- `oauth`: OAuth2 authentication
  - Get user information
  - Get user details
  - Get login information

- `jssdk`: JSSDK support
  - Get JSAPI ticket
  - Get agent config
  - Generate JSAPI signature

- `external_contact`: External contact management
  - Get external contact list
  - Get external contact details
  - Configure contact ways
  - Manage corporate tags

- `group_chat`: Group chat management
  - Create group chats
  - Update group chat settings
  - Send group messages
  - Get group chat information

- `checkin`: Check-in management
  - Get check-in data
  - Get check-in rules
  - Get check-in statistics

## Authentication

The client handles authentication automatically. Just provide your credentials when initializing:

```python
api = WeChatWorkAPI(
    corp_id="your_corp_id",
    corp_secret="your_corp_secret",
    agent_id="your_agent_id"  # Optional, required for some APIs
)
```

## Advanced Usage

### Custom Requests

You can make custom requests to any endpoint:

```python
# GET request
result = api.get("custom/endpoint", params={"key": "value"})

# POST request
result = api.post("custom/endpoint", data={"key": "value"})

# POST with JSON
result = api.post_json("custom/endpoint", json_data={"key": "value"})
```

### Access Token

Access the current access token:

```python
token = api.access_token
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 