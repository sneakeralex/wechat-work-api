from typing import Dict, Any, List, Optional, Union, BinaryIO
from datetime import datetime
from .client import WeChatWorkClient
from .department import DepartmentAPI
from .user import UserAPI
from .message import MessageAPI
from .media import MediaAPI
from .tag import TagAPI
from .agent import AgentAPI
from .menu import MenuAPI
from .oauth import OAuthAPI
from .jssdk import JSSDKAPI
from .external_contact import ExternalContactAPI
from .group_chat import GroupChatAPI
from .checkin import CheckinAPI

class WeChatWorkAPI:
    """WeChat Work API"""
    
    def __init__(
        self,
        corp_id: Optional[str] = None,
        corp_secret: Optional[str] = None,
        agent_id: Optional[str] = None,
        timeout: int = 30
    ):
        """
        Initialize WeChat Work API
        
        Args:
            corp_id: Corporation ID
            corp_secret: Corporation Secret
            agent_id: Agent ID
            timeout: Request timeout in seconds
        """
        self.client = WeChatWorkClient(
            corp_id=corp_id,
            corp_secret=corp_secret,
            agent_id=agent_id,
            timeout=timeout
        )
        
        # Initialize all API modules
        self.department = DepartmentAPI(self.client)
        self.user = UserAPI(self.client)
        self.message = MessageAPI(self.client)
        self.media = MediaAPI(self.client)
        self.tag = TagAPI(self.client)
        self.agent = AgentAPI(self.client)
        self.menu = MenuAPI(self.client)
        self.oauth = OAuthAPI(self.client)
        self.jssdk = JSSDKAPI(self.client)
        self.external_contact = ExternalContactAPI(self.client)
        self.group_chat = GroupChatAPI(self.client)
        self.checkin = CheckinAPI(self.client)
    
    @property
    def access_token(self) -> str:
        """Get access token"""
        return self.client.access_token
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make GET request"""
        return self.client.get(endpoint, params=params)
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make POST request"""
        return self.client.post(endpoint, data=data)
    
    def post_json(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make POST request with JSON data"""
        return self.client.post_json(endpoint, json_data=json_data) 