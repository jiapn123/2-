import streamlit as st
import openai
from openai import OpenAI


st.sidebar.title("여행계획 챗봇")

api_key= st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.sidebar.empty():
        st.markdown(f"**{message['role'].capitalize()}:** {message['content']}")

prompt = st.sidebar.text_input("여행기간, 인원수 및 가고 싶은 곳을 알려주시면 여행 계획 짜드리겠습니다!")

if st.sidebar.button("Send"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.sidebar.empty():
        st.markdown(f"**User:** {prompt}")

    prompt_lines = [f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages]
    prompt = "Conversation:\n" + '\n'.join(prompt_lines)

    response = openai.completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt={"role": "user", "content": prompt},
        max_tokens=1000
    )

    full_response = response.choices[0].text.strip()
    with st.sidebar.empty():
        st.markdown(f"**:robot_face:** {full_response}")
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
