import os
import time
import json
import requests
from typing import Optional, Dict, Any
from dotenv import load_dotenv

class WeChatWorkClient:
    """WeChat Work (企业微信) API Client"""
    
    BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin"
    
    def __init__(
        self,
        corp_id: Optional[str] = None,
        corp_secret: Optional[str] = None,
        agent_id: Optional[str] = None,
        timeout: int = 30
    ):
        """
        Initialize WeChat Work client
        
        Args:
            corp_id: Corporation ID
            corp_secret: Corporation Secret
            agent_id: Agent ID
            timeout: Request timeout in seconds
        """
        load_dotenv()
        self.corp_id = corp_id or os.getenv("WECHAT_WORK_CORP_ID")
        self.corp_secret = corp_secret or os.getenv("WECHAT_WORK_CORP_SECRET")
        self.agent_id = agent_id or os.getenv("WECHAT_WORK_AGENT_ID")
        self.timeout = timeout
        self._access_token = None
        self._token_expires_at = 0
        
        if not all([self.corp_id, self.corp_secret]):
            raise ValueError("Corp ID and Corp Secret are required")
    
    @property
    def access_token(self) -> str:
        """Get access token, refresh if expired"""
        if not self._access_token or time.time() >= self._token_expires_at:
            self._refresh_access_token()
        return self._access_token
    
    def _refresh_access_token(self) -> None:
        """Refresh access token"""
        url = f"{self.BASE_URL}/gettoken"
        params = {
            "corpid": self.corp_id,
            "corpsecret": self.corp_secret
        }
        
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        
        if data.get("errcode") != 0:
            raise Exception(f"Failed to get access token: {data.get('errmsg')}")
        
        self._access_token = data["access_token"]
        self._token_expires_at = time.time() + data["expires_in"] - 200  # Refresh 200s before expiry
    
    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make HTTP request to WeChat Work API
        
        Args:
            method: HTTP method
            endpoint: API endpoint
            params: URL parameters
            data: Form data
            json_data: JSON data
            
        Returns:
            API response data
        """
        url = f"{self.BASE_URL}/{endpoint}"
        if params is None:
            params = {}
        params["access_token"] = self.access_token
        
        response = requests.request(
            method=method,
            url=url,
            params=params,
            data=data,
            json=json_data,
            timeout=self.timeout
        )
        response.raise_for_status()
        data = response.json()
        
        if data.get("errcode") != 0:
            raise Exception(f"API request failed: {data.get('errmsg')}")
        
        return data
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make GET request"""
        return self._request("GET", endpoint, params=params)
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make POST request"""
        return self._request("POST", endpoint, data=data)
    
    def post_json(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make POST request with JSON data"""
        return self._request("POST", endpoint, json_data=json_data) 