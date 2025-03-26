from typing import Dict, Any, List, Optional
from .client import WeChatWorkClient

class TagAPI:
    """Tag Management API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def create(self, tag_name: str) -> Dict[str, Any]:
        """
        Create a tag
        
        Args:
            tag_name: Tag name
            
        Returns:
            Created tag info
        """
        return self.client.post_json("tag/create", json_data={"tagname": tag_name})
    
    def update(self, tag_id: int, tag_name: str) -> Dict[str, Any]:
        """
        Update a tag
        
        Args:
            tag_id: Tag ID
            tag_name: New tag name
            
        Returns:
            Update result
        """
        return self.client.post_json("tag/update", json_data={
            "tagid": tag_id,
            "tagname": tag_name
        })
    
    def delete(self, tag_id: int) -> Dict[str, Any]:
        """
        Delete a tag
        
        Args:
            tag_id: Tag ID
            
        Returns:
            Delete result
        """
        return self.client.get("tag/delete", params={"tagid": tag_id})
    
    def get(self, tag_id: int) -> Dict[str, Any]:
        """
        Get tag detail
        
        Args:
            tag_id: Tag ID
            
        Returns:
            Tag detail
        """
        return self.client.get("tag/get", params={"tagid": tag_id})
    
    def list(self) -> List[Dict[str, Any]]:
        """
        Get tag list
        
        Returns:
            List of tags
        """
        return self.client.get("tag/list")["taglist"]
    
    def add_users(self, tag_id: int, user_ids: List[str]) -> Dict[str, Any]:
        """
        Add users to tag
        
        Args:
            tag_id: Tag ID
            user_ids: List of user IDs
            
        Returns:
            Operation result
        """
        return self.client.post_json("tag/addtagusers", json_data={
            "tagid": tag_id,
            "userlist": user_ids
        })
    
    def remove_users(self, tag_id: int, user_ids: List[str]) -> Dict[str, Any]:
        """
        Remove users from tag
        
        Args:
            tag_id: Tag ID
            user_ids: List of user IDs
            
        Returns:
            Operation result
        """
        return self.client.post_json("tag/deltagusers", json_data={
            "tagid": tag_id,
            "userlist": user_ids
        }) 