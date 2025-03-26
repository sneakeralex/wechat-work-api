import os
from typing import Dict, Any, Optional, Union, BinaryIO
from .client import WeChatWorkClient

class MediaAPI:
    """Media API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def upload(
        self,
        media_type: str,
        media_file: Union[str, BinaryIO],
        filename: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Upload media file
        
        Args:
            media_type: Media type (image, voice, video, file)
            media_file: Media file path or file object
            filename: File name (required if media_file is file object)
            
        Returns:
            Upload result with media_id
        """
        url = f"{self.client.BASE_URL}/media/upload"
        params = {
            "access_token": self.client.access_token,
            "type": media_type
        }
        
        if isinstance(media_file, str):
            if not os.path.exists(media_file):
                raise FileNotFoundError(f"File not found: {media_file}")
            filename = os.path.basename(media_file)
            with open(media_file, "rb") as f:
                files = {"media": (filename, f)}
                response = self.client._request("POST", "media/upload", params=params, files=files)
        else:
            if not filename:
                raise ValueError("filename is required when media_file is file object")
            files = {"media": (filename, media_file)}
            response = self.client._request("POST", "media/upload", params=params, files=files)
            
        return response
    
    def get(self, media_id: str) -> bytes:
        """
        Get media file
        
        Args:
            media_id: Media ID
            
        Returns:
            Media file content
        """
        url = f"{self.client.BASE_URL}/media/get"
        params = {
            "access_token": self.client.access_token,
            "media_id": media_id
        }
        
        response = self.client._request("GET", "media/get", params=params)
        return response.content
    
    def get_jssdk(self, media_id: str) -> Dict[str, Any]:
        """
        Get media file for JSSDK
        
        Args:
            media_id: Media ID
            
        Returns:
            Media file info
        """
        return self.client.get("media/get_jssdk", params={"media_id": media_id}) 