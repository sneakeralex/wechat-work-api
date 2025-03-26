from typing import Dict, Any, List, Optional, Union
from .client import WeChatWorkClient

class UserAPI:
    """User Management API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def create(
        self,
        user_id: str,
        name: str,
        department_ids: List[int],
        mobile: Optional[str] = None,
        email: Optional[str] = None,
        avatar: Optional[str] = None,
        position: Optional[str] = None,
        gender: Optional[int] = None,
        enable: bool = True,
        ext_attr: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a user
        
        Args:
            user_id: User ID
            name: User name
            department_ids: List of department IDs
            mobile: Mobile number
            email: Email address
            avatar: Avatar URL
            position: Position
            gender: Gender (0: unknown, 1: male, 2: female)
            enable: Whether to enable the user
            ext_attr: Extended attributes
            
        Returns:
            Created user info
        """
        data = {
            "userid": user_id,
            "name": name,
            "department": department_ids
        }
        
        if mobile is not None:
            data["mobile"] = mobile
        if email is not None:
            data["email"] = email
        if avatar is not None:
            data["avatar"] = avatar
        if position is not None:
            data["position"] = position
        if gender is not None:
            data["gender"] = gender
        if ext_attr is not None:
            data["extattr"] = ext_attr
            
        data["enable"] = 1 if enable else 0
        
        return self.client.post_json("user/create", json_data=data)
    
    def update(
        self,
        user_id: str,
        name: Optional[str] = None,
        department_ids: Optional[List[int]] = None,
        mobile: Optional[str] = None,
        email: Optional[str] = None,
        avatar: Optional[str] = None,
        position: Optional[str] = None,
        gender: Optional[int] = None,
        enable: Optional[bool] = None,
        ext_attr: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Update a user
        
        Args:
            user_id: User ID
            name: New name
            department_ids: New department IDs
            mobile: New mobile number
            email: New email address
            avatar: New avatar URL
            position: New position
            gender: New gender
            enable: Whether to enable the user
            ext_attr: New extended attributes
            
        Returns:
            Update result
        """
        data = {"userid": user_id}
        
        if name is not None:
            data["name"] = name
        if department_ids is not None:
            data["department"] = department_ids
        if mobile is not None:
            data["mobile"] = mobile
        if email is not None:
            data["email"] = email
        if avatar is not None:
            data["avatar"] = avatar
        if position is not None:
            data["position"] = position
        if gender is not None:
            data["gender"] = gender
        if ext_attr is not None:
            data["extattr"] = ext_attr
        if enable is not None:
            data["enable"] = 1 if enable else 0
            
        return self.client.post_json("user/update", json_data=data)
    
    def delete(self, user_id: str) -> Dict[str, Any]:
        """
        Delete a user
        
        Args:
            user_id: User ID
            
        Returns:
            Delete result
        """
        return self.client.get("user/delete", params={"userid": user_id})
    
    def get(self, user_id: str) -> Dict[str, Any]:
        """
        Get user detail
        
        Args:
            user_id: User ID
            
        Returns:
            User detail
        """
        return self.client.get("user/get", params={"userid": user_id})
    
    def list_by_department(self, department_id: int, fetch_child: bool = False) -> List[Dict[str, Any]]:
        """
        Get users in a department
        
        Args:
            department_id: Department ID
            fetch_child: Whether to fetch users in child departments
            
        Returns:
            List of users
        """
        params = {
            "department_id": department_id,
            "fetch_child": 1 if fetch_child else 0
        }
        return self.client.get("user/list", params=params)["userlist"]
    
    def convert_to_openid(self, user_id: str) -> Dict[str, Any]:
        """
        Convert user ID to open ID
        
        Args:
            user_id: User ID
            
        Returns:
            Open ID info
        """
        return self.client.post_json("user/convert_to_openid", json_data={"userid": user_id})
    
    def convert_to_userid(self, open_id: str) -> Dict[str, Any]:
        """
        Convert open ID to user ID
        
        Args:
            open_id: Open ID
            
        Returns:
            User ID info
        """
        return self.client.post_json("user/convert_to_userid", json_data={"openid": open_id})
    
    def auth_success(self, user_id: str) -> Dict[str, Any]:
        """
        Set user authentication success
        
        Args:
            user_id: User ID
            
        Returns:
            Operation result
        """
        return self.client.get("user/authsucc", params={"userid": user_id}) 