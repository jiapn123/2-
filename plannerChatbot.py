import streamlit as st
from openai import OpenAI
api_key = st.secrets[“openai_secret”]
# OpenAI API 키 설정
client = OpenAI(api_key=api_key)
# 페이지 설정
st.set_page_config(page_title=“챗봇 서비스 페이지“, layout=“wide”)
# 페이지 제목
st.title(“챗봇 서비스“)
# 챗봇 대화 기록 초기화
if ‘messages’ not in st.session_state:
    st.session_state[‘messages’] = []
# 대화 표시
for message in st.session_state[‘messages’]:
    with st.chat_message(message[‘role’]):
        st.markdown(message[‘content’])
# 대화 입력
prompt = st.chat_input(“메시지 입력“)
if prompt:
    with st.chat_message(‘user’):
        st.markdown(prompt)
    st.session_state[‘messages’].append({‘role’:‘user’,‘content’:prompt})
    # OpenAI API 호출
    response = client.chat.completions.create(
        model=“gpt-3.5-turbo”,
        messages=[{“role”: “user”, “content”: prompt}],
        max_tokens=2000
    )
    # 응답 처리
    if response.choices:
        extracted_text = response.choices[0].message.content
        with st.chat_message(‘assistant’):
            st.markdown(extracted_text)
        st.session_state[‘messages’].append({‘role’:‘assistant’,“content”:extracted_text})
