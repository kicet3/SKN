import streamlit as st
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import localDB

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


user_input = st.chat_input("입력")

localDB.insertData('Me',user_input)

def format_chat_history():
    history_text = ""
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            history_text += f"나: {message['content']}\n"
        else:
            history_text += f"AI: {message['content']}\n"
    return history_text

ai_prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 어떤 언어로 물어보더라도 한국어로 대답해야해"),
    ("user", "대화 내용:\n{chat_history}\n나: {prompt}\nAI:")
])

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key='',
    temperature=0
)

output_parser = StrOutputParser()

chain = ai_prompt | llm.with_config({"run_name": "model"}) | output_parser.with_config({"run_name": "Assistant"})

def display_chat_history():
    """대화 내역 전체를 출력 (스트리밍 응답 전까지 고정)"""
    for message in st.session_state.chat_history:
        role = "나" if message["role"] == "user" else "AI"
        st.write(f"**{role}:** {message['content']}")

async def generate_response(user_text, ai_placeholder):
    """이전 대화 내용과 함께 AI 응답을 스트리밍"""
    result_text = ""
    conversation_history = format_chat_history()
    prompt_vars = {"chat_history": conversation_history, "prompt": user_text}
    
    async for chunk in chain.astream_events(prompt_vars, version="v1", include_names=["Assistant"]):
        if chunk.get("event") in ["on_parser_start", "on_parser_stream"]:
            if "data" in chunk:
                data = chunk["data"]
                if isinstance(data, dict):
                    data = data.get("chunk", "")
                result_text += data
                
                ai_placeholder.markdown(f"**AI:** {result_text}")
                
    localDB.insertData('AI',result_text)                
    st.session_state.chat_history.append({"role": "assistant", "content": result_text})
    return result_text

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    display_chat_history()
    
    ai_placeholder = st.empty()
    
    try:
        asyncio.run(generate_response(user_input, ai_placeholder))
    except Exception as e:
        st.error(f"에러 발생: {e}")
