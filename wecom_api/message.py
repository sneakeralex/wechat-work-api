from typing import Dict, List, Any, Optional
from .base import WecomBaseClient

class MessageClient(WecomBaseClient):
    """消息推送客户端"""
    
    def send_text(self,
                 agentid: str,
                 content: str,
                 touser: Optional[str] = None,
                 toparty: Optional[str] = None,
                 totag: Optional[str] = None,
                 safe: int = 0) -> Dict[str, Any]:
        """发送文本消息"""
        data = {
            "msgtype": "text",
            "agentid": agentid,
            "text": {"content": content},
            "safe": safe
        }
        if touser:
            data["touser"] = touser
        if toparty:
            data["toparty"] = toparty
        if totag:
            data["totag"] = totag
        return self._post("message/send", json=data)
    
    def send_image(self,
                  agentid: str,
                  media_id: str,
                  touser: Optional[str] = None,
                  toparty: Optional[str] = None,
                  totag: Optional[str] = None,
                  safe: int = 0) -> Dict[str, Any]:
        """发送图片消息"""
        data = {
            "msgtype": "image",
            "agentid": agentid,
            "image": {"media_id": media_id},
            "safe": safe
        }
        if touser:
            data["touser"] = touser
        if toparty:
            data["toparty"] = toparty
        if totag:
            data["totag"] = totag
        return self._post("message/send", json=data)
    
    def send_voice(self,
                  agentid: str,
                  media_id: str,
                  touser: Optional[str] = None,
                  toparty: Optional[str] = None,
                  totag: Optional[str] = None,
                  safe: int = 0) -> Dict[str, Any]:
        """发送语音消息"""
        data = {
            "msgtype": "voice",
            "agentid": agentid,
            "voice": {"media_id": media_id},
            "safe": safe
        }
        if touser:
            data["touser"] = touser
        if toparty:
            data["toparty"] = toparty
        if totag:
            data["totag"] = totag
        return self._post("message/send", json=data)
    
    def send_video(self,
                  agentid: str,
                  media_id: str,
                  title: str,
                  description: str,
                  touser: Optional[str] = None,
                  toparty: Optional[str] = None,
                  totag: Optional[str] = None,
                  safe: int = 0) -> Dict[str, Any]:
        """发送视频消息"""
        data = {
            "msgtype": "video",
            "agentid": agentid,
            "video": {
                "media_id": media_id,
                "title": title,
                "description": description
            },
            "safe": safe
        }
        if touser:
            data["touser"] = touser
        if toparty:
            data["toparty"] = toparty
        if totag:
            data["totag"] = totag
        return self._post("message/send", json=data)
    
    def send_file(self,
                 agentid: str,
                 media_id: str,
                 touser: Optional[str] = None,
                 toparty: Optional[str] = None,
                 totag: Optional[str] = None,
                 safe: int = 0) -> Dict[str, Any]:
        """发送文件消息"""
        data = {
            "msgtype": "file",
            "agentid": agentid,
            "file": {"media_id": media_id},
            "safe": safe
        }
        if touser:
            data["touser"] = touser
        if toparty:
            data["toparty"] = toparty
        if totag:
            data["totag"] = totag
        return self._post("message/send", json=data)
    
    def send_textcard(self,
                     agentid: str,
                     title: str,
                     description: str,
                     url: str,
                     touser: Optional[str] = None,
                     toparty: Optional[str] = None,
                     totag: Optional[str] = None,
                     safe: int = 0) -> Dict[str, Any]:
        """发送文本卡片消息"""
        data = {
            "msgtype": "textcard",
            "agentid": agentid,
            "textcard": {
                "title": title,
                "description": description,
                "url": url
            },
            "safe": safe
        }
        if touser:
            data["touser"] = touser
        if toparty:
            data["toparty"] = toparty
        if totag:
            data["totag"] = totag
        return self._post("message/send", json=data)
    
    def send_news(self,
                 agentid: str,
                 articles: List[Dict[str, str]],
                 touser: Optional[str] = None,
                 toparty: Optional[str] = None,
                 totag: Optional[str] = None,
                 safe: int = 0) -> Dict[str, Any]:
        """发送图文消息"""
        data = {
            "msgtype": "news",
            "agentid": agentid,
            "news": {"articles": articles},
            "safe": safe
        }
        if touser:
            data["touser"] = touser
        if toparty:
            data["toparty"] = toparty
        if totag:
            data["totag"] = totag
        return self._post("message/send", json=data)
    
    def send_markdown(self,
                     agentid: str,
                     content: str,
                     touser: Optional[str] = None,
                     toparty: Optional[str] = None,
                     totag: Optional[str] = None,
                     safe: int = 0) -> Dict[str, Any]:
        """发送 markdown 消息"""
        data = {
            "msgtype": "markdown",
            "agentid": agentid,
            "markdown": {"content": content},
            "safe": safe
        }
        if touser:
            data["touser"] = touser
        if toparty:
            data["toparty"] = toparty
        if totag:
            data["totag"] = totag
        return self._post("message/send", json=data) 