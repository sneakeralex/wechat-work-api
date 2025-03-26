import requests
from typing import Dict, Any, Optional
from .exceptions import WeChatAPIError

class BaseClient:
    """企业微信 API 基础客户端"""
    
    def __init__(self, corp_id: str, corp_secret: str):
        """
        初始化基础客户端
        
        Args:
            corp_id: 企业ID
            corp_secret: 应用的凭证密钥
        """
        self.corp_id = corp_id
        self.corp_secret = corp_secret
        self.base_url = "https://qyapi.weixin.qq.com"
        self.session = requests.Session()
        
    def _get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        发送GET请求
        
        Args:
            url: 请求URL
            params: 请求参数
            
        Returns:
            Dict[str, Any]: 响应数据
        """
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
        
    def _post(self, url: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        发送POST请求
        
        Args:
            url: 请求URL
            data: 请求数据
            
        Returns:
            Dict[str, Any]: 响应数据
        """
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()
        
    def _handle_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        处理API响应
        
        Args:
            response: API响应数据
            
        Returns:
            Dict[str, Any]: 处理后的响应数据
            
        Raises:
            WeChatAPIError: 当API返回错误时
        """
        if response.get("errcode") != 0:
            raise WeChatAPIError(f"API调用失败: {response}")
        return response 