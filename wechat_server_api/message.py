from typing import Dict, Any, List, Optional, Union
from .base import BaseClient
from .exceptions import WeChatAPIError

class MessageClient(BaseClient):
    """企业微信消息推送 API 客户端"""
    
    def __init__(self, corp_id: str, corp_secret: str):
        super().__init__(corp_id, corp_secret)
        
    def send_text(self, agentid: int, content: str, **kwargs) -> Dict[str, Any]:
        """
        发送文本消息
        
        Args:
            agentid: 应用id
            content: 消息内容
            **kwargs: 其他参数
            
        Returns:
            Dict[str, Any]: 发送结果
        """
        data = {
            "msgtype": "text",
            "agentid": agentid,
            "text": {"content": content},
            **kwargs
        }
        return self._send_message(data)
        
    def send_image(self, agentid: int, media_id: str, **kwargs) -> Dict[str, Any]:
        """
        发送图片消息
        
        Args:
            agentid: 应用id
            media_id: 图片媒体文件id
            **kwargs: 其他参数
            
        Returns:
            Dict[str, Any]: 发送结果
        """
        data = {
            "msgtype": "image",
            "agentid": agentid,
            "image": {"media_id": media_id},
            **kwargs
        }
        return self._send_message(data)
        
    def send_voice(self, agentid: int, media_id: str, **kwargs) -> Dict[str, Any]:
        """
        发送语音消息
        
        Args:
            agentid: 应用id
            media_id: 语音媒体文件id
            **kwargs: 其他参数
            
        Returns:
            Dict[str, Any]: 发送结果
        """
        data = {
            "msgtype": "voice",
            "agentid": agentid,
            "voice": {"media_id": media_id},
            **kwargs
        }
        return self._send_message(data)
        
    def send_video(self, agentid: int, media_id: str, title: str, description: str, **kwargs) -> Dict[str, Any]:
        """
        发送视频消息
        
        Args:
            agentid: 应用id
            media_id: 视频媒体文件id
            title: 视频标题
            description: 视频描述
            **kwargs: 其他参数
            
        Returns:
            Dict[str, Any]: 发送结果
        """
        data = {
            "msgtype": "video",
            "agentid": agentid,
            "video": {
                "media_id": media_id,
                "title": title,
                "description": description
            },
            **kwargs
        }
        return self._send_message(data)
        
    def send_file(self, agentid: int, media_id: str, **kwargs) -> Dict[str, Any]:
        """
        发送文件消息
        
        Args:
            agentid: 应用id
            media_id: 文件媒体文件id
            **kwargs: 其他参数
            
        Returns:
            Dict[str, Any]: 发送结果
        """
        data = {
            "msgtype": "file",
            "agentid": agentid,
            "file": {"media_id": media_id},
            **kwargs
        }
        return self._send_message(data)
        
    def send_textcard(self, agentid: int, title: str, description: str, url: str, **kwargs) -> Dict[str, Any]:
        """
        发送文本卡片消息
        
        Args:
            agentid: 应用id
            title: 标题
            description: 描述
            url: 点击后跳转的链接
            **kwargs: 其他参数
            
        Returns:
            Dict[str, Any]: 发送结果
        """
        data = {
            "msgtype": "textcard",
            "agentid": agentid,
            "textcard": {
                "title": title,
                "description": description,
                "url": url
            },
            **kwargs
        }
        return self._send_message(data)
        
    def send_news(self, agentid: int, articles: List[Dict[str, Any]], **kwargs) -> Dict[str, Any]:
        """
        发送图文消息
        
        Args:
            agentid: 应用id
            articles: 图文消息，一个图文消息支持1到8条图文
            **kwargs: 其他参数
            
        Returns:
            Dict[str, Any]: 发送结果
        """
        data = {
            "msgtype": "news",
            "agentid": agentid,
            "news": {"articles": articles},
            **kwargs
        }
        return self._send_message(data)
        
    def send_mpnews(self, agentid: int, articles: List[Dict[str, Any]], **kwargs) -> Dict[str, Any]:
        """
        发送图文消息（mpnews）
        
        Args:
            agentid: 应用id
            articles: 图文消息，一个图文消息支持1到8条图文
            **kwargs: 其他参数
            
        Returns:
            Dict[str, Any]: 发送结果
        """
        data = {
            "msgtype": "mpnews",
            "agentid": agentid,
            "mpnews": {"articles": articles},
            **kwargs
        }
        return self._send_message(data)
        
    def send_markdown(self, agentid: int, content: str, **kwargs) -> Dict[str, Any]:
        """
        发送markdown消息
        
        Args:
            agentid: 应用id
            content: markdown内容
            **kwargs: 其他参数
            
        Returns:
            Dict[str, Any]: 发送结果
        """
        data = {
            "msgtype": "markdown",
            "agentid": agentid,
            "markdown": {"content": content},
            **kwargs
        }
        return self._send_message(data)
        
    def _send_message(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        发送消息
        
        Args:
            data: 消息数据
            
        Returns:
            Dict[str, Any]: 发送结果
        """
        url = f"{self.base_url}/cgi-bin/message/send"
        params = {"access_token": self.get_access_token()}
        
        response = self._post(url, data=data)
        return response 