from typing import Dict, List, Any, Optional
from .base import WecomBaseClient

class ContactClient(WecomBaseClient):
    """通讯录管理客户端"""
    
    def create_department(self, name: str, parentid: int, order: Optional[int] = None) -> Dict[str, Any]:
        """创建部门"""
        data = {
            "name": name,
            "parentid": parentid
        }
        if order is not None:
            data["order"] = order
        return self._post("department/create", json=data)
    
    def update_department(self, id: int, name: Optional[str] = None, parentid: Optional[int] = None, order: Optional[int] = None) -> Dict[str, Any]:
        """更新部门"""
        data = {"id": id}
        if name is not None:
            data["name"] = name
        if parentid is not None:
            data["parentid"] = parentid
        if order is not None:
            data["order"] = order
        return self._post("department/update", json=data)
    
    def delete_department(self, id: int) -> Dict[str, Any]:
        """删除部门"""
        return self._get("department/delete", params={"id": id})
    
    def get_department_list(self) -> Dict[str, Any]:
        """获取部门列表"""
        return self._get("department/list")
    
    def create_user(self, 
                   userid: str,
                   name: str,
                   department: List[int],
                   mobile: Optional[str] = None,
                   email: Optional[str] = None,
                   avatar: Optional[str] = None,
                   telephone: Optional[str] = None,
                   english_name: Optional[str] = None,
                   extattr: Optional[Dict[str, Any]] = None,
                   to_invite: bool = True,
                   direct_leader: Optional[List[str]] = None) -> Dict[str, Any]:
        """创建成员"""
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "to_invite": to_invite
        }
        if mobile:
            data["mobile"] = mobile
        if email:
            data["email"] = email
        if avatar:
            data["avatar"] = avatar
        if telephone:
            data["telephone"] = telephone
        if english_name:
            data["english_name"] = english_name
        if extattr:
            data["extattr"] = extattr
        if direct_leader:
            data["direct_leader"] = direct_leader
        return self._post("user/create", json=data)
    
    def update_user(self,
                   userid: str,
                   name: Optional[str] = None,
                   department: Optional[List[int]] = None,
                   mobile: Optional[str] = None,
                   email: Optional[str] = None,
                   avatar: Optional[str] = None,
                   telephone: Optional[str] = None,
                   english_name: Optional[str] = None,
                   extattr: Optional[Dict[str, Any]] = None,
                   direct_leader: Optional[List[str]] = None) -> Dict[str, Any]:
        """更新成员"""
        data = {"userid": userid}
        if name is not None:
            data["name"] = name
        if department is not None:
            data["department"] = department
        if mobile is not None:
            data["mobile"] = mobile
        if email is not None:
            data["email"] = email
        if avatar is not None:
            data["avatar"] = avatar
        if telephone is not None:
            data["telephone"] = telephone
        if english_name is not None:
            data["english_name"] = english_name
        if extattr is not None:
            data["extattr"] = extattr
        if direct_leader is not None:
            data["direct_leader"] = direct_leader
        return self._post("user/update", json=data)
    
    def delete_user(self, userid: str) -> Dict[str, Any]:
        """删除成员"""
        return self._get("user/delete", params={"userid": userid})
    
    def get_user(self, userid: str) -> Dict[str, Any]:
        """获取成员"""
        return self._get("user/get", params={"userid": userid})
    
    def get_department_users(self, department_id: int, fetch_child: int = 0) -> Dict[str, Any]:
        """获取部门成员"""
        return self._get("user/simplelist", params={
            "department_id": department_id,
            "fetch_child": fetch_child
        })
    
    def get_department_users_detail(self, department_id: int, fetch_child: int = 0) -> Dict[str, Any]:
        """获取部门成员详情"""
        return self._get("user/list", params={
            "department_id": department_id,
            "fetch_child": fetch_child
        })
    
    def convert_userid_to_openid(self, userid: str) -> Dict[str, Any]:
        """userid 转 openid"""
        return self._post("user/convert_userid_to_openid", json={"userid": userid})
    
    def convert_openid_to_userid(self, openid: str) -> Dict[str, Any]:
        """openid 转 userid"""
        return self._post("user/convert_openid_to_userid", json={"openid": openid})
    
    def get_user_info(self, code: str) -> Dict[str, Any]:
        """获取用户信息"""
        return self._get("user/getuserinfo", params={"code": code}) 