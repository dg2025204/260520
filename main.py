import streamlit as st
import random

# 1. 페이지 기본 설정 (브라우저 탭에 표시될 내용)
st.set_page_config(
    page_title="석리송 제자의 비밀 기지",
    page_icon="⚡",
    layout="centered"
)

# 2. 멋진 타이틀과 소개문구 (이모지와 Markdown 활용)
st.title('⚡ 석리송 제자의 웹앱 !!!')
st.caption('어서오세요! 이곳은 석리송 제자의 아이디어가 실현되는 공간입니다.')

st.markdown('---') # 구분선

# 3. 움직이는 GIF나 이미지로 시선 강점 (선택 사항, 기본은 웰컴 인사)
st.subheader('안녕하세요!!!!!!! 👀')
st.write('방문해 주셔서 감사합니다. 나가시기 전에 아래에서 "오늘의 운세" 하나 뽑고 가세요!')

# 4. 기깔나는 인터랙티브 기능 1: 오늘의 행운 뽑기
st.markdown('### 🔮 오늘의 석리송 치트키')
lucky_messages = [
    "오늘은 뭘 해도 대박 날 날입니다. 자신감을 가지세요!",
    "코딩 에러가 한 번에 해결될 행운의 날입니다. 💻",
    "아아(아이스 아메리카노) 한 잔 마시면 집중력이 200% 상승합니다. ☕",
    "잠깐 쉬어가도 괜찮아요. 이미 잘하고 있으니까요! ✨",
    "오늘의 행운의 아이템: ⚡ (스트림릿 레이저빔)"
]

if st.button('🚀 오늘의 행운 메시지 뽑기'):
    random_msg = random.choice(lucky_messages)
    st.success(random_msg)
else:
    st.info('위 버튼을 눌러 오늘의 행운을 확인해보세요!')

st.markdown('---')

# 5. 기깔나는 인터랙티브 기능 2: 흔적 남기기 (방명록 기능 시뮬레이션)
st.markdown('### ✍️ 방문록 한 줄 남기기')
visitor_name = st.text_input('이름 또는 닉네임', placeholder='홍길동')
visitor_msg = st.text_area('제자에게 한마디!', placeholder='웹앱 너무 멋져요!')

if st.button('응원 전송하기 💌'):
    if visitor_name and visitor_msg:
        st.balloons() # 화면에 풍선 애니메이션 효과!!
        st.success(f'🎉 {visitor_name}님의 소중한 의견이 전송되었습니다! (마음속으로 저장 완료)')
    else:
        st.warning('이름과 한마디를 모두 입력해주세요!')

# 6. 사이드바 꾸미기
with st.sidebar:
    st.header("👤 프로필")
    st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500", caption="Creative Mind") # 감성적인 추상화 이미지
    st.markdown("""
    **석리송 제자**
    - 특기: 폭풍 성장 중
    - 목표: Streamlit 마스터하기
    """)
    st.write("© 2026 석리송 All rights reserved.")
