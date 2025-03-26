from typing import Dict, Any, List, Optional
from .base import BaseClient
from .exceptions import WeChatAPIError

class ContactClient(BaseClient):
    """企业微信通讯录管理 API 客户端"""
    
    def __init__(self, corp_id: str, corp_secret: str):
        super().__init__(corp_id, corp_secret)
        
    def create_department(self, name: str, parentid: int, order: Optional[int] = None, id: Optional[int] = None) -> int:
        """
        创建部门
        
        Args:
            name: 部门名称
            parentid: 父部门id
            order: 排序值
            id: 部门id
            
        Returns:
            int: 部门id
        """
        url = f"{self.base_url}/cgi-bin/department/create"
        params = {"access_token": self.get_access_token()}
        data = {
            "name": name,
            "parentid": parentid
        }
        if order is not None:
            data["order"] = order
        if id is not None:
            data["id"] = id
            
        response = self._post(url, data=data)
        return response.get("id")
        
    def update_department(self, id: int, name: Optional[str] = None, parentid: Optional[int] = None, order: Optional[int] = None) -> bool:
        """
        更新部门
        
        Args:
            id: 部门id
            name: 部门名称
            parentid: 父部门id
            order: 排序值
            
        Returns:
            bool: 是否成功
        """
        url = f"{self.base_url}/cgi-bin/department/update"
        params = {"access_token": self.get_access_token()}
        data = {"id": id}
        if name is not None:
            data["name"] = name
        if parentid is not None:
            data["parentid"] = parentid
        if order is not None:
            data["order"] = order
            
        response = self._post(url, data=data)
        return response.get("errcode") == 0
        
    def delete_department(self, id: int) -> bool:
        """
        删除部门
        
        Args:
            id: 部门id
            
        Returns:
            bool: 是否成功
        """
        url = f"{self.base_url}/cgi-bin/department/delete"
        params = {
            "access_token": self.get_access_token(),
            "id": id
        }
        
        response = self._get(url, params=params)
        return response.get("errcode") == 0
        
    def get_department_list(self) -> List[Dict[str, Any]]:
        """
        获取部门列表
        
        Returns:
            List[Dict[str, Any]]: 部门列表
        """
        url = f"{self.base_url}/cgi-bin/department/list"
        params = {"access_token": self.get_access_token()}
        
        response = self._get(url, params=params)
        return response.get("department", [])
        
    def create_user(self, userid: str, name: str, department: List[int], **kwargs) -> bool:
        """
        创建成员
        
        Args:
            userid: 成员UserID
            name: 成员名称
            department: 成员所属部门id列表
            **kwargs: 其他可选参数
            
        Returns:
            bool: 是否成功
        """
        url = f"{self.base_url}/cgi-bin/user/create"
        params = {"access_token": self.get_access_token()}
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            **kwargs
        }
        
        response = self._post(url, data=data)
        return response.get("errcode") == 0
        
    def update_user(self, userid: str, **kwargs) -> bool:
        """
        更新成员
        
        Args:
            userid: 成员UserID
            **kwargs: 要更新的字段
            
        Returns:
            bool: 是否成功
        """
        url = f"{self.base_url}/cgi-bin/user/update"
        params = {"access_token": self.get_access_token()}
        data = {"userid": userid, **kwargs}
        
        response = self._post(url, data=data)
        return response.get("errcode") == 0
        
    def delete_user(self, userid: str) -> bool:
        """
        删除成员
        
        Args:
            userid: 成员UserID
            
        Returns:
            bool: 是否成功
        """
        url = f"{self.base_url}/cgi-bin/user/delete"
        params = {
            "access_token": self.get_access_token(),
            "userid": userid
        }
        
        response = self._get(url, params=params)
        return response.get("errcode") == 0
        
    def get_user(self, userid: str) -> Dict[str, Any]:
        """
        读取成员
        
        Args:
            userid: 成员UserID
            
        Returns:
            Dict[str, Any]: 成员信息
        """
        url = f"{self.base_url}/cgi-bin/user/get"
        params = {
            "access_token": self.get_access_token(),
            "userid": userid
        }
        
        response = self._get(url, params=params)
        return response
        
    def get_department_users(self, department_id: int, fetch_child: int = 0) -> List[Dict[str, Any]]:
        """
        获取部门成员
        
        Args:
            department_id: 获取的部门id
            fetch_child: 是否递归获取子部门下面的成员
            
        Returns:
            List[Dict[str, Any]]: 成员列表
        """
        url = f"{self.base_url}/cgi-bin/user/simplelist"
        params = {
            "access_token": self.get_access_token(),
            "department_id": department_id,
            "fetch_child": fetch_child
        }
        
        response = self._get(url, params=params)
        return response.get("userlist", [])
        
    def get_department_users_detail(self, department_id: int, fetch_child: int = 0) -> List[Dict[str, Any]]:
        """
        获取部门成员详情
        
        Args:
            department_id: 获取的部门id
            fetch_child: 是否递归获取子部门下面的成员
            
        Returns:
            List[Dict[str, Any]]: 成员列表
        """
        url = f"{self.base_url}/cgi-bin/user/list"
        params = {
            "access_token": self.get_access_token(),
            "department_id": department_id,
            "fetch_child": fetch_child
        }
        
        response = self._get(url, params=params)
        return response.get("userlist", [])
        
    def convert_userid_to_openid(self, userid: str) -> str:
        """
        userid转openid
        
        Args:
            userid: 企业内的成员id
            
        Returns:
            str: openid
        """
        url = f"{self.base_url}/cgi-bin/user/convert_userid_to_openid"
        params = {"access_token": self.get_access_token()}
        data = {"userid": userid}
        
        response = self._post(url, data=data)
        return response.get("openid")
        
    def convert_openid_to_userid(self, openid: str) -> str:
        """
        openid转userid
        
        Args:
            openid: 在使用企业支付之后，返回结果的openid
            
        Returns:
            str: userid
        """
        url = f"{self.base_url}/cgi-bin/user/convert_openid_to_userid"
        params = {"access_token": self.get_access_token()}
        data = {"openid": openid}
        
        response = self._post(url, data=data)
        return response.get("userid")
        
    def get_user_info(self, code: str) -> Dict[str, Any]:
        """
        获取访问用户身份
        
        Args:
            code: 通过成员授权获取到的code
            
        Returns:
            Dict[str, Any]: 用户信息
        """
        url = f"{self.base_url}/cgi-bin/user/getuserinfo"
        params = {
            "access_token": self.get_access_token(),
            "code": code
        }
        
        response = self._get(url, params=params)
        return response
        
    def get_user_info_by_ticket(self, ticket: str) -> Dict[str, Any]:
        """
        获取访问用户身份
        
        Args:
            ticket: 成员授权获取到的code
            
        Returns:
            Dict[str, Any]: 用户信息
        """
        url = f"{self.base_url}/cgi-bin/user/get_userinfo_by_ticket"
        params = {
            "access_token": self.get_access_token(),
            "ticket": ticket
        }
        
        response = self._get(url, params=params)
        return response 