'''
랭체인(LangChain)이란?

초거대 언어모델(LLM) 어플리케이션 개발 프레임워크
= LLM 개발용 도구 모음

프레임워크 = 관련도구모음

'''

#from dotenv import load_dotenv
#load_dotenv()

# from langchain_openai import OpenAI
# llm = OpenAI()
# result = llm.invoke("내가 좋아하는 동물은")
# print(result)


import streamlit as st
from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

st.title("인공지능 시인")

content = st.text_input("시의 주제를 제시해주세요")


if st.button("시 작성 요청하기"):
    with st.spinner("Wait for it...", show_time=True):

        result = chat_model.invoke(content + "에 대한 시를 써줘")
        #print(result.content)
        st.write(result.content)

#st.title("_Streamlit_ is :blue[cool] :sunglasses:")
#title = st.text_input("시의 주제를 제시해주세요",)
#st.write("시의 주제는", title)


