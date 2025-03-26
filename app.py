import streamlit as st
import json
from wechat_work import WeChatWorkAPI
from datetime import datetime
import tempfile
import os

st.set_page_config(page_title="WeChat Work API Tester", layout="wide")

def validate_credentials(corp_id: str, corp_secret: str, agent_id: str) -> tuple[bool, str]:
    """Validate WeChat Work credentials"""
    if not corp_id or not corp_secret:
        return False, "企业ID和企业密钥不能为空"
    
    if not corp_id.isalnum():
        return False, "企业ID只能包含字母和数字"
    
    if len(corp_id) < 5:
        return False, "企业ID长度不正确"
    
    if len(corp_secret) < 10:
        return False, "企业密钥长度不正确"
    
    if agent_id and not agent_id.isalnum():
        return False, "应用ID只能包含字母和数字"
    
    return True, ""

def init_api():
    """Initialize WeChat Work API with credentials from session state"""
    corp_id = st.session_state.get('corp_id', '')
    corp_secret = st.session_state.get('corp_secret', '')
    agent_id = st.session_state.get('agent_id', '')
    
    # Validate credentials
    is_valid, error_msg = validate_credentials(corp_id, corp_secret, agent_id)
    if not is_valid:
        st.error(error_msg)
        return None
    
    try:
        api = WeChatWorkAPI(
            corp_id=corp_id,
            corp_secret=corp_secret,
            agent_id=agent_id
        )
        # Test access token
        api.access_token
        return api
    except Exception as e:
        error_msg = str(e)
        if "invalid credential" in error_msg.lower():
            st.error("认证失败：请检查企业ID和企业密钥是否正确")
        elif "access_token" in error_msg.lower():
            st.error("获取访问令牌失败：请检查网络连接")
        else:
            st.error(f"初始化失败：{error_msg}")
        return None

def display_result(result):
    """Display API result in a formatted way"""
    if isinstance(result, (dict, list)):
        st.json(result)
    else:
        st.write(result)

def test_department_api(api):
    """Test department APIs"""
    st.header("部门管理 API")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("获取部门列表"):
            try:
                result = api.department.list()
                st.success("成功！")
                display_result(result)
            except Exception as e:
                st.error(f"错误：{str(e)}")
    
    with col2:
        if st.button("获取部门详情"):
            department_id = st.text_input("部门ID")
            if department_id:
                try:
                    result = api.department.get(department_id)
                    st.success("成功！")
                    display_result(result)
                except Exception as e:
                    st.error(f"错误：{str(e)}")

def test_user_api(api):
    """Test user APIs"""
    st.header("成员管理 API")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("获取成员列表"):
            try:
                result = api.user.list()
                st.success("成功！")
                display_result(result)
            except Exception as e:
                st.error(f"错误：{str(e)}")
    
    with col2:
        if st.button("获取成员详情"):
            user_id = st.text_input("成员ID")
            if user_id:
                try:
                    result = api.user.get(user_id)
                    st.success("成功！")
                    display_result(result)
                except Exception as e:
                    st.error(f"错误：{str(e)}")

def test_message_api(api):
    """Test message APIs"""
    st.header("消息管理 API")
    
    if st.button("发送文本消息"):
        content = st.text_area("消息内容")
        to_user = st.text_input("接收成员（多个成员用逗号分隔）")
        if content and to_user:
            try:
                result = api.message.send_text(
                    agent_id=st.session_state.agent_id,
                    content=content,
                    to_user=to_user
                )
                st.success("成功！")
                display_result(result)
            except Exception as e:
                st.error(f"错误：{str(e)}")

def test_media_api(api):
    """Test media APIs"""
    st.header("媒体管理 API")
    
    uploaded_file = st.file_uploader("上传媒体文件", type=['jpg', 'png', 'gif', 'mp3', 'mp4'])
    if uploaded_file:
        try:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file.flush()
                
                with open(tmp_file.name, 'rb') as f:
                    result = api.media.upload(uploaded_file.type.split('/')[0], f)
                    st.success("成功！")
                    display_result(result)
                
                os.unlink(tmp_file.name)
        except Exception as e:
            st.error(f"错误：{str(e)}")

def test_tag_api(api):
    """Test tag APIs"""
    st.header("标签管理 API")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("获取标签列表"):
            try:
                result = api.tag.list()
                st.success("成功！")
                display_result(result)
            except Exception as e:
                st.error(f"错误：{str(e)}")
    
    with col2:
        if st.button("获取标签成员"):
            tag_id = st.text_input("标签ID")
            if tag_id:
                try:
                    result = api.tag.get_members(tag_id)
                    st.success("成功！")
                    display_result(result)
                except Exception as e:
                    st.error(f"错误：{str(e)}")

def test_external_contact_api(api):
    """Test external contact APIs"""
    st.header("客户管理 API")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("获取客户列表"):
            user_id = st.text_input("企业成员ID")
            if user_id:
                try:
                    result = api.external_contact.list(user_id)
                    st.success("成功！")
                    display_result(result)
                except Exception as e:
                    st.error(f"错误：{str(e)}")
    
    with col2:
        if st.button("获取客户详情"):
            external_user_id = st.text_input("客户ID")
            if external_user_id:
                try:
                    result = api.external_contact.get(external_user_id)
                    st.success("成功！")
                    display_result(result)
                except Exception as e:
                    st.error(f"错误：{str(e)}")

def test_checkin_api(api):
    """Test check-in APIs"""
    st.header("打卡管理 API")
    
    if st.button("获取打卡数据"):
        user_id = st.text_input("成员ID")
        if user_id:
            try:
                result = api.checkin.get_checkin_data(
                    open_checkin_data=[{"userid": user_id}]
                )
                st.success("成功！")
                display_result(result)
            except Exception as e:
                st.error(f"错误：{str(e)}")

def main():
    st.title("企业微信 API 测试工具")
    
    # Sidebar for credentials
    with st.sidebar:
        st.header("API 凭证")
        st.text_input("企业ID (Corp ID)", key="corp_id", help='在"我的企业"页面查看')
        st.text_input("企业密钥 (Corp Secret)", key="corp_secret", type="password", help='在"应用管理"页面查看')
        st.text_input("应用ID (Agent ID)", key="agent_id", help='在"应用管理"页面查看')
        
        if st.button("初始化 API"):
            api = init_api()
            if api:
                st.success("API 初始化成功！")
            else:
                st.error("请检查凭证是否正确")
    
    # Main content
    api = init_api()
    if api:
        # API Test Sections
        test_department_api(api)
        test_user_api(api)
        test_message_api(api)
        test_media_api(api)
        test_tag_api(api)
        test_external_contact_api(api)
        test_checkin_api(api)
    else:
        st.warning("请在左侧输入 API 凭证以开始测试")

if __name__ == "__main__":
    main() 