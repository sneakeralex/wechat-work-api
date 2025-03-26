from typing import Dict, Any, Optional
import requests
from .exceptions import WeChatAPIError, WeChatConfigError, WeChatAuthError

class WecomBaseClient:
    """企业微信 API 基础客户端"""
    
    def __init__(self, corp_id: str, corp_secret: str):
        self.corp_id = corp_id
        self.corp_secret = corp_secret
        self.access_token = None
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin"
        
    def _get_access_token(self) -> str:
        """获取访问令牌"""
        if self.access_token:
            return self.access_token
            
        url = f"{self.base_url}/gettoken"
        params = {
            "corpid": self.corp_id,
            "corpsecret": self.corp_secret
        }
        
        response = requests.get(url, params=params)
        result = response.json()
        
        if result.get("errcode") == 0:
            self.access_token = result.get("access_token")
            return self.access_token
        else:
            raise WeChatAuthError(f"获取 access_token 失败: {result.get('errmsg')}")
            
    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """发送 GET 请求"""
        if params is None:
            params = {}
            
        params["access_token"] = self._get_access_token()
        url = f"{self.base_url}/{endpoint}"
        
        response = requests.get(url, params=params)
        result = response.json()
        
        if result.get("errcode") == 0:
            return result
        else:
            raise WeChatAPIError(f"API 调用失败: {result.get('errmsg')}")
            
    def _post(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """发送 POST 请求"""
        if json is None:
            json = {}
            
        params = {"access_token": self._get_access_token()}
        url = f"{self.base_url}/{endpoint}"
        
        response = requests.post(url, params=params, json=json)
        result = response.json()
        
        if result.get("errcode") == 0:
            return result
        else:
            raise WeChatAPIError(f"API 调用失败: {result.get('errmsg')}")
            
    def _post_file(self, endpoint: str, files: Dict[str, Any], data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """发送文件上传请求"""
        if data is None:
            data = {}
            
        params = {"access_token": self._get_access_token()}
        url = f"{self.base_url}/{endpoint}"
        
        response = requests.post(url, params=params, files=files, data=data)
        result = response.json()
        
        if result.get("errcode") == 0:
            return result
        else:
            raise WeChatAPIError(f"API 调用失败: {result.get('errmsg')}") 