import streamlit as st
import time

# 1. 페이지 설정 (다크 모드에 어울리는 아이콘)
st.set_page_config(
    page_title="SeokRiSong.dev",
    page_icon="🔮",
    layout="centered"
)

# 2. 상단 헤더 & 네온 스타일 타이틀
st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <h1 style="color: #00FFCC; font-family: 'Courier New', monospace;">🔮 STUDIO. SEOKRISONG</h1>
        <p style="color: #888888; font-size: 1.1rem;">안녕하세요!!!!!!! 👀 혁신을 코딩하는 석리송 제자의 공간입니다.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# 3. 탭(Tabs)을 이용한 깔끔한 화면 분할
tab1, tab2, tab3 = st.tabs(["🚀 HOME", "📊 MY STATUS", "💬 CONTACT"])

# --- TAB 1: 홈 화면 (소개 및 로딩 레이저) ---
with tab1:
    st.subheader("💡 MAIN WORKSPACE")
    st.write("Streamlit을 활용해 아이디어를 빠르게 프로토타이핑하고 있습니다. 아래 버튼을 눌러 시스템을 가동해보세요.")
    
    if st.button("⚡ 시스템 엔진 가동 (Click)"):
        with st.spinner("엔진 예열 중..."):
            time.sleep(1.5)
        st.snow() # 화면에 눈이 내리는 이펙트 효과!
        st.success("시스템 가동 완료. 이제 당신의 상상력을 현실로 만드세요.")
        
    # 간지나는 대시보드형 메트릭(지표) 배치
    col1, col2, col3 = st.columns(3)
    col1.metric(label="코딩 열정", value="999 %", delta="▲ 12%")
    col2.metric(label="커피 섭취량", value="4.5 잔", delta="▲ 1.5잔")
    col3.metric(label="버그 해결률", value="94.2 %", delta="-2.1%", delta_color="inverse")

# --- TAB 2: 내 스탯 측정하기 (인터랙티브 슬라이더) ---
with tab2:
    st.subheader("📊 제자의 현재 스탯 분석")
    st.write("슬라이더를 조절해 오늘의 역량을 체크해보세요.")
    
    python_skill = st.slider("Python 코딩 능력", 0, 100, 70)
    creativity = st.slider("창의성 및 기깔남", 0, 100, 85)
    energy = st.slider("오늘의 에너지 레벨", 0, 100, 50)
    
    # 실시간 점수 계산 및 피드백
    total_score = (python_skill + creativity + energy) // 3
    
    st.markdown(f"### 🎯 종합 평가 점수: `{total_score}점`")
    if total_score >= 80:
        st.balloons()
        st.info("🔥 현재 폭주 상태! 지금 당장 코딩을 시작해야 합니다.")
    elif total_score >= 50:
        st.warning("☕ 연료(커피)가 조금 더 필요한 시점입니다.")
    else:
        st.error("💤 충전이 필요합니다. 오늘은 맛있는 걸 드세요!")

# --- TAB 3: 방명록 및 연락처 ---
with tab3:
    st.subheader("💬 LEAVE A MESSAGE")
    
    with st.form(key="contact_form"):
        name = st.text_input("Name", placeholder="닉네임을 입력하세요.")
        message = st.text_area("Message", placeholder="석리송 제자에게 응원의 한마디를 남겨주세요.")
        submit_button = st.form_submit_button(label="🚀 메시지 전송")
        
        if submit_button:
            if name and message:
                st.success(f"✨ [{name}]님의 메시지가 성공적으로 서버에 전달되었습니다! 감사합니다.")
            else:
                st.error("이름과 메시지를 모두 입력해주세요.")

# 4. 사이드바 - 미니멀한 토글 및 다크 감성
with st.sidebar:
    st.markdown("### `SYSTEM INFO`")
    st.code("""
Status: Running
Version: 2.0.1
Env: Streamlit Cloud
    """, language="bash")
    
    # 진행 바(Progress Bar) 디자인용
    st.markdown("**Project Progress**")
    my_bar = st.progress(0)
    my_bar.progress(75) # 75% 진척도 표시
