import time
import hashlib
import json
from typing import Dict, Any, Optional
from .client import WeChatWorkClient

class JSSDKAPI:
    """JSSDK API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def get_jsapi_ticket(self) -> Dict[str, Any]:
        """
        Get JSAPI ticket
        
        Returns:
            JSAPI ticket info
        """
        return self.client.get("get_jsapi_ticket")
    
    def get_agent_config(
        self,
        agent_id: str,
        timestamp: Optional[int] = None,
        nonce_str: Optional[str] = None,
        jsapi_ticket: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get agent config
        
        Args:
            agent_id: Agent ID
            timestamp: Timestamp
            nonce_str: Nonce string
            jsapi_ticket: JSAPI ticket
            
        Returns:
            Agent config
        """
        if timestamp is None:
            timestamp = int(time.time())
        if nonce_str is None:
            nonce_str = hashlib.md5(str(timestamp).encode()).hexdigest()
        if jsapi_ticket is None:
            jsapi_ticket = self.get_jsapi_ticket()["ticket"]
            
        return self.client.post_json("agent/get_agent_config", json_data={
            "agentid": agent_id,
            "timestamp": timestamp,
            "nonceStr": nonce_str,
            "jsapi_ticket": jsapi_ticket
        })
    
    def get_jsapi_signature(
        self,
        url: str,
        jsapi_ticket: Optional[str] = None,
        timestamp: Optional[int] = None,
        nonce_str: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get JSAPI signature
        
        Args:
            url: Current URL
            jsapi_ticket: JSAPI ticket
            timestamp: Timestamp
            nonce_str: Nonce string
            
        Returns:
            Signature info
        """
        if timestamp is None:
            timestamp = int(time.time())
        if nonce_str is None:
            nonce_str = hashlib.md5(str(timestamp).encode()).hexdigest()
        if jsapi_ticket is None:
            jsapi_ticket = self.get_jsapi_ticket()["ticket"]
            
        return self.client.post_json("get_jsapi_signature", json_data={
            "url": url,
            "jsapi_ticket": jsapi_ticket,
            "timestamp": timestamp,
            "nonceStr": nonce_str
        }) 