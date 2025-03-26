from typing import Dict, Any, List, Optional
from .client import WeChatWorkClient

class AgentAPI:
    """Agent Management API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def get(self, agent_id: str) -> Dict[str, Any]:
        """
        Get agent detail
        
        Args:
            agent_id: Agent ID
            
        Returns:
            Agent detail
        """
        return self.client.get("agent/get", params={"agentid": agent_id})
    
    def set(
        self,
        agent_id: str,
        name: str,
        description: Optional[str] = None,
        redirect_domain: Optional[str] = None,
        is_report_enter: Optional[bool] = None,
        is_report_user_location: Optional[bool] = None,
        logo_media_id: Optional[str] = None,
        home_url: Optional[str] = None,
        report_location_flag: Optional[int] = None,
        report_enter_flag: Optional[int] = None,
        app_type: Optional[int] = None,
        custom_pid: Optional[str] = None,
        close: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Set agent info
        
        Args:
            agent_id: Agent ID
            name: Agent name
            description: Agent description
            redirect_domain: Redirect domain
            is_report_enter: Whether to report enter event
            is_report_user_location: Whether to report user location
            logo_media_id: Logo media ID
            home_url: Home URL
            report_location_flag: Report location flag
            report_enter_flag: Report enter flag
            app_type: App type
            custom_pid: Custom PID
            close: Whether to close the agent
            
        Returns:
            Operation result
        """
        data = {
            "agentid": agent_id,
            "name": name
        }
        
        if description is not None:
            data["description"] = description
        if redirect_domain is not None:
            data["redirect_domain"] = redirect_domain
        if is_report_enter is not None:
            data["isreportenter"] = 1 if is_report_enter else 0
        if is_report_user_location is not None:
            data["isreportuserlocation"] = 1 if is_report_user_location else 0
        if logo_media_id is not None:
            data["logo_mediaid"] = logo_media_id
        if home_url is not None:
            data["home_url"] = home_url
        if report_location_flag is not None:
            data["report_location_flag"] = report_location_flag
        if report_enter_flag is not None:
            data["report_enter_flag"] = report_enter_flag
        if app_type is not None:
            data["app_type"] = app_type
        if custom_pid is not None:
            data["custom_pid"] = custom_pid
        if close is not None:
            data["close"] = close
            
        return self.client.post_json("agent/set", json_data=data)
    
    def list(self) -> List[Dict[str, Any]]:
        """
        Get agent list
        
        Returns:
            List of agents
        """
        return self.client.get("agent/list")["agentlist"]
    
    def set_workbench_template(
        self,
        agent_id: str,
        template_type: str,
        key_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Set workbench template
        
        Args:
            agent_id: Agent ID
            template_type: Template type
            key_data: Key data
            
        Returns:
            Operation result
        """
        return self.client.post_json("agent/set_workbench_template", json_data={
            "agentid": agent_id,
            "type": template_type,
            "key": key_data
        })
    
    def get_workbench_template(self, agent_id: str) -> Dict[str, Any]:
        """
        Get workbench template
        
        Args:
            agent_id: Agent ID
            
        Returns:
            Template info
        """
        return self.client.get("agent/get_workbench_template", params={"agentid": agent_id})
    
    def set_workbench_data(
        self,
        agent_id: str,
        user_id: str,
        template_type: str,
        key_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Set workbench data
        
        Args:
            agent_id: Agent ID
            user_id: User ID
            template_type: Template type
            key_data: Key data
            
        Returns:
            Operation result
        """
        return self.client.post_json("agent/set_workbench_data", json_data={
            "agentid": agent_id,
            "userid": user_id,
            "type": template_type,
            "key": key_data
        }) 