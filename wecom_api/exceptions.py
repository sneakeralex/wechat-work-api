class WeChatAPIError(Exception):
    """企业微信 API 调用异常"""
    pass

class WeChatConfigError(Exception):
    """企业微信配置异常"""
    pass

class WeChatAuthError(Exception):
    """企业微信认证异常"""
    pass 