from typing import Dict, Any, List, Optional
from .client import WeChatWorkClient

class MenuAPI:
    """Menu Management API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def create(self, agent_id: str, button: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create menu
        
        Args:
            agent_id: Agent ID
            button: Menu buttons
            
        Returns:
            Operation result
        """
        return self.client.post_json("menu/create", json_data={
            "agentid": agent_id,
            "button": button
        })
    
    def get(self, agent_id: str) -> Dict[str, Any]:
        """
        Get menu
        
        Args:
            agent_id: Agent ID
            
        Returns:
            Menu info
        """
        return self.client.get("menu/get", params={"agentid": agent_id})
    
    def delete(self, agent_id: str) -> Dict[str, Any]:
        """
        Delete menu
        
        Args:
            agent_id: Agent ID
            
        Returns:
            Operation result
        """
        return self.client.get("menu/delete", params={"agentid": agent_id}) 