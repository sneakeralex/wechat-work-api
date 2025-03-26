from typing import Dict, Any, Optional
from .client import WeChatWorkClient

class OAuthAPI:
    """OAuth2 API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def get_user_info(self, code: str) -> Dict[str, Any]:
        """
        Get user info by code
        
        Args:
            code: Authorization code
            
        Returns:
            User info
        """
        return self.client.get("user/getuserinfo", params={"code": code})
    
    def get_user_detail(self, user_ticket: str) -> Dict[str, Any]:
        """
        Get user detail by user ticket
        
        Args:
            user_ticket: User ticket
            
        Returns:
            User detail
        """
        return self.client.post_json("user/get_userdetail", json_data={"user_ticket": user_ticket})
    
    def get_login_info(self, auth_code: str) -> Dict[str, Any]:
        """
        Get login info by auth code
        
        Args:
            auth_code: Authorization code
            
        Returns:
            Login info
        """
        return self.client.post_json("user/get_login_info", json_data={"auth_code": auth_code}) 