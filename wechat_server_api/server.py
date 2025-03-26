from typing import Dict, Any, Optional
from .base import BaseClient
from .exceptions import WeChatAPIError

class ServerClient(BaseClient):
    """企业微信 Server API 客户端"""
    
    def __init__(self, corp_id: str, corp_secret: str):
        """
        初始化 Server API 客户端
        
        Args:
            corp_id: 企业ID
            corp_secret: 应用的凭证密钥
        """
        super().__init__(corp_id, corp_secret)
        
    def get_access_token(self) -> str:
        """
        获取访问令牌
        
        Returns:
            str: 访问令牌
        """
        url = f"{self.base_url}/cgi-bin/gettoken"
        params = {
            "corpid": self.corp_id,
            "corpsecret": self.corp_secret
        }
        
        response = self._get(url, params=params)
        if response.get("errcode") == 0:
            return response.get("access_token")
        raise WeChatAPIError(f"获取access_token失败: {response}")
        
    def get_server_ip(self) -> list:
        """
        获取企业微信服务器IP地址
        
        Returns:
            list: IP地址列表
        """
        url = f"{self.base_url}/cgi-bin/getcallbackip"
        params = {"access_token": self.get_access_token()}
        
        response = self._get(url, params=params)
        if response.get("errcode") == 0:
            return response.get("ip_list", [])
        raise WeChatAPIError(f"获取服务器IP失败: {response}")
        
    def get_api_domain_ip(self) -> list:
        """
        获取企业微信API域名IP地址
        
        Returns:
            list: IP地址列表
        """
        url = f"{self.base_url}/cgi-bin/get_api_domain_ip"
        params = {"access_token": self.get_access_token()}
        
        response = self._get(url, params=params)
        if response.get("errcode") == 0:
            return response.get("ip_list", [])
        raise WeChatAPIError(f"获取API域名IP失败: {response}")
        
    def get_jsapi_ticket(self) -> str:
        """
        获取企业微信的jsapi_ticket
        
        Returns:
            str: jsapi_ticket
        """
        url = f"{self.base_url}/cgi-bin/get_jsapi_ticket"
        params = {"access_token": self.get_access_token()}
        
        response = self._get(url, params=params)
        if response.get("errcode") == 0:
            return response.get("ticket")
        raise WeChatAPIError(f"获取jsapi_ticket失败: {response}")
        
    def get_api_ticket(self) -> str:
        """
        获取企业微信的api_ticket
        
        Returns:
            str: api_ticket
        """
        url = f"{self.base_url}/cgi-bin/get_api_ticket"
        params = {"access_token": self.get_access_token()}
        
        response = self._get(url, params=params)
        if response.get("errcode") == 0:
            return response.get("ticket")
        raise WeChatAPIError(f"获取api_ticket失败: {response}")
        
    def get_webhook_key(self, webhook_url: str) -> str:
        """
        获取企业微信群机器人的webhook_key
        
        Args:
            webhook_url: 群机器人的webhook地址
            
        Returns:
            str: webhook_key
        """
        # 从webhook_url中提取key
        if "key=" in webhook_url:
            return webhook_url.split("key=")[1]
        raise WeChatAPIError("无效的webhook地址") 