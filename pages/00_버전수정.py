import streamlit as st

# Streamlit 페이지 설정
st.set_page_config(page_title="✨ MBTI로 찾는 꿈의 직업!(버전수정) ✨", page_icon="🌟", layout="wide")

# CSS 스타일링
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fad0c4, #ff9a9e);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .title {
        font-size: 3.5em;
        color: #ffffff;
        text-align: center;
        font-weight: bold;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 1.8em;
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
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        font-size: 1.2em;
        color: #333;
    }
    .job-item {
        cursor: pointer;
        padding: 10px;
        border-radius: 8px;
        transition: background 0.3s ease;
    }
    .job-item:hover {
        background-color: #ff9a9e;
        color: #fff;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff6b6b, #ff8e53);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 24px;
        font-size: 1.3em;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        width: 100%;
        text-align: left;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #ff8e53, #ff6b6b);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        transform: translateY(-2px);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #fad0c4, #ff9a9e);
        border-radius: 10px;
        padding: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 애니메이션 한 번만 실행
if 'animation_shown' not in st.session_state:
    st.balloons()
    st.snow()
    st.session_state.animation_shown = True

# MBTI 유형별 직업 추천 및 설명 데이터
mbti_jobs = {
    "INTJ": {
        "jobs": ["전략 컨설턴트 🧠", "소프트웨어 개발자 💻", "과학자 🔬", "기업가 🚀"],
        "descriptions": {
            "전략 컨설턴트 🧠": "기업의 장기 목표를 설정하고 효율적인 전략을 설계합니다. 분석과 창의력이 필요해요! 📈",
            "소프트웨어 개발자 💻": "앱과 시스템을 코딩하며 기술 혁신을 이끌어요. 문제 해결의 마법사! 🖥️",
            "과학자 🔬": "실험과 연구로 새로운 지식을 창출합니다. 호기심이 핵심! 🔍",
            "기업가 🚀": "새로운 비즈니스를 창업하고 시장을 선도해요. 리더십이 빛나요! 🌟"
        }
    },
    "INTP": {
        "jobs": ["데이터 분석가 📊", "철학자 📚", "프로그래머 🖥️", "연구원 🔍"],
        "descriptions": {
            "데이터 분석가 📊": "데이터를 분석해 인사이트를 도출합니다. 숫자의 마법사! 📉",
            "철학자 📚": "깊은 사고로 삶의 질문을 탐구해요. 지적 호기심이 핵심! 🤔",
            "프로그래머 🖥️": "코드를 통해 아이디어를 현실로 만듭니다. 창의적 문제 해결! 💾",
            "연구원 🔍": "새로운 발견을 위해 실험과 분석을 수행해요. 진실 추구자! 🔬"
        }
    },
    "ENTJ": {
        "jobs": ["CEO 🌟", "마케팅 매니저 📈", "변호사 ⚖️", "프로젝트 매니저 📅"],
        "descriptions": {
            "CEO 🌟": "기업을 이끌며 비전을 실현해요. 강력한 리더십 필요! 🏢",
            "마케팅 매니저 📈": "브랜드 전략을 세우고 시장을 공략해요. 창의력과 추진력! 📣",
            "변호사 ⚖️": "법률 문제 해결과 정의 구현! 논리와 설득력의 달인! ⚖️",
            "프로젝트 매니저 📅": "프로젝트를 계획하고 실행해요. 조직의 마에스트로! 📋"
        }
    },
    "ENTP": {
        "jobs": ["스타트업 창업자 💡", "광고 기획자 🎨", "저널리스트 ✍️", "토론자 🎤"],
        "descriptions": {
            "스타트업 창업자 💡": "혁신적인 아이디어로 새 비즈니스를 시작해요! 💥",
            "광고 기획자 🎨": "창의적인 캠페인으로 브랜드를 빛나게! 🎥",
            "저널리스트 ✍️": "이야기를 발굴하고 세상에 전파해요. 호기심의 전령! 📰",
            "토론자 🎤": "논쟁을 통해 새로운 관점을 제시해요. 말의 마법사! 🗣️"
        }
    },
    "INFJ": {
        "jobs": ["상담사 🤝", "작가 ✒️", "사회복지사 ❤️", "교육자 🍎"],
        "descriptions": {
            "상담사 🤝": "사람들의 마음을 치유하고 성장시키는 역할! 공감의 달인! 🧡",
            "작가 ✒️": "글로 감동과 메시지를 전달해요. 상상력의 창조자! 📖",
            "사회복지사 ❤️": "사회적 약자를 돕고 더 나은 세상을 만들어요! 🌍",
            "교육자 🍎": "학생들의 잠재력을 키우는 멘토! 지식의 전달자! 📚"
        }
    },
    "INFP": {
        "jobs": ["예술가 🎨", "카운셀러 🌈", "작곡가 🎶", "비영리 단체 활동가 🌍"],
        "descriptions": {
            "예술가 🎨": "창작으로 감정을 표현해요. 영감의 화가! 🖌️",
            "카운셀러 🌈": "타인의 마음을 이해하고 치유해요. 따뜻한 공감자! 🤗",
            "작곡가 🎶": "음악으로 이야기를 들려줘요. 감성의 연주자! 🎵",
            "비영리 단체 활동가 🌍": "사회 변화를 위해 헌신해요. 이상주의자! 🌱"
        }
    },
    "ENFJ": {
        "jobs": ["교사 📚", "이벤트 플래너 🎉", "HR 매니저 👥", "코치 🏆"],
        "descriptions": {
            "교사 📚": "학생들에게 지식과 영감을 전파해요! 멘토의 역할! 🍎",
            "이벤트 플래너 🎉": "멋진 이벤트를 기획하고 실행해요. 축제의 마법사! 🎈",
            "HR 매니저 👥": "조직의 인재를 관리하고 문화를 만들어요! 👩‍💼",
            "코치 🏆": "사람들의 목표 달성을 돕는 멘토! 동기부여의 달인! 🥇"
        }
    },
    "ENFP": {
        "jobs": ["크리에이티브 디렉터 🎥", "여행 가이드 ✈️", "마케터 📣", "배우 🎭"],
        "descriptions": {
            "크리에이티브 디렉터 🎥": "창의적인 프로젝트를 이끌어요. 아이디어의 마에스트로! 🎬",
            "여행 가이드 ✈️": "사람들에게 새로운 경험을 선사해요. 모험의 안내자! 🌴",
            "마케터 📣": "브랜드를 빛나게 하는 전략가! 열정의 전파자! 📈",
            "배우 🎭": "연기로 감정을 전달해요. 무대의 스타! 🌟"
        }
    },
    "ISTJ": {
        "jobs": ["회계사 💼", "법무사 📜", "물류 관리자 🚚", "감사관 🔎"],
        "descriptions": {
            "회계사 💼": "재무를 관리하고 투명성을 유지해요. 숫자의 수호자! 💰",
            "법무사 📜": "법적 문서를 처리하고 조언해요. 정의의 관리자! ⚖️",
            "물류 관리자 🚚": "물류 체계를 효율적으로 운영해요. 조직의 설계자! 📦",
            "감사관 🔎": "조직의 투명성을 검토해요. 진실의 감시자! 🔍"
        }
    },
    "ISFJ": {
        "jobs": ["간호사 🩺", "행정 보조 📋", "도서관 사서 📚", "유치원 교사 👶"],
        "descriptions": {
            "간호사 🩺": "환자를 돌보고 건강을 책임져요. 따뜻한 치유자! 💉",
            "행정 보조 📋": "조직의 원활한 운영을 지원해요. 세심한 조력자! 📋",
            "도서관 사서 📚": "지식을 정리하고 공유해요. 책의 수호자! 📖",
            "유치원 교사 👶": "어린이들의 성장을 돕는 멘토! 사랑의 교육자! 🧸"
        }
    },
    "ESTJ": {
        "jobs": ["관리자 🏢", "판사 ⚖️", "경찰관 👮", "금융 분석가 💰"],
        "descriptions": {
            "관리자 🏢": "조직을 체계적으로 이끌어요. 질서의 리더! 🏬",
            "판사 ⚖️": "법을 집행하고 정의를 실현해요. 공정의 수호자! ⚖️",
            "경찰관 👮": "사회 안전을 지켜요. 용감한 보호자! 🚓",
            "금융 분석가 💰": "재무 데이터를 분석해 전략을 세워요. 숫자의 전략가! 📊"
        }
    },
    "ESFJ": {
        "jobs": ["호텔 매니저 🏨", "판매원 🛍️", "커뮤니티 매니저 🌐", "이벤트 코디네이터 🎈"],
        "descriptions": {
            "호텔 매니저 🏨": "고객에게 최고의 경험을 제공해요. 환대의 마법사! 🏨",
            "판매원 🛍️": "고객과 소통하며 제품을 판매해요. 친화력의 달인! 🛍️",
            "커뮤니티 매니저 🌐": "커뮤니티를 활성화하고 연결해요. 소통의 조력자! 🌐",
            "이벤트 코디네이터 🎈": "완벽한 이벤트를 기획해요. 축제의 설계자! 🎉"
        }
    },
    "ISTP": {
        "jobs": ["엔지니어 🔧", "파일럿 ✈️", "사진작가 📸", "소방관 🚒"],
        "descriptions": {
            "엔지니어 🔧": "기술 문제를 해결하고 설계해요. 창의적 설계자! 🔩",
            "파일럿 ✈️": "하늘을 날며 안전을 책임져요. 모험의 조종사! ✈️",
            "사진작가 📸": "순간을 포착해 예술로 만들어요. 시각의 이야기꾼! 📷",
            "소방관 🚒": "위험 속에서 생명을 구해요. 용감한 영웅! 🚒"
        }
    },
    "ISFP": {
        "jobs": ["플로리스트 💐", "패션 디자이너 👗", "요리사 🍳", "그래픽 디자이너 🎨"],
        "descriptions": {
            "플로리스트 💐": "꽃으로 아름다움을 창조해요. 자연의 예술가! 🌸",
            "패션 디자이너 👗": "스타일을 창조하고 트렌드를 이끌어요. 패션의 선구자! 👗",
            "요리사 🍳": "맛으로 사람들을 행복하게 해요. 미각의 마법사! 🍴",
            "그래픽 디자이너 🎨": "시각적 콘텐츠를 디자인해요. 창의력의 화가! 🖌️"
        }
    },
    "ESTP": {
        "jobs": ["스포츠 코치 🏀", "영업 사원 💸", "응급 의료 기술자 🚑", "탐험가 🗺️"],
        "descriptions": {
            "스포츠 코치 🏀": "선수들의 잠재력을 끌어내요. 열정의 멘토! 🏅",
            "영업 사원 💸": "고객을 설득하고 거래를 성사시켜요. 협상의 달인! 💼",
            "응급 의료 기술자 🚑": "위급 상황에서 생명을 구해요. 신속의 영웅! 🚨",
            "탐험가 🗺️": "새로운 세계를 탐험해요. 모험의 개척자! 🌍"
        }
    },
    "ESFP": {
        "jobs": ["연예인 🎤", "파티 플래너 🎊", "투어 가이드 🌴", "소셜 미디어 인플루언서 📱"],
        "descriptions": {
            "연예인 🎤": "무대에서 사람들을 즐겁게 해요. 스포트라이트의 주인공! 🌟",
            "파티 플래너 🎊": "즐거운 파티를 기획해요. 축제의 마에스트로! 🎉",
            "투어 가이드 🌴": "여행자들에게 멋진 경험을 선사해요. 모험의 안내자! ✈️",
            "소셜 미디어 인플루언서 📱": "콘텐츠로 사람들을 매료시켜요. 트렌드의 선구자! 📸"
        }
    }
}

# 세션 상태로 선택된 직업 및 MBTI 관리
if 'selected_job' not in st.session_state:
    st.session_state.selected_job = None
if 'selected_mbti' not in st.session_state:
    st.session_state.selected_mbti = None

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
    st.session_state.selected_mbti = mbti
    st.session_state.selected_job = None  # 새 MBTI 선택 시 직업 초기화

# 직업 목록 표시
if st.session_state.selected_mbti:
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.markdown(f"### {st.session_state.selected_mbti}님을 위한 추천 직업! 🚀")
    for job in mbti_jobs[st.session_state.selected_mbti]["jobs"]:
        if st.button(job, key=job.replace(" ", "_"), help="클릭하면 직업 설명을 볼 수 있어요!"):
            st.session_state.selected_job = job
    st.markdown(f"**{st.session_state.selected_mbti}** 유형의 당신은 이 분야에서 빛날 거예요! 🌟 계속해서 꿈을 향해 나아가세요! 💪", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 사이드바에 직업 설명 표시
with st.sidebar:
    st.markdown("### 직업 설명 📖")
    if st.session_state.selected_job and st.session_state.selected_mbti:
        description = mbti_jobs[st.session_state.selected_mbti]["descriptions"].get(st.session_state.selected_job, "설명 준비 중이에요! 😊")
        st.markdown(f"**{st.session_state.selected_job}**")
        st.markdown(description)
    else:
        st.markdown("직업을 선택하면 여기에 설명이 나타나요! 😊")

st.markdown('</div>', unsafe_allow_html=True)

# 푸터
st.markdown("""
    <div style='text-align: center; margin-top: 30px; color: #333;'>
        <p>만든 사람: xAI와 함께하는 Grok 🌌 | 당신의 꿈을 응원합니다! 💖</p>
    </div>
""", unsafe_allow_html=True)
