from typing import Dict, Any, Optional, BinaryIO
from .base import BaseClient
from .exceptions import WeChatAPIError

class MediaClient(BaseClient):
    """企业微信媒体文件 API 客户端"""
    
    def __init__(self, corp_id: str, corp_secret: str):
        super().__init__(corp_id, corp_secret)
        
    def upload(self, media_type: str, media_file: BinaryIO) -> str:
        """
        上传临时素材
        
        Args:
            media_type: 媒体文件类型，分别有图片（image）、语音（voice）、视频（video），普通文件（file）
            media_file: 媒体文件对象
            
        Returns:
            str: 媒体文件id
        """
        url = f"{self.base_url}/cgi-bin/media/upload"
        params = {
            "access_token": self.get_access_token(),
            "type": media_type
        }
        
        files = {
            "media": media_file
        }
        
        response = self.session.post(url, params=params, files=files)
        response.raise_for_status()
        result = response.json()
        
        if result.get("errcode") == 0:
            return result.get("media_id")
        raise WeChatAPIError(f"上传媒体文件失败: {result}")
        
    def upload_image(self, image_file: BinaryIO) -> str:
        """
        上传图片
        
        Args:
            image_file: 图片文件对象
            
        Returns:
            str: 图片媒体文件id
        """
        return self.upload("image", image_file)
        
    def upload_voice(self, voice_file: BinaryIO) -> str:
        """
        上传语音
        
        Args:
            voice_file: 语音文件对象
            
        Returns:
            str: 语音媒体文件id
        """
        return self.upload("voice", voice_file)
        
    def upload_video(self, video_file: BinaryIO) -> str:
        """
        上传视频
        
        Args:
            video_file: 视频文件对象
            
        Returns:
            str: 视频媒体文件id
        """
        return self.upload("video", video_file)
        
    def upload_file(self, file: BinaryIO) -> str:
        """
        上传普通文件
        
        Args:
            file: 文件对象
            
        Returns:
            str: 文件媒体文件id
        """
        return self.upload("file", file)
        
    def get(self, media_id: str) -> bytes:
        """
        获取临时素材
        
        Args:
            media_id: 媒体文件id
            
        Returns:
            bytes: 媒体文件内容
        """
        url = f"{self.base_url}/cgi-bin/media/get"
        params = {
            "access_token": self.get_access_token(),
            "media_id": media_id
        }
        
        response = self.session.get(url, params=params)
        response.raise_for_status()
        
        # 检查是否是JSON响应（错误信息）
        try:
            result = response.json()
            raise WeChatAPIError(f"获取媒体文件失败: {result}")
        except:
            return response.content
            
    def upload_permanent(self, media_type: str, media_file: BinaryIO) -> str:
        """
        上传永久素材
        
        Args:
            media_type: 媒体文件类型，分别有图片（image）、语音（voice）、视频（video），普通文件（file）
            media_file: 媒体文件对象
            
        Returns:
            str: 媒体文件id
        """
        url = f"{self.base_url}/cgi-bin/material/add_material"
        params = {
            "access_token": self.get_access_token(),
            "type": media_type
        }
        
        files = {
            "media": media_file
        }
        
        response = self.session.post(url, params=params, files=files)
        response.raise_for_status()
        result = response.json()
        
        if result.get("errcode") == 0:
            return result.get("media_id")
        raise WeChatAPIError(f"上传永久素材失败: {result}")
        
    def get_permanent(self, media_id: str) -> bytes:
        """
        获取永久素材
        
        Args:
            media_id: 媒体文件id
            
        Returns:
            bytes: 媒体文件内容
        """
        url = f"{self.base_url}/cgi-bin/material/get_material"
        params = {
            "access_token": self.get_access_token(),
            "media_id": media_id
        }
        
        response = self.session.post(url, params=params)
        response.raise_for_status()
        
        # 检查是否是JSON响应（错误信息）
        try:
            result = response.json()
            raise WeChatAPIError(f"获取永久素材失败: {result}")
        except:
            return response.content
            
    def delete_permanent(self, media_id: str) -> bool:
        """
        删除永久素材
        
        Args:
            media_id: 媒体文件id
            
        Returns:
            bool: 是否成功
        """
        url = f"{self.base_url}/cgi-bin/material/del_material"
        params = {"access_token": self.get_access_token()}
        data = {"media_id": media_id}
        
        response = self._post(url, data=data)
        return response.get("errcode") == 0
        
    def get_permanent_count(self) -> Dict[str, int]:
        """
        获取永久素材的列表
        
        Returns:
            Dict[str, int]: 各类型素材数量
        """
        url = f"{self.base_url}/cgi-bin/material/get_materialcount"
        params = {"access_token": self.get_access_token()}
        
        response = self._get(url, params=params)
        return {
            "voice_count": response.get("voice_count", 0),
            "video_count": response.get("video_count", 0),
            "image_count": response.get("image_count", 0),
            "file_count": response.get("file_count", 0)
        }
        
    def get_permanent_list(self, media_type: str, offset: int = 0, count: int = 20) -> Dict[str, Any]:
        """
        获取永久素材的列表
        
        Args:
            media_type: 媒体文件类型
            offset: 从全部素材的该偏移位置开始返回，0表示从第一个素材返回
            count: 返回素材的数量，取值在1到50之间
            
        Returns:
            Dict[str, Any]: 素材列表
        """
        url = f"{self.base_url}/cgi-bin/material/batchget_material"
        params = {"access_token": self.get_access_token()}
        data = {
            "type": media_type,
            "offset": offset,
            "count": count
        }
        
        response = self._post(url, data=data)
        return response 