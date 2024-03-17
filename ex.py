import streamlit as st
import pandas as pd
import numpy as np


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
        st.session_state.page = 'page1'

# 페이지 1 개인 정보와 학습 진행 메인 페이지
def page1():
    st.header("닉네임_님 안녕하세요")

    container = st.container(border=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("학습 어휘", "70", "+1")
    col2.metric("회화", "9", "-8%")
    col3.metric("전체 학습률", "86%", "4%")

    st.write("일일 학습 달성 그래프")
    chart_data = pd.DataFrame(np.random.randn(10, 1), columns=["a"])
    st.line_chart(chart_data,width=200,height=150)
    container = st.container(border=True)
    container.write("오늘의 추천 영단어:")
    df = pd.DataFrame(np.random.randn(10, 3), columns=["단어", "뜻","예시 문장"])
    container.table(df.head(1).reset_index(drop=True))
    
    # 화면을 두 컬럼으로 분할
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("영화")
        st.write("영화를 이용한 언어 학습.")

        if st.button("학습 페이지 이동"):
            st.session_state.page_history.append(st.session_state.page)  # 현재 페이지를 페이지 이력에 추가
            st.session_state.page = 'page2'

    with col2:
        st.header("LLM tts")
        st.write("기존 단어를 이용한 회화 학습.")

        if st.button("페이지 이동"):
            st.session_state.page_history.append(st.session_state.page)  # 현재 페이지를 페이지 이력에 추가
            st.session_state.page = 'page3'
    
    with col3:
        st.header("복습")
        st.write("복습 페이지 이동.")

        if st.button("이동"):
            st.session_state.page_history.append(st.session_state.page)  # 현재 페이지를 페이지 이력에 추가
            st.session_state.page = 'page4'

# 영화를 이용한 학습 페이지
def page2():
    st.header("영화를 이용한 학습")
    st.write("여기는 페이지 2입니다.")

    # 문제 목록 : 이걸 index로 받아오면 좋을 것 같다!
    questions = [
        "첫 번째 텍스트",
        "두 번째 텍스트",
        "세 번째 텍스트",
        "네 번째 텍스트",
        "다섯 번째 텍스트",
        "여섯 번째 텍스트",
        "일곱 번째 텍스트",
        "여덟 번째 텍스트",
        "아홉 번째 텍스트",
        "열 번째 텍스트"
    ]

    # 이전 문제의 인덱스를 저장하는 세션 상태 변수
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0

    if st.session_state.question_index < len(questions):
        # 현재 문제 인덱스에 해당하는 문제 표시
        current_question = questions[st.session_state.question_index]

        # 비활성화된 텍스트 영역 생성
        txt = st.text_area(
            "Text to analyze",
            current_question,
            disabled=True
        )

        # 선택 상자 생성
        option = st.selectbox(
            'How would you like to be contacted?',
            ('Email', 'Home phone', 'Mobile phone'))

        # 확인 버튼 생성
        if st.button("확인"):
            # 정답 검증
            correct_answer = "Email"
            if option == correct_answer:
                st.success("정답입니다!")
            else:
                st.error(f"오답입니다. 정답은 '{correct_answer}'입니다.")
            # 다음 문제로 이동
            st.session_state.question_index += 1
    else:
        st.write("문제를 모두 푸셨습니다.")

    if st.button("뒤로가기"):
        st.session_state.page = st.session_state.page_history.pop()  # 이전 페이지로 이동


# 페이지 3 : LLM tts를 이용한 학습 페이지
def page3():
    st.header("LLM tts를 이용한 학습")
    st.write("여기는 페이지 3입니다.")
    prompt = st.chat_input("Say something")

    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
        
    if st.button("뒤로가기"):
        st.session_state.page = st.session_state.page_history.pop()  # 이전 페이지로 이동

# 페이지 4 : 복습 페이지
def page4():
    st.header("복습 페이지")
    st.write("여기는 복습 페이지 입니다. 수정 가능성 매우 높음!")
    if st.button("뒤로가기"):
        st.session_state.page = st.session_state.page_history.pop()  # 이전 페이지로 이동


# 앱 로직
def app():
    if st.session_state.page == 'home':
        home_page()
    elif st.session_state.page == 'page1':
        page1()
    elif st.session_state.page == 'page2':
        page2()
    elif st.session_state.page == 'page3':
        page3()
    elif st.session_state.page == 'page4':
        page4()

app()
