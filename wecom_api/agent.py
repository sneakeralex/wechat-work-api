from typing import Dict, List, Any, Optional
from .base import WecomBaseClient

class AgentClient(WecomBaseClient):
    """应用管理客户端"""
    
    def get_agent_list(self) -> Dict[str, Any]:
        """获取应用列表"""
        return self._get("agent/list")
    
    def get_agent(self, agentid: str) -> Dict[str, Any]:
        """获取应用"""
        return self._get("agent/get", params={"agentid": agentid})
    
    def set_agent(self, 
                 agentid: str,
                 name: Optional[str] = None,
                 description: Optional[str] = None,
                 redirect_domain: Optional[str] = None,
                 isreportenter: Optional[int] = None,
                 home_url: Optional[str] = None,
                 report_location_flag: Optional[int] = None,
                 logo_mediaid: Optional[str] = None) -> Dict[str, Any]:
        """设置应用"""
        data = {"agentid": agentid}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if redirect_domain is not None:
            data["redirect_domain"] = redirect_domain
        if isreportenter is not None:
            data["isreportenter"] = isreportenter
        if home_url is not None:
            data["home_url"] = home_url
        if report_location_flag is not None:
            data["report_location_flag"] = report_location_flag
        if logo_mediaid is not None:
            data["logo_mediaid"] = logo_mediaid
        return self._post("agent/set", json=data)
    
    def set_agent_scope(self,
                       agentid: str,
                       allow_user: Optional[List[str]] = None,
                       allow_party: Optional[List[int]] = None,
                       allow_tag: Optional[List[int]] = None) -> Dict[str, Any]:
        """设置应用可见范围"""
        data = {"agentid": agentid}
        if allow_user is not None:
            data["allow_user"] = allow_user
        if allow_party is not None:
            data["allow_party"] = allow_party
        if allow_tag is not None:
            data["allow_tag"] = allow_tag
        return self._post("agent/set_scope", json=data)
    
    def get_agent_scope(self, agentid: str) -> Dict[str, Any]:
        """获取应用可见范围"""
        return self._get("agent/get_scope", params={"agentid": agentid})
    
    def set_agent_workbench_template(self,
                                   agentid: str,
                                   type: str,
                                   keydata: Dict[str, Any]) -> Dict[str, Any]:
        """设置应用工作台自定义展示"""
        data = {
            "agentid": agentid,
            "type": type,
            "keydata": keydata
        }
        return self._post("agent/set_workbench_template", json=data)
    
    def get_agent_workbench_template(self, agentid: str) -> Dict[str, Any]:
        """获取应用工作台自定义展示"""
        return self._get("agent/get_workbench_template", params={"agentid": agentid})
    
    def set_agent_workbench_data(self,
                               agentid: str,
                               userid: str,
                               keydata: Dict[str, Any]) -> Dict[str, Any]:
        """设置应用工作台自定义展示数据"""
        data = {
            "agentid": agentid,
            "userid": userid,
            "keydata": keydata
        }
        return self._post("agent/set_workbench_data", json=data) 