from typing import Dict, List, Optional, Union, Any
from .base import BaseClient
from .exceptions import WeChatAPIError

class WecomClient(BaseClient):
    """企业微信专用接口客户端"""
    
    def __init__(self, corp_id: str, corp_secret: str):
        super().__init__(corp_id, corp_secret)
        
    def get_interface_support(self) -> Dict[str, Any]:
        """判断接口支持情况"""
        return self._get("cgi-bin/wecom/interface/support")
    
    def get_member_info(self, userid: str) -> Dict[str, Any]:
        """获取企业成员信息"""
        return self._get("cgi-bin/wecom/member/info", params={"userid": userid})
    
    def get_address_book_session(self, userid: str) -> Dict[str, Any]:
        """获取企业通讯录与会话"""
        return self._get("cgi-bin/wecom/addressbook/session", params={"userid": userid})
    
    def get_nfc_info(self, nfc_id: str) -> Dict[str, Any]:
        """获取 NFC 信息"""
        return self._get("cgi-bin/wecom/nfc/info", params={"nfc_id": nfc_id})
    
    def send_miniprogram_notice(self, 
                              touser: str,
                              template_id: str,
                              page: str,
                              data: Dict[str, Any],
                              miniprogram_state: str = "formal") -> Dict[str, Any]:
        """发送小程序通知"""
        data = {
            "touser": touser,
            "template_id": template_id,
            "page": page,
            "data": data,
            "miniprogram_state": miniprogram_state
        }
        return self._post("cgi-bin/wecom/miniprogram/notice", json=data)
    
    def speech_to_text(self, 
                      media_id: str,
                      language: str = "zh_CN",
                      voice_type: int = 1) -> Dict[str, Any]:
        """语音转文字"""
        data = {
            "media_id": media_id,
            "language": language,
            "voice_type": voice_type
        }
        return self._post("cgi-bin/wecom/speech/transcribe", json=data)
    
    def get_oauth_user_info(self, code: str) -> Dict[str, Any]:
        """获取 OAuth2.0 用户信息"""
        return self._get("cgi-bin/wecom/oauth2/userinfo", params={"code": code})
    
    def get_web_login_info(self, code: str) -> Dict[str, Any]:
        """获取 Web 登录信息"""
        return self._get("cgi-bin/wecom/web/login/info", params={"code": code})
    
    def get_scan_login_info(self, code: str) -> Dict[str, Any]:
        """获取扫一扫登录信息"""
        return self._get("cgi-bin/wecom/scan/login/info", params={"code": code})
    
    def get_mobile_login_info(self, code: str) -> Dict[str, Any]:
        """获取移动端登录信息"""
        return self._get("cgi-bin/wecom/mobile/login/info", params={"code": code})
    
    def http_callback_login(self, 
                          callback_url: str,
                          state: str,
                          userid: str) -> Dict[str, Any]:
        """HTTP 回调登录"""
        data = {
            "callback_url": callback_url,
            "state": state,
            "userid": userid
        }
        return self._post("cgi-bin/wecom/http/callback/login", json=data)
    
    def third_party_app_login(self, 
                            app_id: str,
                            app_secret: str,
                            code: str) -> Dict[str, Any]:
        """第三方 APP 登录"""
        data = {
            "app_id": app_id,
            "app_secret": app_secret,
            "code": code
        }
        return self._post("cgi-bin/wecom/third_party/app/login", json=data)
    
    def third_party_system_login(self, 
                               system_id: str,
                               system_secret: str,
                               code: str) -> Dict[str, Any]:
        """第三方系统接入"""
        data = {
            "system_id": system_id,
            "system_secret": system_secret,
            "code": code
        }
        return self._post("cgi-bin/wecom/third_party/system/login", json=data)
    
    def sms_gateway_login(self, 
                         gateway_id: str,
                         gateway_secret: str,
                         phone: str) -> Dict[str, Any]:
        """短信网关接入"""
        data = {
            "gateway_id": gateway_id,
            "gateway_secret": gateway_secret,
            "phone": phone
        }
        return self._post("cgi-bin/wecom/sms/gateway/login", json=data)
    
    def speech_gateway_login(self, 
                           gateway_id: str,
                           gateway_secret: str,
                           phone: str) -> Dict[str, Any]:
        """语音转文字网关接入"""
        data = {
            "gateway_id": gateway_id,
            "gateway_secret": gateway_secret,
            "phone": phone
        }
        return self._post("cgi-bin/wecom/speech/gateway/login", json=data)
    
    def get_operation_logs(self, 
                         start_time: int,
                         end_time: int,
                         userids: Optional[List[str]] = None,
                         partyids: Optional[List[int]] = None) -> Dict[str, Any]:
        """获取操作日志"""
        data = {
            "start_time": start_time,
            "end_time": end_time
        }
        if userids:
            data["userids"] = userids
        if partyids:
            data["partyids"] = partyids
        return self._post("cgi-bin/wecom/operation/logs", json=data)
    
    def export_statistics_data(self, 
                             start_time: int,
                             end_time: int,
                             data_type: str) -> Dict[str, Any]:
        """导出统计数据"""
        data = {
            "start_time": start_time,
            "end_time": end_time,
            "data_type": data_type
        }
        return self._post("cgi-bin/wecom/statistics/export", json=data)
    
    def get_session_content(self, 
                          info: List[Dict[str, Any]],
                          cursor: str = "") -> Dict[str, Any]:
        """获取会话内容"""
        data = {
            "info": info,
            "cursor": cursor
        }
        return self._post("cgi-bin/wecom/session/content", json=data)
    
    def get_session_agree_info(self, 
                             info: List[Dict[str, Any]]) -> Dict[str, Any]:
        """获取会话同意情况"""
        data = {"info": info}
        return self._post("cgi-bin/wecom/session/agree/info", json=data)
    
    def decrypt_account(self, 
                       encrypted_data: str,
                       iv: str) -> Dict[str, Any]:
        """账号解密"""
        data = {
            "encrypted_data": encrypted_data,
            "iv": iv
        }
        return self._post("cgi-bin/wecom/account/decrypt", json=data)
    
    def filter_message_keywords(self, 
                              content: str,
                              keywords: List[str]) -> Dict[str, Any]:
        """消息关键字过滤"""
        data = {
            "content": content,
            "keywords": keywords
        }
        return self._post("cgi-bin/wecom/message/keywords/filter", json=data) 