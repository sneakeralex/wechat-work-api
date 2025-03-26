from typing import Dict, Any, List, Optional, Union
from .client import WeChatWorkClient

class MessageAPI:
    """Message API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def send_text(
        self,
        content: str,
        to_user: Optional[List[str]] = None,
        to_party: Optional[List[str]] = None,
        to_tag: Optional[List[str]] = None,
        safe: bool = False,
        agent_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send text message
        
        Args:
            content: Message content
            to_user: List of user IDs
            to_party: List of department IDs
            to_tag: List of tag IDs
            safe: Whether to send as safe message
            agent_id: Agent ID
            
        Returns:
            Send result
        """
        data = {
            "msgtype": "text",
            "text": {"content": content},
            "safe": 1 if safe else 0
        }
        
        if to_user:
            data["touser"] = "|".join(to_user)
        if to_party:
            data["toparty"] = "|".join(to_party)
        if to_tag:
            data["totag"] = "|".join(to_tag)
        if agent_id:
            data["agentid"] = agent_id
            
        return self.client.post_json("message/send", json_data=data)
    
    def send_image(
        self,
        media_id: str,
        to_user: Optional[List[str]] = None,
        to_party: Optional[List[str]] = None,
        to_tag: Optional[List[str]] = None,
        safe: bool = False,
        agent_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send image message
        
        Args:
            media_id: Media ID
            to_user: List of user IDs
            to_party: List of department IDs
            to_tag: List of tag IDs
            safe: Whether to send as safe message
            agent_id: Agent ID
            
        Returns:
            Send result
        """
        data = {
            "msgtype": "image",
            "image": {"media_id": media_id},
            "safe": 1 if safe else 0
        }
        
        if to_user:
            data["touser"] = "|".join(to_user)
        if to_party:
            data["toparty"] = "|".join(to_party)
        if to_tag:
            data["totag"] = "|".join(to_tag)
        if agent_id:
            data["agentid"] = agent_id
            
        return self.client.post_json("message/send", json_data=data)
    
    def send_voice(
        self,
        media_id: str,
        to_user: Optional[List[str]] = None,
        to_party: Optional[List[str]] = None,
        to_tag: Optional[List[str]] = None,
        safe: bool = False,
        agent_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send voice message
        
        Args:
            media_id: Media ID
            to_user: List of user IDs
            to_party: List of department IDs
            to_tag: List of tag IDs
            safe: Whether to send as safe message
            agent_id: Agent ID
            
        Returns:
            Send result
        """
        data = {
            "msgtype": "voice",
            "voice": {"media_id": media_id},
            "safe": 1 if safe else 0
        }
        
        if to_user:
            data["touser"] = "|".join(to_user)
        if to_party:
            data["toparty"] = "|".join(to_party)
        if to_tag:
            data["totag"] = "|".join(to_tag)
        if agent_id:
            data["agentid"] = agent_id
            
        return self.client.post_json("message/send", json_data=data)
    
    def send_video(
        self,
        media_id: str,
        title: str,
        description: str,
        to_user: Optional[List[str]] = None,
        to_party: Optional[List[str]] = None,
        to_tag: Optional[List[str]] = None,
        safe: bool = False,
        agent_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send video message
        
        Args:
            media_id: Media ID
            title: Video title
            description: Video description
            to_user: List of user IDs
            to_party: List of department IDs
            to_tag: List of tag IDs
            safe: Whether to send as safe message
            agent_id: Agent ID
            
        Returns:
            Send result
        """
        data = {
            "msgtype": "video",
            "video": {
                "media_id": media_id,
                "title": title,
                "description": description
            },
            "safe": 1 if safe else 0
        }
        
        if to_user:
            data["touser"] = "|".join(to_user)
        if to_party:
            data["toparty"] = "|".join(to_party)
        if to_tag:
            data["totag"] = "|".join(to_tag)
        if agent_id:
            data["agentid"] = agent_id
            
        return self.client.post_json("message/send", json_data=data)
    
    def send_file(
        self,
        media_id: str,
        to_user: Optional[List[str]] = None,
        to_party: Optional[List[str]] = None,
        to_tag: Optional[List[str]] = None,
        safe: bool = False,
        agent_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send file message
        
        Args:
            media_id: Media ID
            to_user: List of user IDs
            to_party: List of department IDs
            to_tag: List of tag IDs
            safe: Whether to send as safe message
            agent_id: Agent ID
            
        Returns:
            Send result
        """
        data = {
            "msgtype": "file",
            "file": {"media_id": media_id},
            "safe": 1 if safe else 0
        }
        
        if to_user:
            data["touser"] = "|".join(to_user)
        if to_party:
            data["toparty"] = "|".join(to_party)
        if to_tag:
            data["totag"] = "|".join(to_tag)
        if agent_id:
            data["agentid"] = agent_id
            
        return self.client.post_json("message/send", json_data=data)
    
    def send_textcard(
        self,
        title: str,
        description: str,
        url: str,
        to_user: Optional[List[str]] = None,
        to_party: Optional[List[str]] = None,
        to_tag: Optional[List[str]] = None,
        safe: bool = False,
        agent_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send text card message
        
        Args:
            title: Card title
            description: Card description
            url: Card URL
            to_user: List of user IDs
            to_party: List of department IDs
            to_tag: List of tag IDs
            safe: Whether to send as safe message
            agent_id: Agent ID
            
        Returns:
            Send result
        """
        data = {
            "msgtype": "textcard",
            "textcard": {
                "title": title,
                "description": description,
                "url": url
            },
            "safe": 1 if safe else 0
        }
        
        if to_user:
            data["touser"] = "|".join(to_user)
        if to_party:
            data["toparty"] = "|".join(to_party)
        if to_tag:
            data["totag"] = "|".join(to_tag)
        if agent_id:
            data["agentid"] = agent_id
            
        return self.client.post_json("message/send", json_data=data)
    
    def send_news(
        self,
        articles: List[Dict[str, str]],
        to_user: Optional[List[str]] = None,
        to_party: Optional[List[str]] = None,
        to_tag: Optional[List[str]] = None,
        safe: bool = False,
        agent_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send news message
        
        Args:
            articles: List of articles
            to_user: List of user IDs
            to_party: List of department IDs
            to_tag: List of tag IDs
            safe: Whether to send as safe message
            agent_id: Agent ID
            
        Returns:
            Send result
        """
        data = {
            "msgtype": "news",
            "news": {"articles": articles},
            "safe": 1 if safe else 0
        }
        
        if to_user:
            data["touser"] = "|".join(to_user)
        if to_party:
            data["toparty"] = "|".join(to_party)
        if to_tag:
            data["totag"] = "|".join(to_tag)
        if agent_id:
            data["agentid"] = agent_id
            
        return self.client.post_json("message/send", json_data=data)
    
    def send_mpnews(
        self,
        articles: List[Dict[str, Any]],
        to_user: Optional[List[str]] = None,
        to_party: Optional[List[str]] = None,
        to_tag: Optional[List[str]] = None,
        safe: bool = False,
        agent_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send MP news message
        
        Args:
            articles: List of articles
            to_user: List of user IDs
            to_party: List of department IDs
            to_tag: List of tag IDs
            safe: Whether to send as safe message
            agent_id: Agent ID
            
        Returns:
            Send result
        """
        data = {
            "msgtype": "mpnews",
            "mpnews": {"articles": articles},
            "safe": 1 if safe else 0
        }
        
        if to_user:
            data["touser"] = "|".join(to_user)
        if to_party:
            data["toparty"] = "|".join(to_party)
        if to_tag:
            data["totag"] = "|".join(to_tag)
        if agent_id:
            data["agentid"] = agent_id
            
        return self.client.post_json("message/send", json_data=data)
    
    def send_markdown(
        self,
        content: str,
        to_user: Optional[List[str]] = None,
        to_party: Optional[List[str]] = None,
        to_tag: Optional[List[str]] = None,
        safe: bool = False,
        agent_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send markdown message
        
        Args:
            content: Markdown content
            to_user: List of user IDs
            to_party: List of department IDs
            to_tag: List of tag IDs
            safe: Whether to send as safe message
            agent_id: Agent ID
            
        Returns:
            Send result
        """
        data = {
            "msgtype": "markdown",
            "markdown": {"content": content},
            "safe": 1 if safe else 0
        }
        
        if to_user:
            data["touser"] = "|".join(to_user)
        if to_party:
            data["toparty"] = "|".join(to_party)
        if to_tag:
            data["totag"] = "|".join(to_tag)
        if agent_id:
            data["agentid"] = agent_id
            
        return self.client.post_json("message/send", json_data=data) 