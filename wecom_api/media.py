from typing import Dict, Any, Optional, BinaryIO
from .base import WecomBaseClient

class MediaClient(WecomBaseClient):
    """媒体文件客户端"""
    
    def upload_image(self, file: BinaryIO) -> Dict[str, Any]:
        """上传图片"""
        files = {"media": file}
        return self._post_file("media/upload", files=files, data={"type": "image"})
    
    def upload_voice(self, file: BinaryIO) -> Dict[str, Any]:
        """上传语音"""
        files = {"media": file}
        return self._post_file("media/upload", files=files, data={"type": "voice"})
    
    def upload_video(self, file: BinaryIO) -> Dict[str, Any]:
        """上传视频"""
        files = {"media": file}
        return self._post_file("media/upload", files=files, data={"type": "video"})
    
    def upload_file(self, file: BinaryIO) -> Dict[str, Any]:
        """上传普通文件"""
        files = {"media": file}
        return self._post_file("media/upload", files=files, data={"type": "file"})
    
    def get(self, media_id: str) -> Dict[str, Any]:
        """获取临时素材"""
        return self._get("media/get", params={"media_id": media_id})
    
    def upload_permanent(self, type: str, file: BinaryIO) -> Dict[str, Any]:
        """上传永久素材"""
        files = {"media": file}
        return self._post_file("material/add_material", files=files, data={"type": type})
    
    def get_permanent(self, media_id: str) -> Dict[str, Any]:
        """获取永久素材"""
        return self._get("material/get", params={"media_id": media_id})
    
    def delete_permanent(self, media_id: str) -> Dict[str, Any]:
        """删除永久素材"""
        return self._post("material/del", json={"media_id": media_id})
    
    def get_permanent_count(self) -> Dict[str, Any]:
        """获取永久素材数量"""
        return self._get("material/get_count")
    
    def get_permanent_list(self, type: str, offset: int = 0, count: int = 20) -> Dict[str, Any]:
        """获取永久素材列表"""
        data = {
            "type": type,
            "offset": offset,
            "count": count
        }
        return self._post("material/batchget", json=data) 