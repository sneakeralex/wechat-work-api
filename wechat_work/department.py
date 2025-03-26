from typing import Dict, Any, List, Optional
from .client import WeChatWorkClient

class DepartmentAPI:
    """Department Management API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def create(self, name: str, parent_id: int = 1, order: Optional[int] = None) -> Dict[str, Any]:
        """
        Create a department
        
        Args:
            name: Department name
            parent_id: Parent department ID (default: 1)
            order: Display order
            
        Returns:
            Created department info
        """
        data = {
            "name": name,
            "parentid": parent_id
        }
        if order is not None:
            data["order"] = order
            
        return self.client.post_json("department/create", json_data=data)
    
    def update(
        self,
        id: int,
        name: Optional[str] = None,
        parent_id: Optional[int] = None,
        order: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Update a department
        
        Args:
            id: Department ID
            name: New department name
            parent_id: New parent department ID
            order: New display order
            
        Returns:
            Update result
        """
        data = {"id": id}
        if name is not None:
            data["name"] = name
        if parent_id is not None:
            data["parentid"] = parent_id
        if order is not None:
            data["order"] = order
            
        return self.client.post_json("department/update", json_data=data)
    
    def delete(self, id: int) -> Dict[str, Any]:
        """
        Delete a department
        
        Args:
            id: Department ID
            
        Returns:
            Delete result
        """
        return self.client.get("department/delete", params={"id": id})
    
    def list(self) -> List[Dict[str, Any]]:
        """
        Get department list
        
        Returns:
            List of departments
        """
        return self.client.get("department/list")["department"]
    
    def get(self, id: int) -> Dict[str, Any]:
        """
        Get department detail
        
        Args:
            id: Department ID
            
        Returns:
            Department detail
        """
        return self.client.get("department/get", params={"id": id}) 