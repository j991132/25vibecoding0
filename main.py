import streamlit as st

# Streamlit 페이지 설정
st.set_page_config(page_title="✨ MBTI로 찾는 꿈의 직업! ✨", page_icon="🌟", layout="centered")

# CSS 스타일링으로 화려한 디자인 추가
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fad0c4, #ff9a9e);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .title {
        font-size: 3em;
        color: #ffffff;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 1.5em;
        color: #fefefe;
        text-align: center;
        margin-bottom: 30px;
    }
    .selectbox {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .result-box {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        font-size: 1.2em;
        color: #333;
    }
    .emoji {
        font-size: 1.5em;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff6b6b, #ff8e53);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 1.2em;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #ff8e53, #ff6b6b);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# MBTI 유형별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["전략 컨설턴트 🧠", "소프트웨어 개발자 💻", "과학자 🔬", "기업가 🚀"],
    "INTP": ["데이터 분석가 📊", "철학자 📚", "프로그래머 🖥️", "연구원 🔍"],
    "ENTJ": ["CEO 🌟", "마케팅 매니저 📈", "변호사 ⚖️", "프로젝트 매니저 📅"],
    "ENTP": ["스타트업 창업자 💡", "광고 기획자 🎨", "저널리스트 ✍️", "토론자 🎤"],
    "INFJ": ["상담사 🤝", "작가 ✒️", "사회복지사 ❤️", "교육자 🍎"],
    "INFP": ["예술가 🎨", "카운셀러 🌈", "작곡가 🎶", "비영리 단체 활동가 🌍"],
    "ENFJ": ["교사 📚", "이벤트 플래너 🎉", "HR 매니저 👥", "코치 🏆"],
    "ENFP": ["크리에이티브 디렉터 🎥", "여행 가이드 ✈️", "마케터 📣", "배우 🎭"],
    "ISTJ": ["회계사 💼", "법무사 📜", "물류 관리자 🚚", "감사관 🔎"],
    "ISFJ": ["간호사 🩺", "행정 보조 📋", "도서관 사서 📚", "유치원 교사 👶"],
    "ESTJ": ["관리자 🏢", "판사 ⚖️", "경찰관 👮", "금융 분석가 💰"],
    "ESFJ": ["호텔 매니저 🏨", "판매원 🛍️", "커뮤니티 매니저 🌐", "이벤트 코디네이터 🎈"],
    "ISTP": ["엔지니어 🔧", "파일럿 ✈️", "사진작가 📸", "소방관 🚒"],
    "ISFP": ["플로리스트 💐", "패션 디자이너 👗", "요리사 🍳", "그래픽 디자이너 🎨"],
    "ESTP": ["스포츠 코치 🏀", "영업 사원 💸", "응급 의료 기술자 🚑", "탐험가 🗺️"],
    "ESFP": ["연예인 🎤", "파티 플래너 🎊", "투어 가이드 🌴", "소셜 미디어 인플루언서 📱"]
}

# 메인 UI 구성
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">🌈 MBTI로 찾아가는 꿈의 직업! 🌈</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 성격 유형에 맞는 멋진 커리어를 발견해보세요! 🎯</div>', unsafe_allow_html=True)

# MBTI 선택 드롭다운
mbti = st.selectbox(
    "✨ 당신의 MBTI 유형을 선택하세요! ✨",
    list(mbti_jobs.keys()),
    format_func=lambda x: f"{x} 😊",
    key="mbti_select",
    help="MBTI 유형을 선택하면 맞춤 직업을 추천해드려요! 🌟"
)

# 추천 버튼
if st.button("🎉 직업 추천받기! 🎉"):
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.markdown(f"### {mbti}님을 위한 추천 직업! 🚀")
    for job in mbti_jobs[mbti]:
        st.markdown(f"- {job} <span class='emoji'>✨</span>", unsafe_allow_html=True)
    st.markdown(f"**{mbti}** 유형의 당신은 이 분야에서 빛날 거예요! 🌟 계속해서 꿈을 향해 나아가세요! 💪", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 푸터
st.markdown("""
    <div style='text-align: center; margin-top: 30px; color: #ffffff;'>
        <p>만든 사람: xAI와 함께하는 Grok 🌌 | 당신의 꿈을 응원합니다! 💖</p>
    </div>
""", unsafe_allow_html=True)
