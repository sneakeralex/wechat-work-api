from typing import Dict, Any, List, Optional
from .client import WeChatWorkClient

class ExternalContactAPI:
    """External Contact API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def list(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Get external contact list
        
        Args:
            user_id: User ID
            
        Returns:
            List of external contacts
        """
        return self.client.get("externalcontact/list", params={"userid": user_id})["external_userid"]
    
    def get(self, external_user_id: str) -> Dict[str, Any]:
        """
        Get external contact detail
        
        Args:
            external_user_id: External contact ID
            
        Returns:
            External contact detail
        """
        return self.client.get("externalcontact/get", params={"external_userid": external_user_id})
    
    def get_by_code(self, code: str) -> Dict[str, Any]:
        """
        Get external contact by code
        
        Args:
            code: Authorization code
            
        Returns:
            External contact info
        """
        return self.client.get("externalcontact/get_by_code", params={"code": code})
    
    def get_contact_way(
        self,
        config_id: str,
        contact_type: Optional[int] = None,
        scene: Optional[int] = None,
        style: Optional[int] = None,
        remark: Optional[str] = None,
        skip_verify: Optional[bool] = None,
        state: Optional[str] = None,
        user: Optional[List[str]] = None,
        party: Optional[List[int]] = None,
        qr_code: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get contact way
        
        Args:
            config_id: Config ID
            contact_type: Contact type
            scene: Scene
            style: Style
            remark: Remark
            skip_verify: Whether to skip verification
            state: State
            user: List of user IDs
            party: List of department IDs
            qr_code: QR code
            
        Returns:
            Contact way info
        """
        data = {"config_id": config_id}
        
        if contact_type is not None:
            data["contact_type"] = contact_type
        if scene is not None:
            data["scene"] = scene
        if style is not None:
            data["style"] = style
        if remark is not None:
            data["remark"] = remark
        if skip_verify is not None:
            data["skip_verify"] = 1 if skip_verify else 0
        if state is not None:
            data["state"] = state
        if user is not None:
            data["user"] = user
        if party is not None:
            data["party"] = party
        if qr_code is not None:
            data["qr_code"] = qr_code
            
        return self.client.post_json("externalcontact/get_contact_way", json_data=data)
    
    def create_contact_way(
        self,
        contact_type: int,
        scene: int,
        style: Optional[int] = None,
        remark: Optional[str] = None,
        skip_verify: Optional[bool] = None,
        state: Optional[str] = None,
        user: Optional[List[str]] = None,
        party: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        """
        Create contact way
        
        Args:
            contact_type: Contact type
            scene: Scene
            style: Style
            remark: Remark
            skip_verify: Whether to skip verification
            state: State
            user: List of user IDs
            party: List of department IDs
            
        Returns:
            Created contact way info
        """
        data = {
            "contact_type": contact_type,
            "scene": scene
        }
        
        if style is not None:
            data["style"] = style
        if remark is not None:
            data["remark"] = remark
        if skip_verify is not None:
            data["skip_verify"] = 1 if skip_verify else 0
        if state is not None:
            data["state"] = state
        if user is not None:
            data["user"] = user
        if party is not None:
            data["party"] = party
            
        return self.client.post_json("externalcontact/add_contact_way", json_data=data)
    
    def update_contact_way(
        self,
        config_id: str,
        contact_type: Optional[int] = None,
        scene: Optional[int] = None,
        style: Optional[int] = None,
        remark: Optional[str] = None,
        skip_verify: Optional[bool] = None,
        state: Optional[str] = None,
        user: Optional[List[str]] = None,
        party: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        """
        Update contact way
        
        Args:
            config_id: Config ID
            contact_type: Contact type
            scene: Scene
            style: Style
            remark: Remark
            skip_verify: Whether to skip verification
            state: State
            user: List of user IDs
            party: List of department IDs
            
        Returns:
            Update result
        """
        data = {"config_id": config_id}
        
        if contact_type is not None:
            data["contact_type"] = contact_type
        if scene is not None:
            data["scene"] = scene
        if style is not None:
            data["style"] = style
        if remark is not None:
            data["remark"] = remark
        if skip_verify is not None:
            data["skip_verify"] = 1 if skip_verify else 0
        if state is not None:
            data["state"] = state
        if user is not None:
            data["user"] = user
        if party is not None:
            data["party"] = party
            
        return self.client.post_json("externalcontact/update_contact_way", json_data=data)
    
    def delete_contact_way(self, config_id: str) -> Dict[str, Any]:
        """
        Delete contact way
        
        Args:
            config_id: Config ID
            
        Returns:
            Delete result
        """
        return self.client.post_json("externalcontact/del_contact_way", json_data={"config_id": config_id})
    
    def get_corp_tag_list(self, tag_id: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Get corp tag list
        
        Args:
            tag_id: List of tag IDs
            
        Returns:
            Tag list
        """
        data = {}
        if tag_id is not None:
            data["tag_id"] = tag_id
        return self.client.post_json("externalcontact/get_corp_tag_list", json_data=data)
    
    def add_corp_tag(
        self,
        group_id: Optional[str] = None,
        group_name: Optional[str] = None,
        tag: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """
        Add corp tag
        
        Args:
            group_id: Group ID
            group_name: Group name
            tag: List of tags
            
        Returns:
            Added tag info
        """
        data = {}
        if group_id is not None:
            data["group_id"] = group_id
        if group_name is not None:
            data["group_name"] = group_name
        if tag is not None:
            data["tag"] = tag
        return self.client.post_json("externalcontact/add_corp_tag", json_data=data)
    
    def edit_corp_tag(
        self,
        id: str,
        name: Optional[str] = None,
        order: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Edit corp tag
        
        Args:
            id: Tag ID
            name: Tag name
            order: Display order
            
        Returns:
            Edit result
        """
        data = {"id": id}
        if name is not None:
            data["name"] = name
        if order is not None:
            data["order"] = order
        return self.client.post_json("externalcontact/edit_corp_tag", json_data=data)
    
    def delete_corp_tag(
        self,
        tag_id: List[str],
        group_id: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Delete corp tag
        
        Args:
            tag_id: List of tag IDs
            group_id: List of group IDs
            
        Returns:
            Delete result
        """
        data = {"tag_id": tag_id}
        if group_id is not None:
            data["group_id"] = group_id
        return self.client.post_json("externalcontact/del_corp_tag", json_data=data)
    
    def mark_tag(
        self,
        user_id: str,
        external_user_id: str,
        add_tag: Optional[List[str]] = None,
        remove_tag: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Mark tag for external contact
        
        Args:
            user_id: User ID
            external_user_id: External contact ID
            add_tag: List of tag IDs to add
            remove_tag: List of tag IDs to remove
            
        Returns:
            Operation result
        """
        data = {
            "userid": user_id,
            "external_userid": external_user_id
        }
        if add_tag is not None:
            data["add_tag"] = add_tag
        if remove_tag is not None:
            data["remove_tag"] = remove_tag
        return self.client.post_json("externalcontact/mark_tag", json_data=data) 