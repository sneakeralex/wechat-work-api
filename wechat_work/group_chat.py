from typing import Dict, Any, List, Optional
from .client import WeChatWorkClient

class GroupChatAPI:
    """Group Chat API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def create(
        self,
        name: str,
        owner: str,
        chat_id: Optional[str] = None,
        user_list: Optional[List[str]] = None,
        group_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create group chat
        
        Args:
            name: Group name
            owner: Owner user ID
            chat_id: Chat ID
            user_list: List of user IDs
            group_id: Group ID
            
        Returns:
            Created group chat info
        """
        data = {
            "name": name,
            "owner": owner
        }
        
        if chat_id is not None:
            data["chatid"] = chat_id
        if user_list is not None:
            data["userlist"] = user_list
        if group_id is not None:
            data["groupid"] = group_id
            
        return self.client.post_json("appchat/create", json_data=data)
    
    def update(
        self,
        chat_id: str,
        name: Optional[str] = None,
        owner: Optional[str] = None,
        add_user_list: Optional[List[str]] = None,
        del_user_list: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Update group chat
        
        Args:
            chat_id: Chat ID
            name: New group name
            owner: New owner user ID
            add_user_list: List of user IDs to add
            del_user_list: List of user IDs to remove
            
        Returns:
            Update result
        """
        data = {"chatid": chat_id}
        
        if name is not None:
            data["name"] = name
        if owner is not None:
            data["owner"] = owner
        if add_user_list is not None:
            data["add_user_list"] = add_user_list
        if del_user_list is not None:
            data["del_user_list"] = del_user_list
            
        return self.client.post_json("appchat/update", json_data=data)
    
    def get(self, chat_id: str) -> Dict[str, Any]:
        """
        Get group chat detail
        
        Args:
            chat_id: Chat ID
            
        Returns:
            Group chat detail
        """
        return self.client.get("appchat/get", params={"chatid": chat_id})
    
    def send_text(
        self,
        chat_id: str,
        content: str,
        safe: bool = False
    ) -> Dict[str, Any]:
        """
        Send text message to group chat
        
        Args:
            chat_id: Chat ID
            content: Message content
            safe: Whether to send as safe message
            
        Returns:
            Send result
        """
        data = {
            "chatid": chat_id,
            "msgtype": "text",
            "text": {"content": content},
            "safe": 1 if safe else 0
        }
        return self.client.post_json("appchat/send", json_data=data)
    
    def send_image(
        self,
        chat_id: str,
        media_id: str,
        safe: bool = False
    ) -> Dict[str, Any]:
        """
        Send image message to group chat
        
        Args:
            chat_id: Chat ID
            media_id: Media ID
            safe: Whether to send as safe message
            
        Returns:
            Send result
        """
        data = {
            "chatid": chat_id,
            "msgtype": "image",
            "image": {"media_id": media_id},
            "safe": 1 if safe else 0
        }
        return self.client.post_json("appchat/send", json_data=data)
    
    def send_voice(
        self,
        chat_id: str,
        media_id: str,
        safe: bool = False
    ) -> Dict[str, Any]:
        """
        Send voice message to group chat
        
        Args:
            chat_id: Chat ID
            media_id: Media ID
            safe: Whether to send as safe message
            
        Returns:
            Send result
        """
        data = {
            "chatid": chat_id,
            "msgtype": "voice",
            "voice": {"media_id": media_id},
            "safe": 1 if safe else 0
        }
        return self.client.post_json("appchat/send", json_data=data)
    
    def send_video(
        self,
        chat_id: str,
        media_id: str,
        title: str,
        description: str,
        safe: bool = False
    ) -> Dict[str, Any]:
        """
        Send video message to group chat
        
        Args:
            chat_id: Chat ID
            media_id: Media ID
            title: Video title
            description: Video description
            safe: Whether to send as safe message
            
        Returns:
            Send result
        """
        data = {
            "chatid": chat_id,
            "msgtype": "video",
            "video": {
                "media_id": media_id,
                "title": title,
                "description": description
            },
            "safe": 1 if safe else 0
        }
        return self.client.post_json("appchat/send", json_data=data)
    
    def send_file(
        self,
        chat_id: str,
        media_id: str,
        safe: bool = False
    ) -> Dict[str, Any]:
        """
        Send file message to group chat
        
        Args:
            chat_id: Chat ID
            media_id: Media ID
            safe: Whether to send as safe message
            
        Returns:
            Send result
        """
        data = {
            "chatid": chat_id,
            "msgtype": "file",
            "file": {"media_id": media_id},
            "safe": 1 if safe else 0
        }
        return self.client.post_json("appchat/send", json_data=data)
    
    def send_textcard(
        self,
        chat_id: str,
        title: str,
        description: str,
        url: str,
        safe: bool = False
    ) -> Dict[str, Any]:
        """
        Send text card message to group chat
        
        Args:
            chat_id: Chat ID
            title: Card title
            description: Card description
            url: Card URL
            safe: Whether to send as safe message
            
        Returns:
            Send result
        """
        data = {
            "chatid": chat_id,
            "msgtype": "textcard",
            "textcard": {
                "title": title,
                "description": description,
                "url": url
            },
            "safe": 1 if safe else 0
        }
        return self.client.post_json("appchat/send", json_data=data)
    
    def send_news(
        self,
        chat_id: str,
        articles: List[Dict[str, str]],
        safe: bool = False
    ) -> Dict[str, Any]:
        """
        Send news message to group chat
        
        Args:
            chat_id: Chat ID
            articles: List of articles
            safe: Whether to send as safe message
            
        Returns:
            Send result
        """
        data = {
            "chatid": chat_id,
            "msgtype": "news",
            "news": {"articles": articles},
            "safe": 1 if safe else 0
        }
        return self.client.post_json("appchat/send", json_data=data)
    
    def send_mpnews(
        self,
        chat_id: str,
        articles: List[Dict[str, Any]],
        safe: bool = False
    ) -> Dict[str, Any]:
        """
        Send MP news message to group chat
        
        Args:
            chat_id: Chat ID
            articles: List of articles
            safe: Whether to send as safe message
            
        Returns:
            Send result
        """
        data = {
            "chatid": chat_id,
            "msgtype": "mpnews",
            "mpnews": {"articles": articles},
            "safe": 1 if safe else 0
        }
        return self.client.post_json("appchat/send", json_data=data)
    
    def send_markdown(
        self,
        chat_id: str,
        content: str,
        safe: bool = False
    ) -> Dict[str, Any]:
        """
        Send markdown message to group chat
        
        Args:
            chat_id: Chat ID
            content: Markdown content
            safe: Whether to send as safe message
            
        Returns:
            Send result
        """
        data = {
            "chatid": chat_id,
            "msgtype": "markdown",
            "markdown": {"content": content},
            "safe": 1 if safe else 0
        }
        return self.client.post_json("appchat/send", json_data=data) 