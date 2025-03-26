class WeChatAPIError(Exception):
    """企业微信 API 错误"""
    pass

class WeChatConfigError(Exception):
    """企业微信配置错误"""
    pass

class WeChatAuthError(Exception):
    """企业微信认证错误"""
    pass 