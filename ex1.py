import streamlit as st
import pandas as pd

# 세션 상태 초기화 (page와 page_history 속성 추가)
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'page_history' not in st.session_state:
    st.session_state.page_history = []
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ''

# 메인 페이지
# 기존 회원이 아닐 경우 자동으로 추가 후 넘어가기
def home_page():
    st.header("로그인")
    user_input = st.text_input("닉네임을 입력하세요:", st.session_state['user_input'])

    if st.button("페이지 1로 이동"):
        st.session_state.page_history.append(st.session_state.page)  # 현재 페이지를 페이지 이력에 추가
        st.session_state.page = 'page'

def page():
    st.header("테마 선정")
    # 컬럼 분할
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("테마1")
        st.write("테마1 학습")

        if st.button("시작하기"):
            st.session_state.page_history.append(st.session_state.page)
            st.session_state.page = 'page1'

    with col2:
        st.header("테마2")
        st.write("테마2 학습")

        if st.button("참여하기"):
            st.session_state.page_history.append(st.session_state.page)
            st.session_state.page = 'page2'

    with col3:
        st.header("테마3")
        st.write("테마3 학습")

        if st.button("이동"):
            st.session_state.page_history.append(st.session_state.page)
            st.session_state.page = 'page3'

def page1():
    st.header("줄거리 소개")
    st.write("챕터, 목표 소개")
    if st.button("시작하기"):
        st.session_state.page_history.append(st.session_state.page)  # 현재 페이지를 페이지 이력에 추가
        st.session_state.page = 'page1-1'

def page1_1():
    st.header("학습 진행")

# 앱 로직
def app():
    if st.session_state.page == 'home':
        home_page()
    elif st.session_state.page == 'page':
        page()    
    elif st.session_state.page == 'page1':
        page1()
    elif st.session_state.page == 'page1-1':
        page1_1()
     
    # elif st.session_state.page == 'page2':
    #     page2()
    # elif st.session_state.page == 'page3':
    #     page3()


app()