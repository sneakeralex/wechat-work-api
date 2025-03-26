from typing import Dict, Any, List, Optional
from .base import BaseClient
from .exceptions import WeChatAPIError

class AgentClient(BaseClient):
    """企业微信应用管理 API 客户端"""
    
    def __init__(self, corp_id: str, corp_secret: str):
        super().__init__(corp_id, corp_secret)
        
    def get_agent(self, agentid: int) -> Dict[str, Any]:
        """
        获取应用
        
        Args:
            agentid: 应用id
            
        Returns:
            Dict[str, Any]: 应用信息
        """
        url = f"{self.base_url}/cgi-bin/agent/get"
        params = {
            "access_token": self.get_access_token(),
            "agentid": agentid
        }
        
        response = self._get(url, params=params)
        return response
        
    def set_agent(self, agentid: int, **kwargs) -> bool:
        """
        设置应用
        
        Args:
            agentid: 应用id
            **kwargs: 要设置的字段
            
        Returns:
            bool: 是否成功
        """
        url = f"{self.base_url}/cgi-bin/agent/set"
        params = {"access_token": self.get_access_token()}
        data = {"agentid": agentid, **kwargs}
        
        response = self._post(url, data=data)
        return response.get("errcode") == 0
        
    def get_agent_list(self) -> List[Dict[str, Any]]:
        """
        获取应用列表
        
        Returns:
            List[Dict[str, Any]]: 应用列表
        """
        url = f"{self.base_url}/cgi-bin/agent/list"
        params = {"access_token": self.get_access_token()}
        
        response = self._get(url, params=params)
        return response.get("agentlist", [])
        
    def set_agent_scope(self, agentid: int, allow_user: Optional[List[str]] = None, allow_party: Optional[List[int]] = None, allow_tag: Optional[List[int]] = None) -> bool:
        """
        设置应用可见范围
        
        Args:
            agentid: 应用id
            allow_user: 可见的用户列表
            allow_party: 可见的部门列表
            allow_tag: 可见的标签列表
            
        Returns:
            bool: 是否成功
        """
        url = f"{self.base_url}/cgi-bin/agent/set_scope"
        params = {"access_token": self.get_access_token()}
        data = {"agentid": agentid}
        
        if allow_user is not None:
            data["allow_user"] = allow_user
        if allow_party is not None:
            data["allow_party"] = allow_party
        if allow_tag is not None:
            data["allow_tag"] = allow_tag
            
        response = self._post(url, data=data)
        return response.get("errcode") == 0
        
    def get_agent_scope(self, agentid: int) -> Dict[str, Any]:
        """
        获取应用可见范围
        
        Args:
            agentid: 应用id
            
        Returns:
            Dict[str, Any]: 可见范围信息
        """
        url = f"{self.base_url}/cgi-bin/agent/get_scope"
        params = {
            "access_token": self.get_access_token(),
            "agentid": agentid
        }
        
        response = self._get(url, params=params)
        return response
        
    def set_agent_workbench_template(self, agentid: int, type: str, **kwargs) -> bool:
        """
        设置应用工作台自定义展示
        
        Args:
            agentid: 应用id
            type: 展示类型
            **kwargs: 其他参数
            
        Returns:
            bool: 是否成功
        """
        url = f"{self.base_url}/cgi-bin/agent/set_workbench_template"
        params = {"access_token": self.get_access_token()}
        data = {
            "agentid": agentid,
            "type": type,
            **kwargs
        }
        
        response = self._post(url, data=data)
        return response.get("errcode") == 0
        
    def get_agent_workbench_template(self, agentid: int) -> Dict[str, Any]:
        """
        获取应用工作台自定义展示
        
        Args:
            agentid: 应用id
            
        Returns:
            Dict[str, Any]: 工作台展示信息
        """
        url = f"{self.base_url}/cgi-bin/agent/get_workbench_template"
        params = {
            "access_token": self.get_access_token(),
            "agentid": agentid
        }
        
        response = self._get(url, params=params)
        return response
        
    def set_agent_workbench_data(self, agentid: int, userid: str, **kwargs) -> bool:
        """
        设置应用工作台自定义展示数据
        
        Args:
            agentid: 应用id
            userid: 用户id
            **kwargs: 其他参数
            
        Returns:
            bool: 是否成功
        """
        url = f"{self.base_url}/cgi-bin/agent/set_workbench_data"
        params = {"access_token": self.get_access_token()}
        data = {
            "agentid": agentid,
            "userid": userid,
            **kwargs
        }
        
        response = self._post(url, data=data)
        return response.get("errcode") == 0 