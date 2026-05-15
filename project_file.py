import streamlit as st
import random
import time 
from datetime import datetime 


if 'results' not in st.session_state:
    st.session_state.results = {
        '오늘의 운세 🍀': None,
        '오늘 뭐 먹지? 🍽️': None,
        '오늘 뭐 마시지? ☕': None,
        '오늘 뭐 입지? 👕': None,
        '오늘 뭐 보지? 🎬': None,
        '오늘 우리 뭐 하지? 👫': None,
        '오늘 혼자 뭐 하지? 🏃': None,
        '오늘 뭐 듣지? 🎧': None
    }

if 'candidates_text' not in st.session_state:
    st.session_state.candidates_text = ""
if 'show_balloons' not in st.session_state:
    st.session_state.show_balloons = False

def show_seasonal_effect():
    current_month = datetime.now().month
    if current_month in [3, 4, 5]: emoji = "🌸"
    elif current_month in [6, 7, 8]: emoji = "☀️"
    elif current_month in [9, 10, 11]: emoji = "🍂"
    else: emoji = "❄️"
        
    css = f"""
    <style>
    .falling-emoji {{
        position: fixed; top: -50px; font-size: 2rem;
        user-select: none; animation: fall linear forwards; z-index: 9999;
    }}
    @keyframes fall {{
        to {{ transform: translateY(100vh); }}
    }}
    </style>
    """
    html = css
    for _ in range(20): 
        left = random.randint(0, 100)
        duration = random.uniform(2, 5)
        delay = random.uniform(0, 2)
        html += f'<div class="falling-emoji" style="left: {left}vw; animation-duration: {duration}s; animation-delay: {delay}s;">{emoji}</div>'
    st.markdown(html, unsafe_allow_html=True)

st.sidebar.title("선택 천재 앱 🔮")
user_nickname = st.sidebar.text_input("당신의 닉네임을 알려주세요!", "선택 천재")
menu = st.sidebar.radio("어떤 고민을 해결해 드릴까요?", ['오늘의 운세 🍀', '오늘 뭐 먹지? 🍽️', '오늘 뭐 마시지? ☕', '오늘 뭐 입지? 👕', '오늘 뭐 보지? 🎬', '오늘 우리 뭐 하지? 👫', '오늘 혼자 뭐 하지? 🏃', '오늘 뭐 듣지? 🎧'])

lucky_items = ["은은한 우디향 향수", "클래식 기타 피크", "파란색 양말", "뿔테 안경", "집 모양 열쇠고리", "필름 카메라", "두꺼운 전공 교재", "따뜻한 아메리카노", "보조배터리", "노란색 우산", "무선 이어폰", "은반지", "가죽 지갑", "체크무늬 셔츠", "립밤", "검은색 볼펜", "다이어리", "에코백", "비타민 음료", "핸드크림"]

food_list = [# --- 한식 (Korean) ---
    {"name": "비빔밥", "category": "한식", "weight": "라이트", "is_diet": True, "budget": 2, "laziness": 2, "note": "건강한 채소 가득"},
    {"name": "김치찌개", "category": "한식", "weight": "헤비", "is_diet": False, "budget": 1, "laziness": 3, "note": "한국인의 소울푸드"},
    {"name": "된장찌개", "category": "한식", "weight": "라이트", "is_diet": True, "budget": 1, "laziness": 3, "note": "구수하고 깔끔함"},
    {"name": "불고기", "category": "한식", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 2, "note": "달콤 짭짤한 고기"},
    {"name": "제육볶음", "category": "한식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 2, "note": "매콤한 밥도둑"},
    {"name": "보쌈", "category": "한식", "weight": "헤비", "is_diet": True, "budget": 4, "laziness": 1, "note": "기름기 뺀 건강 수육"},
    {"name": "삼겹살", "category": "한식", "weight": "헤비", "is_diet": False, "budget": 4, "laziness": 4, "note": "지글지글 고기 파티"},
    {"name": "냉면", "category": "한식", "weight": "라이트", "is_diet": False, "budget": 2, "laziness": 3, "note": "가슴까지 시원함"},
    {"name": "닭볶음탕", "category": "한식", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 4, "note": "매콤하고 든든함"},
    {"name": "삼계탕", "category": "한식", "weight": "헤비", "is_diet": True, "budget": 4, "laziness": 3, "note": "최고의 보양식"},
    {"name": "순두부찌개", "category": "한식", "weight": "라이트", "is_diet": True, "budget": 1, "laziness": 2, "note": "부드럽고 매콤함"},
    {"name": "갈비찜", "category": "한식", "weight": "헤비", "is_diet": False, "budget": 5, "laziness": 5, "note": "명절 분위기 물씬"},
    {"name": "떡볶이", "category": "한식", "weight": "헤비", "is_diet": False, "budget": 1, "laziness": 1, "note": "매콤달콤 국민 간식"},
    {"name": "육개장", "category": "한식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 3, "note": "얼큰하고 진한 국물"},
    {"name": "콩나물국밥", "category": "한식", "weight": "라이트", "is_diet": True, "budget": 1, "laziness": 1, "note": "해장에 최고"},
    {"name": "잡채", "category": "한식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 4, "note": "잔치날 필수 메뉴"},
    {"name": "감자탕", "category": "한식", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 3, "note": "푸짐한 뼈다귀 고기"},
    {"name": "육회비빔밥", "category": "한식", "weight": "라이트", "is_diet": True, "budget": 4, "laziness": 2, "note": "고소하고 신선함"},
    {"name": "곤드레밥", "category": "한식", "weight": "라이트", "is_diet": True, "budget": 2, "laziness": 2, "note": "은은한 산나물 향"},
    {"name": "추어탕", "category": "한식", "weight": "헤비", "is_diet": True, "budget": 3, "laziness": 3, "note": "진한 국물의 건강식"},

    # --- 중식 (Chinese) ---
    {"name": "짜장면", "category": "중식", "weight": "헤비", "is_diet": False, "budget": 1, "laziness": 1, "note": "이사하는 날 국룰"},
    {"name": "짬뽕", "category": "중식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 1, "note": "얼큰한 해물 국물"},
    {"name": "탕수육", "category": "중식", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 1, "note": "찍먹인가 부먹인가"},
    {"name": "마파두부", "category": "중식", "weight": "라이트", "is_diet": True, "budget": 2, "laziness": 3, "note": "부드럽고 매콤한 두부"},
    {"name": "꿔바로우", "category": "중식", "weight": "헤비", "is_diet": False, "budget": 4, "laziness": 1, "note": "쫀득한 식감이 일품"},
    {"name": "양장피", "category": "중식", "weight": "라이트", "is_diet": True, "budget": 4, "laziness": 2, "note": "코끝 찡한 겨자 소스"},
    {"name": "고추잡채", "category": "중식", "weight": "라이트", "is_diet": True, "budget": 3, "laziness": 3, "note": "꽃빵과 환상 궁합"},
    {"name": "유린기", "category": "중식", "weight": "라이트", "is_diet": False, "budget": 4, "laziness": 2, "note": "바삭하고 상큼한 치킨"},
    {"name": "마라탕", "category": "중식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 1, "note": "스트레스 날리는 매운맛"},
    {"name": "마라샹궈", "category": "중식", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 1, "note": "중독성 강한 볶음요리"},
    {"name": "딤섬", "category": "중식", "weight": "라이트", "is_diet": True, "budget": 4, "laziness": 2, "note": "한입에 쏙 육즙 가득"},
    {"name": "우육면", "category": "중식", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 2, "note": "진한 고기 국물 국수"},
    {"name": "지삼선", "category": "중식", "weight": "라이트", "is_diet": False, "budget": 2, "laziness": 3, "note": "가지 요리의 신세계"},
    {"name": "멘보샤", "category": "중식", "weight": "헤비", "is_diet": False, "budget": 4, "laziness": 2, "note": "바삭한 새우 샌드위치"},
    {"name": "볶음밥", "category": "중식", "weight": "헤비", "is_diet": False, "budget": 1, "laziness": 1, "note": "고슬고슬한 밥알"},

    # --- 일식 (Japanese) ---
    {"name": "초밥", "category": "일식", "weight": "라이트", "is_diet": True, "budget": 4, "laziness": 2, "note": "깔끔하고 신선함"},
    {"name": "돈카츠", "category": "일식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 3, "note": "겉바속촉의 정석"},
    {"name": "라멘", "category": "일식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 3, "note": "진한 돈골 국물"},
    {"name": "우동", "category": "일식", "weight": "라이트", "is_diet": False, "budget": 1, "laziness": 2, "note": "탱글탱글한 면발"},
    {"name": "사케동", "category": "일식", "weight": "라이트", "is_diet": True, "budget": 3, "laziness": 2, "note": "부드러운 연어 덮밥"},
    {"name": "규동", "category": "일식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 1, "note": "일본식 소고기 덮밥"},
    {"name": "가츠동", "category": "일식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 2, "note": "촉촉한 돈까스 덮밥"},
    {"name": "텐동", "category": "일식", "weight": "헤비", "is_diet": False, "budget": 4, "laziness": 3, "note": "비주얼 폭발 튀김 덮밥"},
    {"name": "메밀소바", "category": "일식", "weight": "라이트", "is_diet": True, "budget": 2, "laziness": 2, "note": "여름철 최고의 별미"},
    {"name": "오코노미야끼", "category": "일식", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 4, "note": "맥주를 부르는 맛"},
    {"name": "야끼소바", "category": "일식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 3, "note": "볶음면의 매력"},
    {"name": "회덮밥", "category": "일식", "weight": "라이트", "is_diet": True, "budget": 3, "laziness": 2, "note": "상큼한 초장과 회"},
    {"name": "스키야키", "category": "일식", "weight": "헤비", "is_diet": True, "budget": 5, "laziness": 4, "note": "계란물에 찍어먹는 고기"},
    {"name": "나가사키 짬뽕", "category": "일식", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 3, "note": "시원하고 뽀얀 국물"},
    {"name": "냉우동", "category": "일식", "weight": "라이트", "is_diet": False, "budget": 2, "laziness": 2, "note": "쫄깃함이 살아있음"},

    # --- 양식 (Western) ---
    {"name": "까르보나라", "category": "양식", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 3, "note": "꾸덕한 크림 파스타"},
    {"name": "알리오올리오", "category": "양식", "weight": "라이트", "is_diet": True, "budget": 2, "laziness": 2, "note": "마늘 향 가득 깔끔함"},
    {"name": "봉골레 파스타", "category": "양식", "weight": "라이트", "is_diet": True, "budget": 3, "laziness": 3, "note": "바다 향 가득 조개 파스타"},
    {"name": "티본 스테이크", "category": "양식", "weight": "헤비", "is_diet": True, "budget": 5, "laziness": 4, "note": "고급스러운 고기 파티"},
    {"name": "치즈 피자", "category": "양식", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 1, "note": "치즈가 쭈욱"},
    {"name": "치즈버거", "category": "양식", "weight": "헤비", "is_diet": False, "budget": 1, "laziness": 1, "note": "정석적인 패스트푸드"},
    {"name": "리코타 치즈 샐러드", "category": "양식", "weight": "라이트", "is_diet": True, "budget": 2, "laziness": 2, "note": "신선하고 고소함"},
    {"name": "수비드 닭가슴살 샐러드", "category": "양식", "weight": "라이트", "is_diet": True, "budget": 2, "laziness": 2, "note": "다이어터의 축복"},
    {"name": "라자냐", "category": "양식", "weight": "헤비", "is_diet": False, "budget": 4, "laziness": 5, "note": "치즈와 고기 층층이"},
    {"name": "뇨끼", "category": "양식", "weight": "헤비", "is_diet": False, "budget": 4, "laziness": 4, "note": "쫀득한 감자 반죽"},
    {"name": "프렌치 토스트", "category": "양식", "weight": "라이트", "is_diet": False, "budget": 2, "laziness": 2, "note": "달콤한 브런치"},
    {"name": "에그 베네딕트", "category": "양식", "weight": "라이트", "is_diet": False, "budget": 4, "laziness": 4, "note": "고급스러운 브런치 정석"},
    {"name": "피쉬 앤 칩스", "category": "양식", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 3, "note": "영국의 맛"},
    {"name": "감바스 알 아히요", "category": "양식", "weight": "라이트", "is_diet": False, "budget": 3, "laziness": 2, "note": "새우와 마늘의 환상 조화"},
    {"name": "클램 차우더 스프", "category": "양식", "weight": "라이트", "is_diet": False, "budget": 2, "laziness": 3, "note": "부드럽고 따뜻한 스프"},

    # --- 동남아식 (Asian) ---
    {"name": "팟타이", "category": "동남아식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 2, "note": "태국식 볶음 쌀국수"},
    {"name": "나시고랭", "category": "동남아식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 2, "note": "인도네시아식 볶음밥"},
    {"name": "쌀국수", "category": "동남아식", "weight": "라이트", "is_diet": True, "budget": 2, "laziness": 2, "note": "담백한 베트남의 맛"},
    {"name": "분짜", "category": "동남아식", "weight": "라이트", "is_diet": True, "budget": 3, "laziness": 2, "note": "새콤달콤 소스에 찍어먹기"},
    {"name": "푸팟퐁커리", "category": "동남아식", "weight": "헤비", "is_diet": False, "budget": 5, "laziness": 4, "note": "부드러운 게살 커리"},
    {"name": "똠양꿍", "category": "동남아식", "weight": "라이트", "is_diet": True, "budget": 4, "laziness": 3, "note": "세계 3대 스포"},
    {"name": "월남쌈", "category": "동남아식", "weight": "라이트", "is_diet": True, "budget": 4, "laziness": 5, "note": "직접 싸먹는 재미와 건강"},
    {"name": "공심채 볶음", "category": "동남아식", "weight": "라이트", "is_diet": True, "budget": 2, "laziness": 1, "note": "아삭아삭한 밥반찬"},
    {"name": "미고랭", "category": "동남아식", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 2, "note": "중독성 있는 볶음면"},
    {"name": "반미 샌드위치", "category": "동남아식", "weight": "라이트", "is_diet": False, "budget": 2, "laziness": 1, "note": "바게트 속 베트남 감성"},

    # --- 퓨전 & 기타 (Fusion/Other) ---
    {"name": "김치 치즈 도리아", "category": "퓨전", "weight": "헤비", "is_diet": False, "budget": 2, "laziness": 3, "note": "김치와 치즈의 만남"},
    {"name": "명란 크림 파스타", "category": "퓨전", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 3, "note": "짭조름하고 고소함"},
    {"name": "불고기 피자", "category": "퓨전", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 1, "note": "동서양의 조화"},
    {"name": "치즈 닭갈비", "category": "퓨전", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 4, "note": "매콤 고소함의 끝판왕"},
    {"name": "베이컨 김치볶음밥", "category": "퓨전", "weight": "헤비", "is_diet": False, "budget": 1, "laziness": 2, "note": "실패 없는 메뉴"},
    {"name": "카레라이스", "category": "퓨전", "weight": "헤비", "is_diet": True, "budget": 1, "laziness": 2, "note": "든든하고 건강한 한그릇"},
    {"name": "치킨 마요 덮밥", "category": "퓨전", "weight": "헤비", "is_diet": False, "budget": 1, "laziness": 1, "note": "도시락 스테디셀러"},

    # --- 디저트 (Dessert) ---
    {"name": "그릭 요거트 볼", "category": "디저트", "weight": "라이트", "is_diet": True, "budget": 3, "laziness": 1, "note": "건강하고 꾸덕함"},
    {"name": "과일 타르트", "category": "디저트", "weight": "라이트", "is_diet": False, "budget": 4, "laziness": 1, "note": "상큼하고 예쁜 디저트"},
    {"name": "조각 케이크", "category": "디저트", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 1, "note": "당 충전 100%"},
    {"name": "마카롱", "category": "디저트", "weight": "라이트", "is_diet": False, "budget": 2, "laziness": 1, "note": "작고 달콤한 행복"},
    {"name": "빙수", "category": "디저트", "weight": "헤비", "is_diet": False, "budget": 4, "laziness": 2, "note": "여름철 필수 코스"},
    {"name": "크로플", "category": "디저트", "weight": "헤비", "is_diet": False, "budget": 3, "laziness": 2, "note": "겉은 바삭 속은 쫀득"},
    {"name": "츄러스", "category": "디저트", "weight": "라이트", "is_diet": False, "budget": 1, "laziness": 1, "note": "시나몬 향 솔솔"},
    {"name": "아이스크림", "category": "디저트", "weight": "라이트", "is_diet": False, "budget": 2, "laziness": 1, "note": "언제 먹어도 시원함"}]

together_list = [
    # ── 감성 카페 / 브런치 ──────────────────────────────────────────
    {"name": "숨겨진 북카페에서 책 읽기", "meeting_type": "데이트", "awkwardness": 2, "crowd": 1, "energy": 1, "mobility": 1, "note": "조용한 분위기, 대화 깊어짐"},
    {"name": "루프탑 카페에서 야경 감상", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 1, "mobility": 2, "note": "분위기 최고, 인증샷 필수"},
    {"name": "대형 브런치 카페에서 늦은 아침", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 1, "mobility": 2, "note": "주말 브런치 감성"},
    {"name": "한옥 카페에서 전통차 마시기", "meeting_type": "데이트", "awkwardness": 2, "crowd": 2, "energy": 1, "mobility": 2, "note": "고즈넉한 분위기, 찐 감성"},
    {"name": "테마 카페 투어 (고양이·강아지)", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 1, "note": "동물 힐링, 대화 무한"},
    {"name": "동네 작은 독립 카페 탐방", "meeting_type": "공통", "awkwardness": 2, "crowd": 1, "energy": 2, "mobility": 1, "note": "감성 스팟, 사진 예쁨"},
    {"name": "공방 겸 카페에서 도자기 체험", "meeting_type": "데이트", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 2, "note": "체험+카페 원스톱"},
    {"name": "스페셜티 커피 바에서 핸드드립 체험", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 1, "note": "커피 덕후 코스"},
    {"name": "뷰 맛집 카페에서 일몰 보기", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 1, "mobility": 3, "note": "골든아워 황금 타이밍"},
    {"name": "감성 폴라로이드 카페 방문", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 2, "mobility": 1, "note": "추억 즉석 사진"},
    {"name": "팝업 카페·한정 메뉴 오픈런", "meeting_type": "공통", "awkwardness": 3, "crowd": 5, "energy": 2, "mobility": 1, "note": "줄서기 공동 운명체"},
    {"name": "와플·크로플 맛집 카페 탐방", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 1, "mobility": 2, "note": "당 충전 필수"},
    {"name": "인생 네컷·포토부스 투어", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 1, "note": "추억 남기기 최고"},
    {"name": "LP 카페에서 바이닐 감상", "meeting_type": "데이트", "awkwardness": 2, "crowd": 2, "energy": 1, "mobility": 1, "note": "아날로그 감성 폭발"},
    {"name": "빵지순례 베이커리 카페 3곳 투어", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 2, "note": "걸으며 먹는 재미"},
    {"name": "디저트 카페 3곳 스탬프 투어", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 2, "note": "당도 MAX, 행복 MAX"},
    {"name": "셀프 사진관에서 콘셉트 촬영", "meeting_type": "공통", "awkwardness": 1, "crowd": 1, "energy": 2, "mobility": 1, "note": "사진 찍으며 친해지기"},
    {"name": "아이스크림 가게 투어", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 2, "note": "여름 필수 코스"},
    {"name": "테이스팅 바에서 와인·막걸리 페어링", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 1, "mobility": 1, "note": "분위기 있는 어른 데이트"},
    {"name": "대형 서점 카페에서 책 고르기", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 1, "mobility": 1, "note": "서로 고른 책 선물하기"},

    # ── 맛집 / 식사 투어 ────────────────────────────────────────────
    {"name": "오마카세 레스토랑 도전", "meeting_type": "데이트", "awkwardness": 4, "crowd": 1, "energy": 1, "mobility": 1, "note": "특별한 날 플렉스"},
    {"name": "야시장·포장마차 거리 투어", "meeting_type": "공통", "awkwardness": 2, "crowd": 5, "energy": 3, "mobility": 2, "note": "서서 먹는 재미"},
    {"name": "전통 시장 음식 탐방", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 3, "mobility": 1, "note": "인심 가득, 저렴"},
    {"name": "스시 오마카세 도전", "meeting_type": "데이트", "awkwardness": 4, "crowd": 1, "energy": 1, "mobility": 1, "note": "고급 분위기 최고"},
    {"name": "국밥 투어 (유명 국밥집 3곳)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 2, "mobility": 3, "note": "찐 친구와 국밥 논쟁"},
    {"name": "새벽 노량진 수산시장 회 떠먹기", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 4, "energy": 3, "mobility": 2, "note": "새벽 감성 + 신선도 MAX"},
    {"name": "BBQ 파티 (옥상·공원)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 4, "energy": 4, "mobility": 3, "note": "직접 굽는 재미"},
    {"name": "1인 1닭 치킨 파티", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 4, "energy": 2, "mobility": 1, "note": "배달 파티의 정석"},
    {"name": "유명 라멘집 웨이팅 도전", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 2, "mobility": 1, "note": "웨이팅 중 대화 보장"},
    {"name": "뷔페 정복하기 (점심 런치)", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 2, "mobility": 2, "note": "가성비 폭식 타임"},
    {"name": "고기집 소고기 플렉스", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 1, "note": "고기 앞에선 어색함 없음"},
    {"name": "해산물 레스토랑 코스 요리", "meeting_type": "데이트", "awkwardness": 4, "crowd": 2, "energy": 1, "mobility": 2, "note": "고급 분위기 데이트"},
    {"name": "이자카야에서 일본 요리 코스", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 1, "note": "꼬치+술 완벽 조합"},
    {"name": "핫도그·길거리 음식 투어", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 2, "note": "먹방 유튜버 코스"},
    {"name": "곱창·막창집 도전", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 2, "mobility": 1, "note": "소주 한 잔 필수"},
    {"name": "쌀국수 전문점 탐방", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 1, "mobility": 2, "note": "베트남 감성"},
    {"name": "파인다이닝 레스토랑 예약", "meeting_type": "데이트", "awkwardness": 4, "crowd": 1, "energy": 1, "mobility": 1, "note": "드레스코드 있는 특별한 날"},
    {"name": "타코·멕시칸 레스토랑 탐방", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 2, "note": "이국적 메뉴 탐험"},
    {"name": "전골·샤브샤브 전문점 방문", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 2, "note": "겨울 최강 메뉴"},
    {"name": "백반집 투어 (동네 할머니 백반)", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 1, "mobility": 2, "note": "집밥 그리울 때"},
    {"name": "중식 코스 요리 도전", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 1, "mobility": 1, "note": "탕수육 부먹 vs 찍먹 논쟁"},
    {"name": "브런치 투어 (성수·망원)", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 1, "note": "핫플 성지순례"},
    {"name": "홍대 음식 거리 탐방", "meeting_type": "공통", "awkwardness": 2, "crowd": 5, "energy": 3, "mobility": 1, "note": "먹거리 천국"},
    {"name": "인도 커리 전문점 방문", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 1, "mobility": 2, "note": "이색 요리 탐험"},
    {"name": "마라 핫팟 전문점 도전", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 2, "note": "매운 음식 함께 도전"},
    {"name": "이탈리안 레스토랑 파스타 탐방", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 1, "mobility": 2, "note": "낭만적 이탈리아 분위기"},
    {"name": "스페인 타파스 바 방문", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 1, "note": "와인과 함께 소소한 메뉴"},
    {"name": "해물 파전에 막걸리 한 사발", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 2, "mobility": 2, "note": "비 오는 날 필수 코스"},
    {"name": "족발·보쌈 맛집 탐방", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 2, "mobility": 2, "note": "배달보다 현장이 맛있어"},
    {"name": "낙지·해물 볶음 전문점", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 2, "mobility": 2, "note": "매운 걸 이겨내는 공동체"},
    {"name": "치즈 전문 레스토랑 방문", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 1, "mobility": 2, "note": "치즈 늘리기 인증샷"},

    # ── 실내 엔터테인먼트 ────────────────────────────────────────────
    {"name": "방탈출 카페 도전 (2인)", "meeting_type": "데이트", "awkwardness": 2, "crowd": 1, "energy": 3, "mobility": 1, "note": "협력으로 어색함 타파"},
    {"name": "방탈출 카페 도전 (단체)", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 1, "note": "팀워크 테스트"},
    {"name": "보드게임 카페 (2인용 전략 게임)", "meeting_type": "데이트", "awkwardness": 2, "crowd": 2, "energy": 2, "mobility": 1, "note": "두뇌 싸움으로 친해지기"},
    {"name": "보드게임 카페 (파티 게임)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 3, "mobility": 1, "note": "웃음 보장 파티"},
    {"name": "노래방 (코인 or 일반)", "meeting_type": "공통", "awkwardness": 1, "crowd": 2, "energy": 4, "mobility": 1, "note": "스트레스 해소 국룰"},
    {"name": "VR 카페 체험", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 3, "mobility": 2, "note": "가상 현실 공동 체험"},
    {"name": "PC방 팀게임 대결", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 4, "energy": 2, "mobility": 1, "note": "롤·배그 뚝배기 깨기"},
    {"name": "오락실·게임센터 탐방", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 3, "mobility": 1, "note": "90년대 감성 부활"},
    {"name": "다트 바에서 대결", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 1, "note": "내기 하며 친해지기"},
    {"name": "탁구장 대결", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 4, "mobility": 2, "note": "운동+재미 동시에"},
    {"name": "미니 골프 (스크린 or 실내)", "meeting_type": "공통", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 2, "note": "누구나 할 수 있는 레저"},
    {"name": "클라이밍 짐 초보 코스", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 5, "mobility": 2, "note": "성취감 폭발, 서로 응원"},
    {"name": "스크린 야구 배팅", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 2, "note": "내기 배팅으로 긴장감"},
    {"name": "볼링장 대결 (3게임)", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 3, "mobility": 2, "note": "스트라이크 자랑하기"},
    {"name": "방방 트램폴린 파크", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 5, "mobility": 3, "note": "어른도 신나는 방방"},
    {"name": "실내 서핑 체험 (웨이브풀)", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 5, "mobility": 3, "note": "이색 액티비티 도전"},
    {"name": "레이저 태그(레이저 건 전쟁)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 4, "energy": 4, "mobility": 3, "note": "팀 vs 팀 대결"},
    {"name": "방 안에서 방탈출 앱 게임", "meeting_type": "공통", "awkwardness": 2, "crowd": 1, "energy": 1, "mobility": 1, "note": "집에서도 즐기는 방탈출"},
    {"name": "닌텐도 스위치 파티 게임", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 1, "energy": 2, "mobility": 1, "note": "마리오 파티 찐친 테스트"},
    {"name": "심리 테스트·MBTI 토크", "meeting_type": "공통", "awkwardness": 4, "crowd": 1, "energy": 1, "mobility": 1, "note": "서로 알아가기 최고"},
    {"name": "스피드 퀴즈·퀴즈쇼 게임", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 2, "energy": 2, "mobility": 1, "note": "두뇌 풀가동 웃음판"},
    {"name": "카드게임 (러미·포커·고스톱)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 2, "energy": 1, "mobility": 1, "note": "내기는 금물(농담)"},
    {"name": "넷플릭스 같은 영화 동시 시청", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 1, "mobility": 1, "note": "원격도 가능한 데이트"},
    {"name": "방구석 뮤직 스테이션 (유튜브 반주 노래)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 1, "energy": 3, "mobility": 1, "note": "코노 못 가도 우리가 코노"},
    {"name": "영화관 개봉작 보기", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 1, "mobility": 1, "note": "정석 데이트·약속 코스"},
    {"name": "CGV 스페셜관 (4DX·IMAX) 체험", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 2, "note": "영화관에서 놀이기구"},
    {"name": "독립영화관 예술 영화 감상", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 1, "mobility": 1, "note": "영화 후 카페 토론 필수"},
    {"name": "심야 영화 관람 (자정 상영)", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 1, "mobility": 1, "note": "자정의 시네마 감성"},
    {"name": "당구장에서 포켓볼 대결", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 1, "note": "스킬 차이로 웃음 폭발"},
    {"name": "방 안에서 UNO·할리갈리 대결", "meeting_type": "공통", "awkwardness": 1, "crowd": 1, "energy": 2, "mobility": 1, "note": "카드게임으로 모임 흥기"},

    # ── 문화 / 예술 ─────────────────────────────────────────────────
    {"name": "현대 미술관 전시 관람", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 2, "note": "서로 해석 다름 = 대화 소재"},
    {"name": "사진 전시회 관람", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 1, "note": "감성 충전 + 인증샷"},
    {"name": "국립중앙박물관 탐방", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 2, "note": "무료 관람, 역사 교양"},
    {"name": "팝업 스토어 투어 (성수·홍대)", "meeting_type": "공통", "awkwardness": 3, "crowd": 5, "energy": 3, "mobility": 1, "note": "브랜드 체험 + 굿즈 득템"},
    {"name": "연극 공연 관람", "meeting_type": "데이트", "awkwardness": 4, "crowd": 3, "energy": 1, "mobility": 1, "note": "공연 후 카페 감상 토크"},
    {"name": "뮤지컬 관람", "meeting_type": "데이트", "awkwardness": 4, "crowd": 3, "energy": 1, "mobility": 1, "note": "OST 같이 흥얼거리기"},
    {"name": "인디 밴드 공연 관람", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 3, "mobility": 1, "note": "감성 충만 라이브 음악"},
    {"name": "클래식 음악회 관람", "meeting_type": "데이트", "awkwardness": 4, "crowd": 3, "energy": 1, "mobility": 1, "note": "드레스코드 준비, 고급짐"},
    {"name": "야외 페스티벌 참가", "meeting_type": "공통", "awkwardness": 2, "crowd": 5, "energy": 4, "mobility": 4, "note": "여름 페스 분위기 최고"},
    {"name": "재즈 바 방문", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 1, "mobility": 1, "note": "어른의 밤, 재즈 감성"},
    {"name": "아이돌 콘서트 참가", "meeting_type": "공통", "awkwardness": 1, "crowd": 5, "energy": 5, "mobility": 2, "note": "응원봉 흔들며 하나 됨"},
    {"name": "힙합 클럽 공연 관람", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 5, "energy": 4, "mobility": 1, "note": "밤새 에너지 방전"},
    {"name": "버스킹 공연 구경 (홍대·인사동)", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 2, "mobility": 1, "note": "즉흥 문화 충전"},
    {"name": "세계 문화 축제 참가", "meeting_type": "공통", "awkwardness": 3, "crowd": 5, "energy": 3, "mobility": 3, "note": "이국적 음식·공연 체험"},
    {"name": "독립 서점 투어 + 굿즈 구매", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 2, "note": "책 선물로 감성 포인트"},
    {"name": "인문학 강연·토크쇼 참가", "meeting_type": "공통", "awkwardness": 4, "crowd": 3, "energy": 1, "mobility": 2, "note": "지적 대화의 시작점"},
    {"name": "갤러리 오프닝 파티 참가", "meeting_type": "데이트", "awkwardness": 4, "crowd": 4, "energy": 2, "mobility": 1, "note": "와인+예술 조합"},
    {"name": "도자기 공방 원데이 클래스", "meeting_type": "데이트", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 2, "note": "흙 만지며 어색함 타파"},
    {"name": "캘리그라피 체험 클래스", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 2, "note": "집중하다 보면 친해짐"},
    {"name": "수채화·유화 원데이 클래스", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 2, "note": "그린 그림 선물하기"},

    # ── 야외 / 공원 / 산책 ──────────────────────────────────────────
    {"name": "한강 공원 돗자리 피크닉", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 2, "mobility": 1, "note": "편의점 음식 필수"},
    {"name": "한강 자전거 라이딩", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 4, "mobility": 1, "note": "따릉이 빌려서 라이딩"},
    {"name": "경복궁·창덕궁 한복 투어", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 1, "note": "한복 입으면 어색함 사라짐"},
    {"name": "남산 케이블카+N서울타워", "meeting_type": "데이트", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 1, "note": "야경+자물쇠 사랑 클리셰"},
    {"name": "북촌 한옥마을 골목 산책", "meeting_type": "데이트", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 1, "note": "사진 찍으며 걷기"},
    {"name": "서울 숲·보라매 공원 산책", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 1, "note": "반려동물 구경 보너스"},
    {"name": "인왕산·북한산 가볍게 등산", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 4, "mobility": 2, "note": "정상에서 막걸리 한 잔"},
    {"name": "하늘공원·노을공원 일몰 감상", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 2, "note": "억새밭 골든아워"},
    {"name": "올림픽공원 조깅·피크닉", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 3, "mobility": 2, "note": "넓은 잔디밭에서 힐링"},
    {"name": "별빛 야경 포인트 투어", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 3, "note": "드라이브 야경 코스"},
    {"name": "벚꽃 명소 산책 (봄 한정)", "meeting_type": "공통", "awkwardness": 3, "crowd": 5, "energy": 3, "mobility": 2, "note": "분홍빛 봄날의 로망"},
    {"name": "단풍 명소 산책 (가을 한정)", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 3, "note": "가을 낭만 감성 충전"},
    {"name": "식물원·수목원 탐방", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 3, "note": "초록 힐링 + 사진"},
    {"name": "해수욕장 낮 해변 산책", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 5, "note": "바닷바람 맞으며 힐링"},
    {"name": "별 관찰 (천문대·야외)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 2, "mobility": 4, "note": "낭만 MAX, 이야기 소재 무궁무진"},
    {"name": "공원 플로깅 (쓰레기 줍기 산책)", "meeting_type": "공통", "awkwardness": 3, "crowd": 2, "energy": 3, "mobility": 2, "note": "환경+건강+뿌듯함"},
    {"name": "동네 골목 카페 산책 투어", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 1, "note": "숨은 명소 발굴"},
    {"name": "야간 한강 산책 + 편의점 야식", "meeting_type": "데이트", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 1, "note": "새벽 감성 최고"},
    {"name": "새벽 일출 보러 가기", "meeting_type": "데이트", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 4, "note": "함께 기억에 남을 장면"},
    {"name": "식물 마켓·플리마켓 구경", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 2, "mobility": 2, "note": "소품 득템 탐험"},

    # ── 드라이브 / 근교 여행 ────────────────────────────────────────
    {"name": "드라이브 (한강변 야경 코스)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 1, "mobility": 5, "note": "음악 틀고 드라이브 감성"},
    {"name": "가평·춘천 당일 기차 여행", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 4, "note": "닭갈비+막국수 코스"},
    {"name": "강릉 당일치기 바다 드라이브", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 5, "note": "커피거리+해변"},
    {"name": "남이섬 나들이", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 4, "note": "메타세쿼이아 명소"},
    {"name": "제주도 1박 2일 여행", "meeting_type": "데이트", "awkwardness": 4, "crowd": 3, "energy": 4, "mobility": 5, "note": "렌터카 필수, 해변+흑돼지"},
    {"name": "전주 한옥마을 당일 투어", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 5, "note": "한복+콩나물국밥"},
    {"name": "경주 역사 유적지 투어", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 5, "note": "첨성대·불국사 감성"},
    {"name": "부산 해운대 당일치기", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 5, "note": "밀면+씨앗호떡"},
    {"name": "파주 출판도시+헤이리 예술마을", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 4, "note": "책+예술 감성 투어"},
    {"name": "용인 에버랜드 하루 종일", "meeting_type": "공통", "awkwardness": 2, "crowd": 5, "energy": 5, "mobility": 4, "note": "놀이기구+퍼레이드"},
    {"name": "수원 화성 성곽길 산책", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 4, "note": "역사 나들이, 근교 최적"},
    {"name": "양평 카페거리 드라이브", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 5, "note": "강변 카페 힐링 코스"},
    {"name": "인천 차이나타운+월미도", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 3, "note": "짜장면+바닷가"},
    {"name": "속초 낙산사+해수욕장", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 5, "note": "바다+아바이 순대"},
    {"name": "여수 돌산도 밤바다 투어", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 5, "note": "낭만 포차 해산물"},
    {"name": "태안 안면도 꽃 축제", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 2, "mobility": 5, "note": "봄 튤립 장관"},
    {"name": "담양 죽녹원 산책 드라이브", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 5, "note": "대나무 숲 인스타 명소"},
    {"name": "통영 케이블카+해산물 투어", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 5, "note": "뷰+굴구이"},
    {"name": "제천 의림지+청풍호 드라이브", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 5, "note": "숨겨진 근교 명소"},
    {"name": "홍천 에델바이스 스위스 테마파크", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 5, "note": "이색 감성 근교"},
    {"name": "임진각 평화 누리 공원 나들이", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 4, "note": "역사+힐링"},
    {"name": "대부도 조개구이 드라이브", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 5, "note": "조개+소주 조합"},
    {"name": "정동진 일출 여행 (1박)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 5, "note": "기차+일출 낭만"},
    {"name": "남해 독일 마을 드라이브", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 5, "note": "이국적 풍경"},
    {"name": "순천만 갈대밭 드라이브", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 5, "note": "가을 황금빛 장관"},

    # ── 스포츠 / 액티비티 ────────────────────────────────────────────
    {"name": "테니스 레슨 체험 (초보)", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 4, "mobility": 3, "note": "유행 스포츠 함께 배우기"},
    {"name": "배드민턴 공원 대결", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 4, "mobility": 2, "note": "공원 셔틀콕 날리기"},
    {"name": "풋살 (소규모 축구)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 5, "mobility": 3, "note": "땀 뻘뻘 친목"},
    {"name": "농구 3대3 대결", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 5, "mobility": 2, "note": "팀 vs 팀 불꽃 경쟁"},
    {"name": "스케이트장 (실내/야외)", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 4, "mobility": 3, "note": "넘어지며 자연스럽게 밀착"},
    {"name": "스키장·스노보드 시즌권", "meeting_type": "공통", "awkwardness": 2, "crowd": 5, "energy": 5, "mobility": 5, "note": "겨울 레저의 꽃"},
    {"name": "워터파크 여름 나들이", "meeting_type": "공통", "awkwardness": 2, "crowd": 5, "energy": 5, "mobility": 4, "note": "슬라이드+파도풀"},
    {"name": "서핑 입문 레슨 (양양·부산)", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 5, "mobility": 5, "note": "파도 위에서 친해지기"},
    {"name": "래프팅 체험 (인제·화천)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 5, "mobility": 5, "note": "비명과 웃음의 공존"},
    {"name": "번지점프 도전 (가평)", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 5, "mobility": 5, "note": "공포 공유로 극도로 친해짐"},
    {"name": "패러글라이딩 체험 (단양)", "meeting_type": "공통", "awkwardness": 3, "crowd": 2, "energy": 4, "mobility": 5, "note": "하늘에서 보는 뷰"},
    {"name": "카약·SUP 체험 (강/바다)", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 4, "mobility": 5, "note": "물 위 힐링 액티비티"},
    {"name": "ATV 오프로드 체험", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 2, "energy": 4, "mobility": 5, "note": "흙탕물 무서운 거 없음"},
    {"name": "짚라인 체험 (산 속)", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 4, "mobility": 5, "note": "스릴 공유 = 유대감"},
    {"name": "요가·필라테스 클래스 함께", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 3, "mobility": 2, "note": "함께 건강해지는 루틴"},
    {"name": "러닝 크루 참가 (한강)", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 4, "mobility": 1, "note": "뛰면서 어색함 타파"},
    {"name": "폴댄스 일일 체험", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 5, "mobility": 2, "note": "색다른 댄스 체험"},
    {"name": "K-POP 댄스 클래스 참가", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 4, "mobility": 2, "note": "아이돌 안무 함께 배우기"},
    {"name": "볼더링 (클라이밍) 초급 코스", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 5, "mobility": 2, "note": "서로 등반 응원하기"},
    {"name": "수영장 자유수영 (실내)", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 3, "energy": 4, "mobility": 2, "note": "레인 경쟁하며 친해짐"},
    {"name": "야구장 직관 (1루·3루 응원단)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 5, "energy": 4, "mobility": 2, "note": "응원가+치맥 조합"},
    {"name": "축구장 직관 K리그", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 5, "energy": 4, "mobility": 3, "note": "응원봉 없어도 열정"},
    {"name": "농구장 직관 KBL 경기", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 4, "energy": 3, "mobility": 3, "note": "실내라 쾌적한 관람"},
    {"name": "당구·스누커 카페 대결", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 2, "mobility": 1, "note": "큐 잡는 법부터 배우기"},
    {"name": "사격 체험장 방문", "meeting_type": "공통", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 3, "note": "첫 사격 긴장감 공유"},
    {"name": "승마 체험 (초급 코스)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 3, "mobility": 5, "note": "말 위에서 고귀한 분위기"},
    {"name": "스킨스쿠버 다이빙 체험", "meeting_type": "공통", "awkwardness": 3, "crowd": 2, "energy": 4, "mobility": 5, "note": "수중 세계 함께 탐험"},
    {"name": "스탠드업 패들 보드 (SUP) 체험", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 3, "mobility": 5, "note": "물 위에서 요가처럼"},
    {"name": "암벽등반 체험장 방문", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 2, "energy": 5, "mobility": 4, "note": "팀워크로 꼭대기 정복"},
    {"name": "마라톤 대회 함께 참가 (5km)", "meeting_type": "공통", "awkwardness": 2, "crowd": 5, "energy": 5, "mobility": 3, "note": "완주 후 삼겹살 파티"},

    # ── 체험 클래스 ─────────────────────────────────────────────────
    {"name": "향수 조향 클래스", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 2, "mobility": 2, "note": "서로만의 향 만들기"},
    {"name": "베이킹 원데이 클래스", "meeting_type": "데이트", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 2, "note": "만든 빵 나눠 먹기"},
    {"name": "떡 만들기 체험 클래스", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 3, "note": "전통 체험 + 소확행"},
    {"name": "소시지·샤르퀴트리 만들기 클래스", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 3, "note": "직접 만든 소시지 맛집"},
    {"name": "김치 만들기 체험", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 3, "note": "K-문화 체험, 외국인 코스"},
    {"name": "초콜릿·봉봉 만들기 클래스", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 2, "note": "달콤한 선물 만들기"},
    {"name": "드립 커피 마스터 클래스", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 2, "note": "커피 이야기로 대화 풍성"},
    {"name": "수제 맥주 브루잉 클래스", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 3, "note": "직접 빚은 맥주 마시기"},
    {"name": "목공 원데이 클래스 (미니 선반)", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 3, "note": "직접 만든 작품 집에 가져가기"},
    {"name": "가죽 공예 클래스 (카드지갑)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 2, "mobility": 2, "note": "핸드메이드 선물 교환"},
    {"name": "유리 공예 클래스 (퓨징)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 2, "mobility": 2, "note": "빛 투과되는 나만의 작품"},
    {"name": "도자기 물레 체험", "meeting_type": "데이트", "awkwardness": 2, "crowd": 1, "energy": 3, "mobility": 2, "note": "Ghost 명장면 재현"},
    {"name": "테라리움 만들기 클래스", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 2, "note": "작은 정원 만들어 선물"},
    {"name": "리본·플라워 클래스 (꽃다발)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 2, "energy": 2, "mobility": 2, "note": "만든 꽃다발 바로 선물"},
    {"name": "압화·드라이플라워 액자 만들기", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 2, "mobility": 2, "note": "집에 걸어두는 추억"},
    {"name": "실크 스크린 프린팅 티셔츠 제작", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 3, "mobility": 2, "note": "커플·그룹 굿즈 제작"},
    {"name": "소이 캔들 만들기 클래스", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 2, "note": "향과 색 조합 취향 공유"},
    {"name": "마크라메 (매듭 공예) 클래스", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 2, "note": "집중하다 보면 자연스러워짐"},
    {"name": "매직·마술 클래스 (입문)", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 3, "energy": 3, "mobility": 2, "note": "마술로 분위기 띄우기"},
    {"name": "요리 클래스 (이탈리안·태국)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 3, "mobility": 2, "note": "직접 요리한 밥 먹기"},

    # ── 술자리 / 나이트라이프 ────────────────────────────────────────
    {"name": "홈 칵테일 파티", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 1, "energy": 3, "mobility": 1, "note": "각자 칵테일 한 가지씩 만들기"},
    {"name": "루프탑 바 야경 칵테일", "meeting_type": "데이트", "awkwardness": 4, "crowd": 3, "energy": 2, "mobility": 1, "note": "야경+칵테일 분위기 최고"},
    {"name": "홍대 클럽 나이트", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 5, "energy": 5, "mobility": 1, "note": "밤새 댄스 에너지"},
    {"name": "이태원 바 투어 (펍 크롤링)", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 4, "energy": 3, "mobility": 1, "note": "3곳 이상 순례"},
    {"name": "보드게임 바 방문", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 1, "note": "술+게임 최고 조합"},
    {"name": "포장마차 호프 + 치킨", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 4, "energy": 2, "mobility": 1, "note": "퇴근 후 국룰 코스"},
    {"name": "일본식 이자카야 방문", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 1, "note": "꼬치+하이볼 조합"},
    {"name": "와인 바 방문 (내추럴 와인)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 2, "energy": 1, "mobility": 1, "note": "어른스러운 대화 분위기"},
    {"name": "위스키 바 방문", "meeting_type": "데이트", "awkwardness": 4, "crowd": 2, "energy": 1, "mobility": 1, "note": "위스키 종류 탐구하기"},
    {"name": "막걸리 양조장 투어+시음", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 2, "mobility": 4, "note": "전통주 교양 쌓기"},
    {"name": "맥주 브루어리 직접 방문", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 3, "note": "갓 나온 생맥주 맛"},
    {"name": "전통주 테이스팅 바 방문", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 1, "mobility": 1, "note": "다양한 전통주 비교"},
    {"name": "라이브 재즈 바 방문", "meeting_type": "데이트", "awkwardness": 4, "crowd": 3, "energy": 1, "mobility": 1, "note": "음악 들으며 대화"},
    {"name": "노래방 + 치킨 배달 파티", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 2, "energy": 4, "mobility": 1, "note": "노코노코 조합"},
    {"name": "홈파티 (각자 음식 한 가지씩)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 3, "mobility": 1, "note": "팟럭 파티"},
    {"name": "숙소 파티 (에어비앤비 1박)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 4, "mobility": 3, "note": "밤새 파티 + 아침 해장"},
    {"name": "와인 + 치즈 홈파티", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 1, "mobility": 1, "note": "집에서 즐기는 프렌치 감성"},
    {"name": "옥상 바베큐 + 맥주 파티", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 3, "mobility": 2, "note": "여름 옥상 파티 필수"},
    {"name": "감성 포차 방문 (한강변)", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 2, "mobility": 2, "note": "야경+소주 감성"},
    {"name": "생맥주 크래프트 비어 바", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 2, "note": "각자 취향 맥주 골라보기"},

    # ── 숙박 / 여행 ─────────────────────────────────────────────────
    {"name": "호캉스 (서울 시내 특급 호텔)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 1, "energy": 1, "mobility": 2, "note": "룸서비스+수영장 풀코스"},
    {"name": "감성 펜션 1박 2일 (경기도)", "meeting_type": "공통", "awkwardness": 2, "crowd": 1, "energy": 3, "mobility": 5, "note": "바베큐+별보기"},
    {"name": "글램핑 1박 (화성·가평)", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 5, "note": "럭셔리 캠핑 감성"},
    {"name": "오토 캠핑 (강원도)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 2, "energy": 4, "mobility": 5, "note": "짐 싣고 자연 속으로"},
    {"name": "에어비앤비 독채 1박 파티", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 4, "mobility": 4, "note": "우리만의 공간 파티"},
    {"name": "제주도 2박 3일 렌터카 여행", "meeting_type": "데이트", "awkwardness": 4, "crowd": 3, "energy": 4, "mobility": 5, "note": "해안 도로 드라이브"},
    {"name": "강원도 리조트 스키 1박 2일", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 5, "mobility": 5, "note": "스키+온천+바베큐"},
    {"name": "부산 해운대 호텔 1박", "meeting_type": "데이트", "awkwardness": 4, "crowd": 3, "energy": 3, "mobility": 5, "note": "바다뷰 호텔 낭만"},
    {"name": "경주 한옥 스테이 1박", "meeting_type": "데이트", "awkwardness": 4, "crowd": 2, "energy": 2, "mobility": 5, "note": "전통 숙박 체험"},
    {"name": "해외 여행 (일본 도쿄 3박)", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 4, "mobility": 5, "note": "라멘+편의점+온천"},
    {"name": "해외 여행 (방콕 4박)", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 4, "energy": 4, "mobility": 5, "note": "길거리 음식+나이트"},
    {"name": "해외 여행 (유럽 배낭 여행)", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 5, "mobility": 5, "note": "평생 기억에 남을 모험"},
    {"name": "템플스테이 1박 (부부·커플)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 2, "mobility": 4, "note": "명상+힐링 이너 피스"},
    {"name": "게스트하우스 1박 (새로운 사람 만남)", "meeting_type": "친구모임", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 4, "note": "여행자들과의 인연"},
    {"name": "한강 크루즈 야경 투어", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 2, "note": "배 위 낭만 야경"},
    {"name": "유람선 다도해 크루즈", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 5, "note": "섬 구경 힐링"},
    {"name": "캐러밴 파크 1박", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 5, "note": "캐러밴 안에서 뒹굴뒹굴"},
    {"name": "리조트 워터파크 패키지", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 5, "mobility": 5, "note": "물놀이+숙박 원스톱"},
    {"name": "독채 풀빌라 1박 (경기·강원)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 1, "energy": 2, "mobility": 5, "note": "프라이빗 풀 낭만"},
    {"name": "스카이 캐슬 펜션 1박", "meeting_type": "데이트", "awkwardness": 4, "crowd": 1, "energy": 2, "mobility": 5, "note": "뷰 맛집 숙소"},

    # ── 쇼핑 / 라이프스타일 ─────────────────────────────────────────
    {"name": "이케아 구경하며 미래 집 상상하기", "meeting_type": "데이트", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 4, "note": "미래 동거 토론 필수"},
    {"name": "빈티지 편집샵 투어 (동묘·망원)", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 2, "note": "감성 헌옷 득템"},
    {"name": "백화점 아이쇼핑 + 푸드코트", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 2, "note": "눈 쇼핑도 힐링"},
    {"name": "아울렛 쇼핑 (반값 득템)", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 3, "mobility": 4, "note": "득템 희열 공유"},
    {"name": "올리브영 신제품 사냥", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 2, "mobility": 1, "note": "뷰티 템 함께 테스트"},
    {"name": "다이소 만 원 챌린지 쇼핑", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 1, "note": "탕진잼의 정석"},
    {"name": "성수·망원 편집샵 투어", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 2, "note": "트렌디한 브랜드 탐험"},
    {"name": "문구점·팬시 전문점 탐방", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 1, "note": "예쁜 거 보면 기분 좋아짐"},
    {"name": "서로 선물 사주기 (예산 제한)", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 2, "note": "상대 취향 파악하기"},
    {"name": "벼룩시장·플리마켓 구경", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 3, "mobility": 3, "note": "숨은 보물 찾기"},
    {"name": "식물 마켓에서 식물 함께 고르기", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 3, "note": "각자 식물 키우며 성장 공유"},
    {"name": "레코드샵에서 바이닐 함께 고르기", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 2, "note": "음악 취향 나누기"},
    {"name": "공방 마켓에서 핸드메이드 소품 구매", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 3, "note": "작가 직접 만든 굿즈 득템"},
    {"name": "생활 편집샵 구경 (무신사 스토어)", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 2, "mobility": 2, "note": "옷 취향 파악 최고"},
    {"name": "서점에서 서로에게 책 골라주기", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 1, "note": "선물 교환 감성"},

    # ── 이색 체험 / 힐링 ────────────────────────────────────────────
    {"name": "찜질방·스파 함께 즐기기", "meeting_type": "공통", "awkwardness": 1, "crowd": 3, "energy": 1, "mobility": 2, "note": "식혜+계란 국룰"},
    {"name": "온천·스파 리조트 방문", "meeting_type": "데이트", "awkwardness": 4, "crowd": 2, "energy": 1, "mobility": 4, "note": "몸과 마음 힐링"},
    {"name": "아로마 마사지 커플 패키지", "meeting_type": "데이트", "awkwardness": 4, "crowd": 1, "energy": 1, "mobility": 2, "note": "피로 회복+분위기 업"},
    {"name": "요가 리트리트 1박 (힐링 여행)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 2, "energy": 2, "mobility": 5, "note": "몸과 마음 정화"},
    {"name": "동물농장 체험 (알파카·염소)", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 2, "mobility": 4, "note": "동물 힐링 = 어색함 0"},
    {"name": "반려동물 카페 방문 (고양이·강아지)", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 1, "mobility": 2, "note": "동물이 어색함 해결해 줌"},
    {"name": "타로 카드 점 보기 (같이)", "meeting_type": "공통", "awkwardness": 3, "crowd": 1, "energy": 1, "mobility": 1, "note": "서로의 미래 공유"},
    {"name": "사주·궁합 보기 (전문가)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 1, "energy": 1, "mobility": 2, "note": "진지해지는 대화 시작"},
    {"name": "퍼스널 컬러 진단 받기 (함께)", "meeting_type": "공통", "awkwardness": 3, "crowd": 1, "energy": 1, "mobility": 2, "note": "서로 어울리는 색 찾아주기"},
    {"name": "천문대 별자리 관측", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 4, "note": "별빛 아래 낭만 대화"},
    {"name": "명상·마음 챙김 클래스", "meeting_type": "데이트", "awkwardness": 4, "crowd": 2, "energy": 1, "mobility": 2, "note": "내면을 함께 들여다보기"},
    {"name": "수족관·아쿠아리움 방문", "meeting_type": "공통", "awkwardness": 3, "crowd": 4, "energy": 2, "mobility": 3, "note": "물고기 보며 힐링"},
    {"name": "동물원·사파리 나들이", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 3, "mobility": 4, "note": "동심 회복 코스"},
    {"name": "식물원 온실 투어", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 3, "note": "열대식물 속 이국 감성"},
    {"name": "방탈출+밥+카페 풀 코스 데이트", "meeting_type": "데이트", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 1, "note": "완벽한 하루 코스"},
    {"name": "한강 요트 파티 탑승", "meeting_type": "데이트", "awkwardness": 4, "crowd": 2, "energy": 2, "mobility": 2, "note": "럭셔리한 특별한 날"},
    {"name": "헬기 투어 (도심 야경)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 1, "energy": 3, "mobility": 3, "note": "일생에 한 번 레전드 데이트"},
    {"name": "미식 투어 (미슐랭 레스토랑)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 1, "energy": 1, "mobility": 2, "note": "플렉스 데이트"},
    {"name": "체험 농장 (딸기·감귤 따기)", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 3, "mobility": 5, "note": "직접 딴 과일 먹기 꿀맛"},
    {"name": "도자기 마을 투어 (이천·광주)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 5, "note": "도자기 구매+체험"},

    # ── 소개팅 / 어색한 만남 특화 ──────────────────────────────────
    {"name": "카페 → 산책 → 식사 정석 코스", "meeting_type": "데이트", "awkwardness": 5, "crowd": 3, "energy": 2, "mobility": 1, "note": "소개팅 첫 만남 교과서"},
    {"name": "소규모 방탈출 (어색함 타파용)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 1, "energy": 3, "mobility": 1, "note": "미션 수행 중 친해짐"},
    {"name": "보드게임 카페 (협력 게임 선택)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 2, "energy": 2, "mobility": 1, "note": "승패 없이 함께 클리어"},
    {"name": "원데이 클래스 (공동 제작)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 2, "energy": 2, "mobility": 2, "note": "결과물로 대화 이어짐"},
    {"name": "아쿠아리움 (나란히 걷기)", "meeting_type": "데이트", "awkwardness": 5, "crowd": 3, "energy": 2, "mobility": 3, "note": "어두운 조명 + 물고기 덕분에 편안"},
    {"name": "영화관 (IMAX 몰입 영화 선택)", "meeting_type": "데이트", "awkwardness": 5, "crowd": 4, "energy": 1, "mobility": 2, "note": "영화 중 대화 없어도 OK"},
    {"name": "전시회 + 감상 공유 카페", "meeting_type": "데이트", "awkwardness": 4, "crowd": 3, "energy": 2, "mobility": 2, "note": "전시 얘기로 자연스러운 대화"},
    {"name": "공원 산책 + 아이스크림", "meeting_type": "데이트", "awkwardness": 4, "crowd": 3, "energy": 2, "mobility": 2, "note": "걸으면 대화 더 편해짐"},
    {"name": "팝업 스토어 체험 (브랜드 공통관심)", "meeting_type": "데이트", "awkwardness": 4, "crowd": 4, "energy": 3, "mobility": 2, "note": "같은 브랜드 팬이면 즉시 친해짐"},
    {"name": "미술관 + 근처 맛집", "meeting_type": "데이트", "awkwardness": 4, "crowd": 3, "energy": 2, "mobility": 2, "note": "예술 얘기로 분위기 환기"},

    # ── 친구 모임 특화 ──────────────────────────────────────────────
    {"name": "MT (1박 2일 단체 여행)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 5, "mobility": 5, "note": "진짜 친해지는 마지막 관문"},
    {"name": "단체 요리 파티 (각자 요리 담당)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 4, "mobility": 1, "note": "요리+식사+설거지 함께"},
    {"name": "축구 직관 + 뒤풀이 치맥", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 5, "energy": 4, "mobility": 3, "note": "경기 후 뒤풀이 필수"},
    {"name": "단체 줄넘기·배구 (공원)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 2, "energy": 5, "mobility": 2, "note": "운동회 감성"},
    {"name": "팀 대항 보드게임 대회", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 2, "energy": 3, "mobility": 1, "note": "팀 나눠 진지하게"},
    {"name": "단체 사진 컨셉 촬영 (스튜디오)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 2, "energy": 3, "mobility": 2, "note": "연말 단체 사진"},
    {"name": "야간 자전거 라이딩 (한강)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 4, "mobility": 2, "note": "야경 라이딩 낭만"},
    {"name": "공유 오피스 스터디 카페 대관", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 2, "energy": 2, "mobility": 2, "note": "스터디+수다 미묘한 균형"},
    {"name": "단체 방방 트램폴린 파크", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 4, "energy": 5, "mobility": 3, "note": "어른이의 방방"},
    {"name": "단체 스크린 골프 대결", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 2, "energy": 2, "mobility": 2, "note": "홀인원 내기"},
    {"name": "단체 클라이밍 초급 코스 도전", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 5, "mobility": 2, "note": "서로 응원하며 정상 정복"},
    {"name": "단체 수영 + 사우나 코스", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 4, "mobility": 2, "note": "운동+힐링 조합"},
    {"name": "단체 페인트볼 서바이벌", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 3, "energy": 5, "mobility": 4, "note": "팀전 스릴 최고"},
    {"name": "친구들과 퀴즈쇼 (TVN 양식 공부)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 2, "energy": 2, "mobility": 1, "note": "지식 배틀"},
    {"name": "모두의 마블·부루마블 실제 투어", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 4, "energy": 4, "mobility": 3, "note": "서울 명소 실제로 가기"},

    # ── 계절 한정 이벤트 ────────────────────────────────────────────
    {"name": "벚꽃 축제 (여의도·진해)", "meeting_type": "공통", "awkwardness": 3, "crowd": 5, "energy": 3, "mobility": 3, "note": "봄 한정, 분홍빛 감성"},
    {"name": "여름 해수욕장 물놀이", "meeting_type": "공통", "awkwardness": 2, "crowd": 5, "energy": 5, "mobility": 5, "note": "여름 필수 이벤트"},
    {"name": "단풍 명산 등산 (설악산)", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 5, "mobility": 5, "note": "가을 단풍 절정 순간"},
    {"name": "크리스마스 마켓 (서울 도심)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 5, "energy": 3, "mobility": 2, "note": "겨울 핫 초콜릿+마켓"},
    {"name": "눈 오는 날 공원 눈싸움", "meeting_type": "공통", "awkwardness": 1, "crowd": 3, "energy": 5, "mobility": 2, "note": "동심 폭발 이벤트"},
    {"name": "여름 야외 음악 페스티벌", "meeting_type": "공통", "awkwardness": 2, "crowd": 5, "energy": 5, "mobility": 4, "note": "뜨거운 여름 밤의 열기"},
    {"name": "가을 국화 축제 관람", "meeting_type": "데이트", "awkwardness": 3, "crowd": 4, "energy": 2, "mobility": 3, "note": "향기로운 꽃밭 산책"},
    {"name": "겨울 빙어 낚시 체험 (인제)", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 3, "energy": 3, "mobility": 5, "note": "낚시+즉석 구이"},
    {"name": "여름 옥수수·수박 농장 체험", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 3, "mobility": 5, "note": "밭에서 직접 따 먹기"},
    {"name": "봄 딸기 농장 체험", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 3, "mobility": 5, "note": "딸기 실컷 먹는 꿈의 시간"},
    {"name": "가을 고구마·감자 캐기 체험", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 4, "mobility": 5, "note": "자연 속 농부 체험"},
    {"name": "겨울 스키 야간 리프트 탑승", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 5, "note": "야간 설경 낭만 최고"},
    {"name": "가을 억새밭 드라이브 (민둥산)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 5, "note": "황금빛 억새 물결"},
    {"name": "봄 유채꽃밭 나들이 (제주·태안)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 4, "energy": 2, "mobility": 5, "note": "노란 꽃밭 인생샷"},
    {"name": "크리스마스 이브 야경 드라이브", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 2, "mobility": 5, "note": "연말 최고 감성 코스"},

    # ── 취미 공유 ────────────────────────────────────────────────────
    {"name": "같이 그림 그리기 (아이패드)", "meeting_type": "공통", "awkwardness": 2, "crowd": 1, "energy": 1, "mobility": 1, "note": "서로 초상화 그려주기"},
    {"name": "같이 뜨개질 (초급 강습)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 1, "mobility": 2, "note": "완성품 선물하기"},
    {"name": "함께 독서 (북클럽 형성)", "meeting_type": "공통", "awkwardness": 3, "crowd": 2, "energy": 1, "mobility": 1, "note": "책 이야기로 깊어지는 대화"},
    {"name": "함께 영화 리뷰 영상 찍기", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 1, "energy": 3, "mobility": 1, "note": "유튜버 체험"},
    {"name": "음악 함께 듣기 (플리 공유)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 1, "mobility": 1, "note": "취향 공유 = 빠른 친해짐"},
    {"name": "함께 요리 해먹기 (집밥)", "meeting_type": "공통", "awkwardness": 2, "crowd": 1, "energy": 3, "mobility": 1, "note": "역할 나누면 자연스러워짐"},
    {"name": "함께 K-POP 안무 배우기 (유튜브)", "meeting_type": "공통", "awkwardness": 1, "crowd": 1, "energy": 4, "mobility": 1, "note": "같이 망가지면 친해짐"},
    {"name": "함께 악기 배우기 (우쿨렐레)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 2, "mobility": 1, "note": "함께 한 곡 완성하기"},
    {"name": "함께 러닝 + 커피 마시기", "meeting_type": "공통", "awkwardness": 2, "crowd": 3, "energy": 4, "mobility": 2, "note": "운동 후 대화 더 잘됨"},
    {"name": "한강에서 치킨+맥주 피크닉", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 2, "mobility": 1, "note": "여름 한강 국룰"},
    {"name": "함께 MBTI 딥 다이브 토크", "meeting_type": "공통", "awkwardness": 4, "crowd": 1, "energy": 1, "mobility": 1, "note": "16가지 유형 분석 수다"},
    {"name": "같이 미니멀 살림 정리하기", "meeting_type": "데이트", "awkwardness": 2, "crowd": 1, "energy": 3, "mobility": 1, "note": "서로의 공간 탐방"},
    {"name": "함께 유튜브 본방 사수", "meeting_type": "공통", "awkwardness": 2, "crowd": 1, "energy": 1, "mobility": 1, "note": "관심 채널 추천 교환"},
    {"name": "함께 포토부스 콘셉트 사진 찍기", "meeting_type": "공통", "awkwardness": 2, "crowd": 2, "energy": 2, "mobility": 1, "note": "컨셉 정하는 것도 재미"},
    {"name": "수제 버거 만들기 파티", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 2, "energy": 3, "mobility": 1, "note": "각자 재료 갖고 와서 조합"},
    {"name": "함께 웹툰·웹소설 추천 교환", "meeting_type": "공통", "awkwardness": 3, "crowd": 1, "energy": 1, "mobility": 1, "note": "각자 최애 공유"},
    {"name": "함께 플레이리스트 공유 카페", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 1, "mobility": 1, "note": "서로의 음악 취향 탐험"},
    {"name": "함께 과거 앨범 보며 추억 여행", "meeting_type": "공통", "awkwardness": 1, "crowd": 1, "energy": 1, "mobility": 1, "note": "시간여행 수다 보장"},
    {"name": "야외 스케치 (공원·골목)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 2, "mobility": 2, "note": "그림 실력 무관, 과정이 중요"},
    {"name": "함께 맥주 홈브루잉 도전", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 1, "energy": 3, "mobility": 1, "note": "2주 후 함께 마시기"},

    # ── 이색·특별 경험 ───────────────────────────────────────────────
    {"name": "핸드폰 없이 하루 오프라인 데이트", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 3, "mobility": 2, "note": "디지털 디톡스+진짜 대화"},
    {"name": "버스킹 공연 직접 참여 (오픈 마이크)", "meeting_type": "공통", "awkwardness": 2, "crowd": 4, "energy": 4, "mobility": 1, "note": "용기 있는 자만이 참가"},
    {"name": "사진 공모전 함께 참가 (테마 사진전)", "meeting_type": "공통", "awkwardness": 3, "crowd": 2, "energy": 3, "mobility": 3, "note": "공동 목표로 친해짐"},
    {"name": "음식 만들기 대결 (심사위원 초대)", "meeting_type": "공통", "awkwardness": 1, "crowd": 2, "energy": 4, "mobility": 1, "note": "MasterChef 빙의"},
    {"name": "인생 투어 (각자의 추억 장소 방문)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 3, "mobility": 3, "note": "서로의 과거 탐방"},
    {"name": "운세 카페·사주 카페 방문", "meeting_type": "공통", "awkwardness": 4, "crowd": 2, "energy": 1, "mobility": 1, "note": "미래 얘기로 대화 풍성"},
    {"name": "셀프 영화 촬영 (단편 영화)", "meeting_type": "공통", "awkwardness": 2, "crowd": 1, "energy": 4, "mobility": 2, "note": "감독+배우 동시에"},
    {"name": "함께 등대 보러 가기 (밤)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 2, "mobility": 5, "note": "빛나는 등대 + 낭만"},
    {"name": "우편 교환 프로젝트 (손편지 쓰기)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 1, "mobility": 1, "note": "아날로그 감성 소통"},
    {"name": "새벽 시장 탐방 (가락시장)", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 4, "energy": 3, "mobility": 3, "note": "새벽 4시 활기찬 시장"},
    {"name": "지역 축제 탐방 (지역 특색 축제)", "meeting_type": "공통", "awkwardness": 3, "crowd": 5, "energy": 3, "mobility": 4, "note": "지역 음식+공연 체험"},
    {"name": "함께 자원봉사 활동 (급식소 등)", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 3, "note": "뿌듯함 공유 = 유대감"},
    {"name": "해돋이 명소 드라이브 (새해 한정)", "meeting_type": "데이트", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 5, "note": "새해 첫날 특별한 기억"},
    {"name": "코스튬 파티 (할로윈·컨셉 파티)", "meeting_type": "친구모임", "awkwardness": 1, "crowd": 5, "energy": 5, "mobility": 2, "note": "변장하면 어색함 사라짐"},
    {"name": "함께 새 취미 도전 (처음 해보는 것)", "meeting_type": "공통", "awkwardness": 3, "crowd": 2, "energy": 3, "mobility": 2, "note": "초보 실력 공유 = 친해짐"},
    {"name": "시민 마라톤 완주 후 뒤풀이", "meeting_type": "공통", "awkwardness": 2, "crowd": 5, "energy": 5, "mobility": 3, "note": "완주 메달+삼겹살"},
    {"name": "감성 필름 카메라 투어", "meeting_type": "데이트", "awkwardness": 3, "crowd": 2, "energy": 3, "mobility": 2, "note": "현상 후 함께 보는 기쁨"},
    {"name": "새로운 동네 탐방 (처음 가는 구)", "meeting_type": "공통", "awkwardness": 3, "crowd": 3, "energy": 3, "mobility": 2, "note": "미지의 동네 탐험가"},
    {"name": "함께 독학 챌린지 (외국어·코딩)", "meeting_type": "친구모임", "awkwardness": 2, "crowd": 1, "energy": 2, "mobility": 1, "note": "스터디 파트너"},
    {"name": "함께 버킷리스트 작성+실행 계획", "meeting_type": "데이트", "awkwardness": 3, "crowd": 1, "energy": 1, "mobility": 1, "note": "서로의 꿈 공유"},
]

philosophical_fortunes = [# [자아와 성찰]
    "가장 밝은 빛은 가장 깊은 어둠 속에서 태어납니다.",
    "거울 속의 당신은 당신이 아는 것보다 더 강한 힘을 숨기고 있습니다.",
    "당신이라는 책의 다음 장은 아직 백지입니다. 어떤 문장으로 채우고 싶나요?",
    "결과보다 과정 속에서 발견하는 당신의 표정에 주목하세요.",
    "오늘은 스스로를 평가하기보다, 그저 다독여주어야 하는 날입니다.",
    "내면의 소음이 커질 때, 가장 지혜로운 대답은 침묵 속에 있습니다.",
    "당신은 누군가의 배경이 아니라, 당신 인생의 유일한 주인공입니다.",
    "남들의 속도에 맞추느라 당신만의 박자를 잃어버리지 마세요.",
    "자신을 용서하는 일이야말로 오늘 당신이 해야 할 가장 큰 성취입니다.",
    "작은 균열 사이로 새로운 빛이 들어오기 시작할 것입니다.",
    "당신이 가진 상처는 당신이 살아남았다는 가장 영광스러운 증거입니다.",
    "생각의 꼬리를 자르고, 지금 이 순간의 감각에만 집중해 보세요.",
    "완벽함이라는 환상에서 벗어날 때, 진정한 자유가 찾아옵니다.",
    "당신은 존재만으로도 충분히 가치 있는 사람이라는 사실을 잊지 마세요.",
    "가장 나다운 모습일 때, 당신은 가장 아름답게 빛납니다.",
    "마음의 환기가 필요합니다. 고여 있는 생각들을 밖으로 흘려보내세요.",
    "오늘의 당신은 어제의 당신이 꿈꾸던 미래입니다.",
    "자신에게 너무 엄격한 잣대를 들이대고 있지는 않나요?",
    "꿈은 이루어지는 것이 아니라, 매일 조금씩 만들어가는 것입니다.",
    "가장 소중한 답은 이미 당신의 마음 깊은 곳에 자리 잡고 있습니다.",

    # [변화와 도전]
    "익숙한 길에서 벗어나는 순간, 보이지 않던 풍경이 나타납니다.",
    "바람이 불지 않을 때 바람개비를 돌리는 방법은, 당신이 앞으로 달려가는 것입니다.",
    "두려움은 당신을 막아서는 벽이 아니라, 넘어서야 할 문턱일 뿐입니다.",
    "멈춰 서 있는 배는 결코 새로운 대륙을 발견할 수 없습니다.",
    "실패는 넘어지는 것이 아니라, 넘어진 자리에 계속 머무는 것입니다.",
    "변화는 고통스럽지만, 정체는 서서히 영혼을 갉아먹습니다.",
    "오늘 당신이 내딛는 작은 한 걸음이 거대한 기적의 시작이 될 것입니다.",
    "한 번도 가보지 않은 길 위에 진정한 성장이 기다리고 있습니다.",
    "포기하고 싶은 그 순간이, 바로 문이 열리기 직전의 찰나입니다.",
    "불가능해 보이는 일도 '아직' 방법을 찾지 못한 것일 뿐입니다.",
    "당신의 한계는 당신이 직접 그어놓은 선에 불과합니다.",
    "용기란 두려움이 없는 것이 아니라, 두려워도 한 발자국 나아가는 것입니다.",
    "씨앗이 땅을 뚫고 나오듯, 당신의 노력이 결실을 맺으려 합니다.",
    "기회는 노크하지 않습니다. 당신이 직접 문을 열고 나가야 합니다.",
    "과거의 실수를 교훈 삼아, 오늘이라는 무대에서 더 멋지게 연기하세요.",
    "상황을 바꿀 수 없다면, 상황을 바라보는 당신의 시선을 바꾸어 보세요.",
    "어려운 선택일수록 당신을 더 크게 성장시켜 줄 것입니다.",
    "시작하기에 가장 좋은 때는 바로 '지금'입니다.",
    "당신만의 속도로 걸으세요. 결국 도착지는 같습니다.",
    "어제의 후회에 발목 잡히기엔 오늘의 햇살이 너무 아깝습니다.",

    # [관계와 연결]
    "진심은 화려한 말보다 따뜻한 눈빛 속에 깃들어 있습니다.",
    "타인의 시선이라는 감옥에서 스스로를 석방해 주어야 할 때입니다.",
    "가까운 사람일수록 더 예의 바르게 대해야 함을 기억하세요.",
    "모두에게 좋은 사람이 되려다 정작 자신을 잃어버리고 있지는 않나요?",
    "말 한마디가 누군가에게는 평생 잊지 못할 흉터가 될 수도 있습니다.",
    "타인을 이해하려는 노력은 결국 나를 이해하는 과정과 같습니다.",
    "진정한 우정은 침묵 속에서도 어색하지 않은 사이입니다.",
    "사랑은 받는 것이 아니라, 기꺼이 내어주는 마음에서 시작됩니다.",
    "혼자라는 외로움보다 나쁜 것은 맞지 않는 옷을 입은 듯한 만남입니다.",
    "사람과 사람 사이에도 적당한 거리가 필요합니다. 그래야 서로가 보입니다.",
    "당신을 아프게 하는 관계라면 잠시 거리를 두어도 괜찮습니다.",
    "상대방의 약점을 안아줄 때, 관계는 비로소 깊어집니다.",
    "진정한 대화는 입이 아니라 귀에서 시작됨을 잊지 마세요.",
    "누군가의 기대를 충족시키기 위해 당신의 영혼을 팔지 마세요.",
    "친절은 결코 낭비되는 법이 없습니다. 언젠가 당신에게 돌아옵니다.",
    "사소한 배려가 얼어붙은 마음을 녹이는 열쇠가 됩니다.",
    "타인의 비난에 흔들리지 마세요. 그건 그들의 문제일 뿐입니다.",
    "좋은 인연은 억지로 맺으려 하지 않아도 자연스레 찾아옵니다.",
    "말하지 않아도 전해지는 마음이 가장 순수한 법입니다.",
    "곁에 있는 소중한 사람에게 오늘 '고맙다'는 말을 전해 보세요.",

    # [시간과 타이밍]
    "모든 꽃이 봄에 피지는 않습니다. 당신의 계절은 곧 올 것입니다.",
    "조급함은 서두르게 만들고, 서두름은 소중한 것을 놓치게 합니다.",
    "시간은 누구에게나 공평하지만, 그 가치를 결정하는 건 당신입니다.",
    "기다림 또한 행동의 한 형태임을 깨닫는 하루가 되길 바랍니다.",
    "과거는 기억 속에 있고 미래는 상상 속에 있지만, 삶은 지금 여기에 있습니다.",
    "인생은 타이밍이 아니라, 당신이 준비되었는가의 문제입니다.",
    "너무 늦은 때란 없습니다. 단지 시작하지 않은 순간이 있을 뿐입니다.",
    "찰나의 순간들이 모여 당신의 영원을 구성합니다.",
    "오늘의 고생은 내일의 웃음을 위한 밑거름이 될 것입니다.",
    "휴식은 멈춤이 아니라, 더 멀리 나아가기 위한 충전의 시간입니다.",
    "시간의 흐름에 몸을 맡기되, 방향만은 잃지 마세요.",
    "어둠이 깊을수록 새벽이 가까워졌음을 믿으세요.",
    "지금 겪는 진통은 새로운 생명이 태어나기 위한 과정입니다.",
    "세상은 서두르는 자보다 끈기 있게 기다리는 자에게 문을 열어줍니다.",
    "오늘 하루를 인생의 마지막 날인 것처럼 치열하고 아름답게 살아보세요.",
    "천천히 가도 괜찮습니다. 중요한 건 멈추지 않는 것입니다.",
    "우연처럼 보이는 필연들이 당신의 길을 안내하고 있습니다.",
    "지나간 일은 흘러가게 두세요. 새로운 물결이 들어오도록.",
    "계획대로 되지 않는 것도 인생의 묘미입니다. 의외성을 즐기세요.",
    "지금 이 순간이 당신 인생의 가장 화양연화(花樣年華)일 수 있습니다.",

    # [성취와 목표]
    "성공의 높이보다 당신이 견뎌온 깊이가 더 중요합니다.",
    "위대한 일은 단번에 이루어지지 않습니다. 작은 조각들이 모여 완성됩니다.",
    "남과 비교하지 마세요. 어제의 당신보다 오늘 한 걸음 나아갔다면 충분합니다.",
    "진정한 성취는 결과가 아니라 그 과정에서 얻은 지혜에 있습니다.",
    "포기하고 싶을 때 왜 시작했는지를 다시 한번 떠올려 보세요.",
    "목표에만 매몰되어 주변의 아름다운 풍경을 놓치고 있지는 않나요?",
    "노력은 배신하지 않습니다. 다만 시간이 조금 더 걸릴 뿐입니다.",
    "실패했다는 건, 당신이 무언가에 도전했다는 멋진 증거입니다.",
    "정상에 오르는 법은 단순합니다. 한 발자국씩 계속 걷는 것입니다.",
    "자신을 믿으세요. 당신은 당신이 생각하는 것보다 훨씬 유능합니다.",
    "최선을 다했다면 결과에 연연하지 마세요. 하늘의 뜻에 맡기세요.",
    "어려운 과제가 주어졌다는 건 당신이 그만큼 신뢰받고 있다는 뜻입니다.",
    "기초를 튼튼히 다지는 데 시간을 아끼지 마세요.",
    "창의성은 지식보다 상상력과 용기에서 나옵니다.",
    "오늘의 작은 성공이 내일의 거대한 승리로 이어질 것입니다.",
    "한 분야의 대가는 수만 번의 실패를 경험한 사람입니다.",
    "당신의 열정에 다시 한번 불을 지펴보세요. 아직 늦지 않았습니다.",
    "문제의 답은 문제 속에 있습니다. 다시 한번 찬찬히 들여다보세요.",
    "주변의 도움을 받는 것을 부끄러워하지 마세요. 그것도 능력입니다.",
    "자신만의 철학을 가지세요. 그것이 당신을 지켜주는 방패가 됩니다.",

    # [감성과 위로]
    "비가 온 뒤에 땅이 굳어지듯, 아픔 뒤엔 더 단단한 당신이 있습니다.",
    "따뜻한 차 한 잔의 여유가 수천 마디의 조언보다 나을 때가 있습니다.",
    "오늘 밤엔 아무 생각 없이 깊은 잠에 빠져보세요. 내일은 내일의 태양이 뜹니다.",
    "당신의 마음을 괴롭히는 것들을 종이에 적어 불태워버리세요.",
    "작은 것에 감사할 때, 행복은 당신의 문턱을 넘습니다.",
    "눈물을 흘리는 것은 나약함이 아니라, 마음을 정화하는 과정입니다.",
    "창밖의 풍경을 가만히 바라보는 것만으로도 위로가 되는 하루입니다.",
    "당신은 충분히 잘해왔고, 지금도 잘하고 있습니다.",
    "가끔은 길을 잃어도 괜찮습니다. 예상치 못한 보물을 발견할지도 모르니까요.",
    "당신의 진심을 알아주는 단 한 사람만 있어도 세상은 살 만합니다.",
    "마음의 짐을 잠시 내려놓으세요. 당신의 어깨가 너무 무거워 보입니다.",
    "소박한 일상이 주는 행복을 온전히 누리는 하루가 되길.",
    "어제의 슬픔이 오늘의 당신을 무너뜨리게 두지 마세요.",
    "당신이라는 존재는 그 자체로 하나의 우주이자 신비입니다.",
    "구름 뒤의 태양은 언제나 그 자리에 있음을 잊지 마세요.",
    "힘들 땐 쉬어 가세요. 나무도 겨울엔 성장을 멈추고 봄을 준비합니다.",
    "누군가에게 당신은 세상에서 가장 소중한 사람입니다.",
    "마음속의 미움은 상대가 아니라 나를 아프게 할 뿐입니다.",
    "부드러움이 강함을 이긴다는 사실을 기억하는 하루가 되길.",
    "오늘 하루, 수고한 당신에게 스스로 작은 선물을 건네보세요.",

    # [인생의 지혜]
    "빈 수레가 요란한 법입니다. 내실을 다지는 데 집중하세요.",
    "과한 욕심은 눈을 가리고 이성을 마비시킵니다.",
    "삶은 정답을 찾는 과정이 아니라, 나만의 해답을 써 내려가는 과정입니다.",
    "흐르는 강물에 손을 씻듯, 미련을 버리고 현재를 사세요.",
    "지혜로운 사람은 자신의 부족함을 인정하는 데서 시작합니다.",
    "당신이 가진 것에 만족할 때, 당신은 세상에서 가장 부유한 사람입니다.",
    "말을 아끼세요. 침묵은 때로 가장 강력한 웅변이 됩니다.",
    "모든 일에는 원인과 결과가 있습니다. 오늘 당신이 심은 씨앗을 보세요.",
    "행복은 멀리 있지 않습니다. 당신의 발밑에 피어 있는 작은 꽃과 같습니다.",
    "인생은 속도가 아니라 방향입니다. 올바른 곳을 향하고 있나요?",
    "배움에는 끝이 없습니다. 세상 모든 것에서 스승을 찾으세요.",
    "겸손은 비굴함이 아니라 자신감에서 나오는 여유입니다.",
    "진정한 자유는 내 마음을 내가 다스릴 수 있을 때 찾아옵니다.",
    "세상을 바꾸려 하지 말고, 당신 자신을 먼저 바꾸어 보세요.",
    "인생의 소중한 것들은 대개 눈에 보이지 않습니다.",
    "어려운 시기는 당신을 강하게 만들기 위한 훈련 과정입니다.",
    "뿌리 깊은 나무는 바람에 흔들리지 않습니다. 당신의 신념을 굳건히 하세요.",
    "지나친 걱정은 일어나지도 않은 불행을 앞당겨 사는 것과 같습니다.",
    "매 순간이 기회입니다. 당신이 알아차리기만 한다면.",
    "오늘의 선택이 당신의 내일을 결정합니다. 신중하되 단호하세요.",
    "당신의 영혼이 하는 말에 귀를 기울이세요. 그게 진짜 당신입니다.",
    "세상은 당신이 보는 대로 존재합니다. 긍정의 렌즈를 끼워보세요.",
    "삶의 무게가 느껴진다면, 당신이 그만큼 책임감 있게 살고 있다는 뜻입니다.",
    "가장 위대한 승리는 자신을 이기는 승리입니다.",
    "오늘이라는 선물(Present)을 기쁘게 받아들이세요."]

cafe_list = [{"name": "아이스 아메리카노", "caffeine": 4, "sweetness": 1, "note": "국룰, 식후 필수"}, {"name": "따뜻한 아메리카노", "caffeine": 4, "sweetness": 1, "note": "비오는 날, 아침"}, {"name": "카페라떼", "caffeine": 4, "sweetness": 2, "note": "부드러움, 고소함"}, {"name": "바닐라 라떼", "caffeine": 4, "sweetness": 4, "note": "당 충전, 달달함"}, {"name": "콜드브루", "caffeine": 5, "sweetness": 1, "note": "깔끔함, 카페인 폭발"}, {"name": "에스프레소", "caffeine": 5, "sweetness": 1, "note": "강렬함, 잠 깨기"}, {"name": "카라멜 마끼아또", "caffeine": 4, "sweetness": 5, "note": "극강의 단맛, 피곤할 때"}, {"name": "헤이즐넛 라떼", "caffeine": 4, "sweetness": 4, "note": "향긋함, 달콤함"}, {"name": "아인슈페너", "caffeine": 4, "sweetness": 4, "note": "크림의 부드러움, 씁쓸함"}, {"name": "돌체 라떼 (연유 라떼)", "caffeine": 4, "sweetness": 5, "note": "달달함, 화장실 직행"}, {"name": "디카페인 아메리카노", "caffeine": 1, "sweetness": 1, "note": "밤 늦게, 카페인 부담될 때"}, {"name": "딸기 라떼", "caffeine": 1, "sweetness": 4, "note": "상큼달콤, 논커피"}, {"name": "초코 라떼", "caffeine": 2, "sweetness": 5, "note": "당 충전 100%, 우울할 때"}, {"name": "녹차 라떼", "caffeine": 3, "sweetness": 3, "note": "쌉싸름함, 부드러움"}, {"name": "민트초코 라떼", "caffeine": 2, "sweetness": 4, "note": "호불호, 시원달달"}, {"name": "고구마 라떼", "caffeine": 1, "sweetness": 3, "note": "포만감, 따뜻함"}, {"name": "미숫가루 (곡물 라떼)", "caffeine": 1, "sweetness": 3, "note": "든든함, 할매니얼"}, {"name": "자몽 에이드", "caffeine": 1, "sweetness": 4, "note": "상큼함, 톡쏘는 맛"}, {"name": "레몬 에이드", "caffeine": 1, "sweetness": 4, "note": "비타민 충전, 새콤함"}, {"name": "청포도 에이드", "caffeine": 1, "sweetness": 4, "note": "달달상큼, 여름 추천"}, {"name": "망고 스무디", "caffeine": 1, "sweetness": 4, "note": "열대과일, 시원함"}, {"name": "딸기 요거트 스무디", "caffeine": 1, "sweetness": 4, "note": "새콤달콤, 든든함"}, {"name": "플레인 요거트 스무디", "caffeine": 1, "sweetness": 3, "note": "깔끔한 새콤함"}, {"name": "밀크티", "caffeine": 3, "sweetness": 4, "note": "향긋함, 오후의 여유"}, {"name": "흑당 버블티", "caffeine": 3, "sweetness": 5, "note": "쫀득함, 극강의 단맛"}, {"name": "얼그레이 티", "caffeine": 3, "sweetness": 1, "note": "향긋함, 깔끔함"}, {"name": "캐모마일 티", "caffeine": 1, "sweetness": 1, "note": "심신 안정, 수면 전"}, {"name": "페퍼민트 티", "caffeine": 1, "sweetness": 1, "note": "상쾌함, 식후 양치 느낌"}, {"name": "유자차", "caffeine": 1, "sweetness": 4, "note": "감기 기운 있을 때, 겨울"}, {"name": "복숭아 아이스티", "caffeine": 2, "sweetness": 5, "note": "국민 음료, 달달시원"}]
youtube_list = [{"name": "침착맨 삼국지 풀영상", "duration": 5, "immersion": 1, "note": "백색소음"}, {"name": "무한도전 레전드 클립", "duration": 2, "immersion": 3, "note": "웃음 보장"}, {"name": "에센셜 플레이리스트", "duration": 5, "immersion": 1, "note": "감성 배경음악"}, {"name": "먹방 크리에이터 영상", "duration": 3, "immersion": 4, "note": "식욕 폭발"}, {"name": "슈카월드 경제 교양", "duration": 4, "immersion": 3, "note": "지식 충전"}, {"name": "궤도 과학 다큐", "duration": 4, "immersion": 4, "note": "지적 유희"}, {"name": "결말포함 영화 리뷰", "duration": 3, "immersion": 5, "note": "시간 순삭"}, {"name": "빠니보틀 세계여행", "duration": 4, "immersion": 4, "note": "대리 여행"}, {"name": "요리/베이킹 브이로그", "duration": 2, "immersion": 3, "note": "눈이 즐거움"}, {"name": "숲속 캠핑 ASMR", "duration": 5, "immersion": 1, "note": "차분함"}, {"name": "동물농장 힐링 영상", "duration": 2, "immersion": 4, "note": "귀여움 한도초과"}, {"name": "웃긴 릴스 모음", "duration": 1, "immersion": 4, "note": "도파민 뿜뿜"}, {"name": "게임 스트리밍 하이라이트", "duration": 3, "immersion": 4, "note": "긴장감"}, {"name": "꼬꼬무 사건 요약", "duration": 4, "immersion": 5, "note": "소름 과몰입"}, {"name": "IT/전자기기 리뷰", "duration": 2, "immersion": 4, "note": "뽐뿌 옴"}, {"name": "룸투어 인테리어 영상", "duration": 2, "immersion": 3, "note": "인테리어 영감"}, {"name": "공포 괴담썰", "duration": 3, "immersion": 2, "note": "오싹함"}, {"name": "한문철 TV 레전드", "duration": 2, "immersion": 4, "note": "도파민 경각심"}, {"name": "아이돌 직캠 교차편집", "duration": 2, "immersion": 4, "note": "눈호강"}, {"name": "스탠드업 코미디", "duration": 3, "immersion": 3, "note": "어른의 유머"}, {"name": "고퀄리티 다큐", "duration": 4, "immersion": 3, "note": "마음이 편안"}, {"name": "스포츠 하이라이트", "duration": 2, "immersion": 4, "note": "명장면 짜릿함"}, {"name": "알콩달콩 커플 브이로그", "duration": 3, "immersion": 3, "note": "몽글몽글"}, {"name": "해외 스트리트 푸드", "duration": 3, "immersion": 3, "note": "여행 뽐뿌"}, {"name": "뷰티 겟레디윗미", "duration": 3, "immersion": 3, "note": "화장할 때"}, {"name": "홈트레이닝 따라하기", "duration": 3, "immersion": 4, "note": "다이어트 자극"}, {"name": "다이어트 식단 브이로그", "duration": 2, "immersion": 3, "note": "건강 자극"}, {"name": "스트리트 룩북", "duration": 2, "immersion": 4, "note": "옷차림 참고"}, {"name": "ASMR 먹방", "duration": 3, "immersion": 2, "note": "소리 힐링"}, {"name": "역사 썰 풀기", "duration": 4, "immersion": 3, "note": "흥미진진 교양"}]
drama_list = [{"name": "나의 아저씨", "duration": 5, "immersion": 5, "note": "인생 드라마"}, {"name": "도깨비", "duration": 5, "immersion": 4, "note": "판타지 로맨스"}, {"name": "비밀의 숲", "duration": 5, "immersion": 5, "note": "스릴러 명작"}, {"name": "미생", "duration": 5, "immersion": 5, "note": "직장인 애환"}, {"name": "응답하라 1988", "duration": 5, "immersion": 4, "note": "가족애"}, {"name": "슬기로운 의사생활", "duration": 5, "immersion": 4, "note": "힐링 메디컬"}, {"name": "시그널", "duration": 5, "immersion": 5, "note": "타임워프 수사극"}, {"name": "오징어 게임", "duration": 5, "immersion": 5, "note": "글로벌 히트작"}, {"name": "더 글로리", "duration": 5, "immersion": 5, "note": "통쾌한 복수극"}, {"name": "킹덤", "duration": 5, "immersion": 5, "note": "조선 좀비"}, {"name": "무빙", "duration": 5, "immersion": 5, "note": "한국형 히어로"}, {"name": "스카이 캐슬", "duration": 5, "immersion": 5, "note": "입시 스릴러"}, {"name": "사랑의 불시착", "duration": 5, "immersion": 4, "note": "설레는 로코"}, {"name": "별에서 온 그대", "duration": 5, "immersion": 4, "note": "외계인 로맨스"}, {"name": "이태원 클라쓰", "duration": 5, "immersion": 5, "note": "청춘 복수극"}, {"name": "눈이 부시게", "duration": 5, "immersion": 5, "note": "반전 감동"}, {"name": "동백꽃 필 무렵", "duration": 5, "immersion": 4, "note": "스릴러 한 스푼"}, {"name": "멜로가 체질", "duration": 5, "immersion": 4, "note": "현실 공감"}, {"name": "스토브리그", "duration": 5, "immersion": 5, "note": "스포츠 오피스"}, {"name": "소년심판", "duration": 5, "immersion": 5, "note": "묵직한 메시지"}, {"name": "D.P.", "duration": 5, "immersion": 5, "note": "현실 고발"}, {"name": "지옥", "duration": 5, "immersion": 5, "note": "디스토피아"}, {"name": "나의 해방일지", "duration": 5, "immersion": 5, "note": "깊은 여운"}, {"name": "이상한 변호사 우영우", "duration": 5, "immersion": 4, "note": "무해한 힐링"}, {"name": "재벌집 막내아들", "duration": 5, "immersion": 5, "note": "인생 2회차"}, {"name": "눈물의 여왕", "duration": 5, "immersion": 4, "note": "로맨틱 코미디"}, {"name": "선재 업고 튀어", "duration": 5, "immersion": 4, "note": "타임슬립 청춘"}, {"name": "환혼", "duration": 5, "immersion": 4, "note": "판타지 무협"}, {"name": "괴물", "duration": 5, "immersion": 5, "note": "심리 스릴러"}, {"name": "호텔 델루나", "duration": 5, "immersion": 4, "note": "판타지 로코"}]
variety_list = [{"name": "신서유기", "duration": 4, "immersion": 4, "note": "웃음 보장"}, {"name": "런닝맨", "duration": 4, "immersion": 3, "note": "주말 근본"}, {"name": "지구오락실", "duration": 4, "immersion": 4, "note": "MZ 텐션"}, {"name": "나 혼자 산다", "duration": 4, "immersion": 3, "note": "스타 일상"}, {"name": "유 퀴즈 온 더 블럭", "duration": 4, "immersion": 4, "note": "따뜻한 토크"}, {"name": "아는 형님", "duration": 4, "immersion": 3, "note": "학교 컨셉"}, {"name": "놀면 뭐하니?", "duration": 4, "immersion": 3, "note": "부캐 세계관"}, {"name": "환승연애", "duration": 4, "immersion": 5, "note": "과몰입 100%"}, {"name": "나는 SOLO", "duration": 4, "immersion": 5, "note": "도파민 리얼리티"}, {"name": "최강야구", "duration": 4, "immersion": 5, "note": "스포츠 예능"}, {"name": "대탈출", "duration": 4, "immersion": 5, "note": "추리 방탈출"}, {"name": "여고추리반", "duration": 4, "immersion": 5, "note": "여고 괴담"}, {"name": "피지컬: 100", "duration": 4, "immersion": 5, "note": "원초적 아드레날린"}, {"name": "솔로지옥", "duration": 4, "immersion": 4, "note": "핫한 남녀"}, {"name": "크라임씬", "duration": 4, "immersion": 5, "note": "뇌섹 예능"}, {"name": "태어난 김에 세계일주", "duration": 4, "immersion": 4, "note": "날것 여행"}, {"name": "삼시세끼", "duration": 4, "immersion": 2, "note": "농촌 힐링"}, {"name": "서진이네", "duration": 4, "immersion": 3, "note": "식당 운영기"}, {"name": "강철부대", "duration": 4, "immersion": 5, "note": "밀리터리 서바이벌"}, {"name": "스트릿 우먼 파이터", "duration": 4, "immersion": 5, "note": "댄스 배틀"}, {"name": "흑백요리사", "duration": 4, "immersion": 5, "note": "계급 전쟁"}, {"name": "텐트 밖은 유럽", "duration": 4, "immersion": 3, "note": "캠핑기"}, {"name": "SNL 코리아", "duration": 4, "immersion": 4, "note": "선 넘는 콩트"}, {"name": "전지적 참견 시점", "duration": 4, "immersion": 3, "note": "매니저와 일상"}, {"name": "미운 우리 새끼", "duration": 4, "immersion": 3, "note": "소소한 웃음"}, {"name": "골 때리는 그녀들", "duration": 4, "immersion": 5, "note": "여자 축구"}, {"name": "놀라운 토요일", "duration": 4, "immersion": 4, "note": "가사 맞추기"}, {"name": "백종원의 골목식당", "duration": 4, "immersion": 4, "note": "솔루션 사이다"}, {"name": "하트시그널", "duration": 4, "immersion": 4, "note": "원조 연애 예능"}, {"name": "마이 리틀 텔레비전", "duration": 4, "immersion": 4, "note": "인터넷 방송 감성"}]
ani_list = [{"name": "귀멸의 칼날", "duration": 3, "immersion": 5, "note": "작화 폭발"}, {"name": "스즈메의 문단속", "duration": 5, "immersion": 4, "note": "신카이 마코토 감성"}]
movie_list = [{"name": "인터스텔라", "duration": 5, "immersion": 5, "note": "우주 SF"}, {"name": "어벤져스", "duration": 5, "immersion": 5, "note": "마블 히어로"}, {"name": "기생충", "duration": 5, "immersion": 5, "note": "블랙 코미디"}, {"name": "범죄도시", "duration": 5, "immersion": 4, "note": "사이다 액션"}, {"name": "어바웃 타임", "duration": 5, "immersion": 4, "note": "시간 여행"}, {"name": "라라랜드", "duration": 5, "immersion": 4, "note": "뮤지컬 명작"}, {"name": "해리 포터", "duration": 5, "immersion": 5, "note": "마법 세계"}, {"name": "매트릭스", "duration": 5, "immersion": 5, "note": "SF 액션"}, {"name": "타이타닉", "duration": 5, "immersion": 5, "note": "세기의 로맨스"}, {"name": "신과함께", "duration": 5, "immersion": 4, "note": "가족애 눈물"}, {"name": "다크 나이트", "duration": 5, "immersion": 5, "note": "최고의 조커"}, {"name": "인셉션", "duration": 5, "immersion": 5, "note": "꿈 속의 꿈"}, {"name": "너의 이름은.", "duration": 5, "immersion": 4, "note": "명작 애니"}, {"name": "센과 치히로의 행방불명", "duration": 5, "immersion": 4, "note": "지브리 마스터피스"}, {"name": "엘리멘탈", "duration": 5, "immersion": 4, "note": "픽사 감동"}, {"name": "아바타", "duration": 5, "immersion": 5, "note": "3D 시각 혁명"}, {"name": "탑건: 매버릭", "duration": 5, "immersion": 5, "note": "항공 액션"}, {"name": "건축학개론", "duration": 5, "immersion": 4, "note": "첫사랑 추억"}, {"name": "아저씨", "duration": 5, "immersion": 4, "note": "감성 액션"}, {"name": "베테랑", "duration": 5, "immersion": 4, "note": "유쾌통쾌"}, {"name": "타짜", "duration": 5, "immersion": 5, "note": "쫄깃한 심리전"}, {"name": "올빼미", "duration": 5, "immersion": 5, "note": "팩션 스릴러"}, {"name": "파묘", "duration": 5, "immersion": 5, "note": "오컬트 장인"}, {"name": "서울의 봄", "duration": 5, "immersion": 5, "note": "시대극"}, {"name": "노트북", "duration": 5, "immersion": 4, "note": "찐 로맨스"}, {"name": "비긴 어게인", "duration": 5, "immersion": 3, "note": "음악 힐링"}, {"name": "존 윅", "duration": 5, "immersion": 4, "note": "총기 액션"}, {"name": "미션 임파서블", "duration": 5, "immersion": 4, "note": "목숨 건 액션"}, {"name": "극한직업", "duration": 5, "immersion": 3, "note": "빵 터지는 코미디"}, {"name": "엑시트", "duration": 5, "immersion": 4, "note": "재난 탈출기"}]
bgm_list = [{"name": "비 오는 날의 로파이(Lo-Fi)", "energy": 1, "focus": 1, "note": "비, 공부, 새벽"}, {"name": "새벽 감성 재즈 힙합", "energy": 2, "focus": 1, "note": "새벽, 작업, 차분함"}, {"name": "코딩할 때 듣는 백색소음", "energy": 1, "focus": 1, "note": "백색소음, 초집중"}, {"name": "지브리 애니메이션 OST 피아노", "energy": 2, "focus": 2, "note": "힐링, 피아노, 동화"}, {"name": "나른한 오후의 카페 재즈", "energy": 2, "focus": 3, "note": "커피, 휴식, 대화"}, {"name": "경쾌한 스윙 재즈", "energy": 4, "focus": 4, "note": "경쾌, 기분전환"}, {"name": "보사노바와 함께하는 브런치", "energy": 2, "focus": 2, "note": "주말, 아침, 여유"}, {"name": "밤거리의 블루스", "energy": 2, "focus": 2, "note": "밤, 혼술, 감성"}, {"name": "잔잔한 클래식 기타 독주", "energy": 1, "focus": 1, "note": "휴식, 독서, 기타"}, {"name": "웅장한 오케스트라 교향곡", "energy": 4, "focus": 2, "note": "압도, 영감, 클래식"}, {"name": "우아한 현악 사중주", "energy": 2, "focus": 2, "note": "우아함, 다과, 현악기"}, {"name": "쇼팽 피아노 녹턴", "energy": 1, "focus": 1, "note": "수면, 위로, 피아노"}, {"name": "출근길 텐션업 케이팝 댄스", "energy": 5, "focus": 5, "note": "출근길, 각성, 댄스"}, {"name": "청량한 여름 트로피컬 하우스", "energy": 4, "focus": 4, "note": "여름, 휴가, 드라이브"}, {"name": "둠칫둠칫 클럽 EDM", "energy": 5, "focus": 5, "note": "운동, 파티, 폭발"}, {"name": "드라이브할 때 듣는 시티팝", "energy": 3, "focus": 3, "note": "드라이브, 밤, 레트로"}, {"name": "리듬 타기 좋은 R&B", "energy": 3, "focus": 3, "note": "그루브, 세련됨"}, {"name": "타격감 있는 붐뱁 힙합", "energy": 4, "focus": 4, "note": "스트레스 해소, 바운스"}, {"name": "트렌디한 트랩 힙합", "energy": 4, "focus": 5, "note": "트렌디, 운동"}, {"name": "감성 싱잉랩", "energy": 3, "focus": 2, "note": "새벽감성, 드라이브"}, {"name": "가슴 뛰는 일본 밴드 애니송", "energy": 5, "focus": 4, "note": "오타쿠, 열정, 밴드"}, {"name": "잔잔한 어쿠스틱 인디 팝", "energy": 2, "focus": 2, "note": "산책, 기타, 인디"}, {"name": "몽환적인 슈게이징/포스트 락", "energy": 3, "focus": 1, "note": "몽환, 작업, 락"}, {"name": "스트레스 날리는 하드 락", "energy": 5, "focus": 5, "note": "야근, 분노의 타이핑"}, {"name": "기분 좋아지는 모던 락", "energy": 4, "focus": 3, "note": "청량, 나들이, 밴드"}, {"name": "우주를 유영하는 듯한 앰비언트", "energy": 1, "focus": 1, "note": "명상, 수면, 우주"}, {"name": "신나는 레트로 디스코", "energy": 4, "focus": 5, "note": "파티, 복고, 댄스"}, {"name": "이국적인 라틴 팝", "energy": 4, "focus": 5, "note": "여행, 정열, 남미"}, {"name": "감성적인 어쿠스틱 팝", "energy": 2, "focus": 2, "note": "카페, 배경음악"}, {"name": "에너지 넘치는 펑크(Funk)", "energy": 5, "focus": 4, "note": "베이스, 리듬, 각성"}]

f_top_list = [{"name": "무지 크롭 반팔티", "weather": 1, "formality": 1, "style": "캐주얼"}, {"name": "오프숄더 블라우스", "weather": 1, "formality": 4, "style": "페미닌"}, {"name": "퍼프 소매 블라우스", "weather": 2, "formality": 4, "style": "러블리"}, {"name": "시스루 셔츠", "weather": 1, "formality": 3, "style": "유니크"}, {"name": "스퀘어넥 티셔츠", "weather": 2, "formality": 2, "style": "페미닌"}, {"name": "얇은 린넨 셔츠", "weather": 2, "formality": 3, "style": "모던"}, {"name": "홀터넥 나시", "weather": 1, "formality": 2, "style": "바캉스"}, {"name": "레이스 블라우스", "weather": 3, "formality": 5, "style": "로맨틱"}, {"name": "실크 블라우스", "weather": 3, "formality": 5, "style": "오피스"}, {"name": "크롭 맨투맨", "weather": 3, "formality": 1, "style": "스트릿"}, {"name": "오버핏 셔츠", "weather": 3, "formality": 2, "style": "시티보이"}, {"name": "단가라 티셔츠", "weather": 3, "formality": 2, "style": "캐주얼"}, {"name": "슬림핏 목폴라", "weather": 4, "formality": 4, "style": "모던"}, {"name": "브이넥 니트", "weather": 4, "formality": 4, "style": "클래식"}, {"name": "앙고라 니트", "weather": 5, "formality": 4, "style": "포근함"}, {"name": "케이블 크롭 니트", "weather": 4, "formality": 2, "style": "프레피"}, {"name": "오프숄더 니트", "weather": 4, "formality": 4, "style": "페미닌"}, {"name": "하프넥 티셔츠", "weather": 4, "formality": 3, "style": "미니멀"}, {"name": "벌룬 소매 니트", "weather": 4, "formality": 3, "style": "러블리"}, {"name": "루즈핏 후드티", "weather": 4, "formality": 1, "style": "캐주얼"}, {"name": "벨벳 블라우스", "weather": 5, "formality": 5, "style": "연말파티"}, {"name": "두꺼운 터틀넥 니트", "weather": 5, "formality": 3, "style": "코지"}, {"name": "기모 맨투맨", "weather": 5, "formality": 1, "style": "스포티"}, {"name": "골지 긴팔 티셔츠", "weather": 3, "formality": 3, "style": "페미닌"}, {"name": "프린팅 긴팔티", "weather": 3, "formality": 1, "style": "스트릿"}, {"name": "카라 넥 니트", "weather": 4, "formality": 4, "style": "단정"}, {"name": "크로셰 가디건(단독)", "weather": 2, "formality": 3, "style": "빈티지"}, {"name": "타이 블라우스", "weather": 3, "formality": 5, "style": "오피스"}, {"name": "트위드 베스트", "weather": 3, "formality": 5, "style": "클래식"}, {"name": "언발란스 숄더 티", "weather": 3, "formality": 3, "style": "유니크"}]
f_bottom_list = [{"name": "데님 숏팬츠", "weather": 1, "formality": 1, "style": "캐주얼"}, {"name": "린넨 와이드 팬츠", "weather": 1, "formality": 3, "style": "모던"}, {"name": "플리츠 미니스커트", "weather": 2, "formality": 2, "style": "프레피"}, {"name": "바이커 쇼츠", "weather": 1, "formality": 1, "style": "스포티"}, {"name": "쉬폰 롱스커트", "weather": 2, "formality": 4, "style": "여리여리"}, {"name": "랩 스커트", "weather": 2, "formality": 4, "style": "페미닌"}, {"name": "슬릿 롱스커트", "weather": 3, "formality": 4, "style": "페미닌"}, {"name": "연청 부츠컷 데님", "weather": 3, "formality": 2, "style": "빈티지"}, {"name": "와이드 핀턱 슬랙스", "weather": 3, "formality": 5, "style": "오피스"}, {"name": "카고 스커트", "weather": 3, "formality": 2, "style": "스트릿"}, {"name": "새틴 롱스커트", "weather": 3, "formality": 5, "style": "우아함"}, {"name": "흑청 일자 데님", "weather": 4, "formality": 2, "style": "캐주얼"}, {"name": "나일론 파라슈트 팬츠", "weather": 3, "formality": 1, "style": "스트릿"}, {"name": "코듀로이 미니스커트", "weather": 4, "formality": 2, "style": "러블리"}, {"name": "레더 숏팬츠", "weather": 4, "formality": 4, "style": "시크"}, {"name": "머메이드 스커트", "weather": 4, "formality": 5, "style": "하객룩"}, {"name": "생지 데님 와이드", "weather": 4, "formality": 3, "style": "미니멀"}, {"name": "니트 롱스커트", "weather": 5, "formality": 3, "style": "코지"}, {"name": "기모 슬랙스", "weather": 5, "formality": 5, "style": "오피스"}, {"name": "코듀로이 와이드 팬츠", "weather": 5, "formality": 3, "style": "빈티지"}, {"name": "기모 스웨트 팬츠", "weather": 5, "formality": 1, "style": "스포티"}, {"name": "트위드 미니스커트", "weather": 4, "formality": 5, "style": "클래식"}, {"name": "벨벳 와이드 팬츠", "weather": 5, "formality": 4, "style": "파티"}, {"name": "플리스 조거팬츠", "weather": 5, "formality": 1, "style": "캐주얼"}, {"name": "진청 스키니진", "weather": 4, "formality": 3, "style": "모던"}, {"name": "체크 패턴 스커트", "weather": 4, "formality": 2, "style": "프레피"}, {"name": "화이트 진", "weather": 3, "formality": 3, "style": "클래식"}, {"name": "언발란스 스커트", "weather": 3, "formality": 4, "style": "유니크"}, {"name": "레이스 롱스커트", "weather": 3, "formality": 5, "style": "로맨틱"}, {"name": "부츠컷 코튼 팬츠", "weather": 3, "formality": 3, "style": "캐주얼"}]
f_onepiece_list = [{"name": "슬리브리스 미니 원피스", "weather": 1, "formality": 2, "style": "바캉스"}, {"name": "플로럴 쉬폰 원피스", "weather": 2, "formality": 3, "style": "로맨틱"}, {"name": "린넨 셔츠 원피스", "weather": 1, "formality": 4, "style": "단정"}, {"name": "퍼프 소매 롱 원피스", "weather": 2, "formality": 4, "style": "페미닌"}, {"name": "랩 디자인 원피스", "weather": 2, "formality": 4, "style": "우아함"}, {"name": "티셔츠 롱 원피스", "weather": 2, "formality": 1, "style": "꾸안꾸"}, {"name": "홀터넥 롱 원피스", "weather": 1, "formality": 3, "style": "리조트"}, {"name": "데님 뷔스티에 원피스", "weather": 3, "formality": 2, "style": "캐주얼"}, {"name": "새틴 슬립 원피스", "weather": 3, "formality": 5, "style": "파티"}, {"name": "플리츠 카라 원피스", "weather": 3, "formality": 5, "style": "하객룩"}, {"name": "스퀘어넥 미니 원피스", "weather": 3, "formality": 3, "style": "러블리"}, {"name": "셔링 디테일 원피스", "weather": 3, "formality": 4, "style": "페미닌"}, {"name": "루즈핏 셔츠 원피스", "weather": 3, "formality": 3, "style": "모던"}, {"name": "니트 뷔스티에 원피스", "weather": 4, "formality": 3, "style": "코지"}, {"name": "트위드 미니 원피스", "weather": 4, "formality": 5, "style": "클래식"}, {"name": "레더 셔츠 원피스", "weather": 4, "formality": 4, "style": "시크"}, {"name": "골지 니트 롱 원피스", "weather": 4, "formality": 3, "style": "모던"}, {"name": "오프숄더 니트 원피스", "weather": 4, "formality": 4, "style": "연말룩"}, {"name": "후드 맥시 원피스", "weather": 4, "formality": 1, "style": "스포티"}, {"name": "벨벳 미니 원피스", "weather": 5, "formality": 5, "style": "파티"}, {"name": "도톰한 터틀넥 원피스", "weather": 5, "formality": 4, "style": "포근함"}, {"name": "기모 맨투맨 원피스", "weather": 5, "formality": 1, "style": "캐주얼"}, {"name": "코듀로이 멜빵 원피스", "weather": 5, "formality": 2, "style": "빈티지"}, {"name": "아가일 니트 원피스", "weather": 5, "formality": 3, "style": "프레피"}, {"name": "머메이드 니트 원피스", "weather": 5, "formality": 4, "style": "우아함"}, {"name": "체크 패턴 롱 원피스", "weather": 4, "formality": 3, "style": "클래식"}, {"name": "언발란스 셔링 원피스", "weather": 3, "formality": 4, "style": "유니크"}, {"name": "레이스 디테일 원피스", "weather": 3, "formality": 5, "style": "로맨틱"}, {"name": "브이넥 슬릿 원피스", "weather": 4, "formality": 4, "style": "페미닌"}, {"name": "하프집업 니트 원피스", "weather": 4, "formality": 2, "style": "스포티"}]
f_outer_list = [{"name": "여름용 린넨 자켓", "weather": 2, "formality": 4, "style": "포멀"}, {"name": "크롭 반팔 자켓", "weather": 2, "formality": 4, "style": "모던"}, {"name": "얇은 볼레로 가디건", "weather": 2, "formality": 3, "style": "여리여리"}, {"name": "시스루 바람막이", "weather": 2, "formality": 1, "style": "스포티"}, {"name": "베이직 트렌치 코트", "weather": 3, "formality": 5, "style": "클래식"}, {"name": "크롭 청자켓", "weather": 3, "formality": 2, "style": "캐주얼"}, {"name": "오버핏 블레이저", "weather": 3, "formality": 4, "style": "시크"}, {"name": "비건 레더 자켓", "weather": 3, "formality": 4, "style": "모던"}, {"name": "루즈핏 가디건", "weather": 3, "formality": 2, "style": "코지"}, {"name": "노카라 트위드 자켓", "weather": 3, "formality": 5, "style": "하객룩"}, {"name": "집업 후드 가디건", "weather": 3, "formality": 1, "style": "스트릿"}, {"name": "니트 베스트", "weather": 3, "formality": 3, "style": "프레피"}, {"name": "경량 패딩 점퍼", "weather": 4, "formality": 2, "style": "실용적"}, {"name": "플리스 (뽀글이) 자켓", "weather": 4, "formality": 1, "style": "캐주얼"}, {"name": "코듀로이 크롭 자켓", "weather": 4, "formality": 3, "style": "빈티지"}, {"name": "스웨이드 자켓", "weather": 4, "formality": 4, "style": "페미닌"}, {"name": "바시티 자켓", "weather": 4, "formality": 2, "style": "스포티"}, {"name": "에코 퍼 자켓", "weather": 5, "formality": 5, "style": "화려함"}, {"name": "핸드메이드 롱 코트", "weather": 5, "formality": 5, "style": "우아함"}, {"name": "숏 무스탕", "weather": 5, "formality": 4, "style": "시크"}, {"name": "글로시 숏패딩", "weather": 5, "formality": 3, "style": "트렌디"}, {"name": "알파카 니트 가디건", "weather": 5, "formality": 3, "style": "포근함"}, {"name": "헤비 다운 롱패딩", "weather": 5, "formality": 1, "style": "생존템"}, {"name": "하프 기장 울 코트", "weather": 5, "formality": 4, "style": "클래식"}, {"name": "더플 코트 (떡볶이)", "weather": 5, "formality": 3, "style": "프레피"}, {"name": "항공점퍼 (MA-1)", "weather": 4, "formality": 2, "style": "스트릿"}, {"name": "퀼팅 자켓", "weather": 4, "formality": 3, "style": "클래식"}, {"name": "판초 / 망토 코트", "weather": 5, "formality": 4, "style": "유니크"}, {"name": "테일러드 코트", "weather": 5, "formality": 5, "style": "오피스"}, {"name": "벨티드 코트", "weather": 5, "formality": 5, "style": "페미닌"}]

m_top_list = [{"name": "무지 반팔 티셔츠", "weather": 1, "formality": 1, "style": "캐주얼"}, {"name": "오버핏 프린팅 티", "weather": 1, "formality": 1, "style": "스트릿"}, {"name": "린넨 오픈카라 셔츠", "weather": 1, "formality": 3, "style": "시티보이"}, {"name": "반팔 니트", "weather": 2, "formality": 4, "style": "미니멀"}, {"name": "반팔 옥스퍼드 셔츠", "weather": 2, "formality": 4, "style": "단정"}, {"name": "머슬핏 반팔티", "weather": 1, "formality": 1, "style": "스포티"}, {"name": "긴팔 스트라이프 티", "weather": 2, "formality": 2, "style": "캐주얼"}, {"name": "얇은 코튼 셔츠", "weather": 2, "formality": 3, "style": "모던"}, {"name": "오버핏 데님 셔츠", "weather": 3, "formality": 2, "style": "아메카지"}, {"name": "기본 옥스퍼드 셔츠", "weather": 3, "formality": 4, "style": "클래식"}, {"name": "긴팔 라운드 니트", "weather": 3, "formality": 4, "style": "미니멀"}, {"name": "하프집업 멘투맨", "weather": 3, "formality": 2, "style": "시티보이"}, {"name": "스웨트 셔츠 (맨투맨)", "weather": 3, "formality": 1, "style": "캐주얼"}, {"name": "기본 후드티", "weather": 3, "formality": 1, "style": "스트릿"}, {"name": "카라 니트 긴팔", "weather": 3, "formality": 4, "style": "비즈니스"}, {"name": "럭비 티셔츠", "weather": 3, "formality": 2, "style": "스포티"}, {"name": "두꺼운 라운드 니트", "weather": 5, "formality": 4, "style": "포근함"}, {"name": "터틀넥 니트", "weather": 5, "formality": 5, "style": "클래식"}, {"name": "기모 스웨트 셔츠", "weather": 5, "formality": 1, "style": "캐주얼"}, {"name": "기모 후드티", "weather": 5, "formality": 1, "style": "스트릿"}, {"name": "플리스 반집업", "weather": 5, "formality": 1, "style": "아웃도어"}, {"name": "케이블 니트", "weather": 4, "formality": 3, "style": "프레피"}, {"name": "모크넥 티셔츠", "weather": 4, "formality": 3, "style": "미니멀"}, {"name": "아가일 니트", "weather": 4, "formality": 3, "style": "빈티지"}, {"name": "오버핏 체크 셔츠", "weather": 3, "formality": 2, "style": "아메카지"}, {"name": "골지 터틀넥", "weather": 5, "formality": 4, "style": "시크"}, {"name": "워싱 데님 셔츠", "weather": 3, "formality": 2, "style": "캐주얼"}, {"name": "니트 베스트 (단독)", "weather": 2, "formality": 3, "style": "프레피"}, {"name": "드레스 셔츠", "weather": 3, "formality": 5, "style": "포멀"}, {"name": "피케 티셔츠 (카라티)", "weather": 2, "formality": 3, "style": "클래식"}]
m_bottom_list = [{"name": "나일론 숏팬츠", "weather": 1, "formality": 1, "style": "스포티"}, {"name": "린넨 하프 팬츠", "weather": 1, "formality": 2, "style": "리조트"}, {"name": "데님 하프 팬츠", "weather": 1, "formality": 1, "style": "캐주얼"}, {"name": "버뮤다 팬츠", "weather": 2, "formality": 2, "style": "시티보이"}, {"name": "얇은 쿨링 슬랙스", "weather": 2, "formality": 4, "style": "비즈니스"}, {"name": "연청 와이드 데님", "weather": 2, "formality": 2, "style": "스트릿"}, {"name": "테이퍼드 슬랙스", "weather": 3, "formality": 5, "style": "포멀"}, {"name": "와이드 슬랙스", "weather": 3, "formality": 4, "style": "미니멀"}, {"name": "흑청 와이드 데님", "weather": 3, "formality": 2, "style": "캐주얼"}, {"name": "치노 팬츠 (면바지)", "weather": 3, "formality": 4, "style": "클래식"}, {"name": "나일론 파라슈트 팬츠", "weather": 3, "formality": 1, "style": "스트릿"}, {"name": "카고 조거 팬츠", "weather": 3, "formality": 1, "style": "테크웨어"}, {"name": "스웨트 조거 팬츠", "weather": 3, "formality": 1, "style": "스포티"}, {"name": "생지 스트레이트 데님", "weather": 4, "formality": 3, "style": "미니멀"}, {"name": "퍼티그 팬츠", "weather": 4, "formality": 2, "style": "아메카지"}, {"name": "코듀로이 팬츠", "weather": 5, "formality": 2, "style": "빈티지"}, {"name": "기모 슬랙스", "weather": 5, "formality": 5, "style": "비즈니스"}, {"name": "기모 와이드 데님", "weather": 5, "formality": 2, "style": "캐주얼"}, {"name": "기모 스웨트 팬츠", "weather": 5, "formality": 1, "style": "스포티"}, {"name": "플리스 조거 팬츠", "weather": 5, "formality": 1, "style": "아웃도어"}, {"name": "울 블렌드 슬랙스", "weather": 5, "formality": 5, "style": "클래식"}, {"name": "진청 테이퍼드 데님", "weather": 4, "formality": 3, "style": "모던"}, {"name": "카고 팬츠 (와이드)", "weather": 3, "formality": 2, "style": "스트릿"}, {"name": "트랙 팬츠", "weather": 3, "formality": 1, "style": "스포티"}, {"name": "크롭 슬랙스", "weather": 3, "formality": 4, "style": "단정"}, {"name": "화이트 진", "weather": 3, "formality": 3, "style": "클래식"}, {"name": "워싱 그레이 데님", "weather": 4, "formality": 2, "style": "스트릿"}, {"name": "밴딩 코튼 팬츠", "weather": 3, "formality": 2, "style": "캐주얼"}, {"name": "투턱 와이드 팬츠", "weather": 4, "formality": 4, "style": "시티보이"}, {"name": "블랙 스키니진", "weather": 4, "formality": 2, "style": "락시크"}]
m_setup_list = [{"name": "여름용 린넨 셋업", "weather": 1, "formality": 4, "style": "모던"}, {"name": "나일론 반팔 하프 셋업", "weather": 1, "formality": 1, "style": "스포티"}, {"name": "오픈카라 셔츠+쇼츠 셋업", "weather": 1, "formality": 2, "style": "리조트"}, {"name": "코튼 반팔 셋업", "weather": 2, "formality": 2, "style": "캐주얼"}, {"name": "베이직 수트 셋업", "weather": 3, "formality": 5, "style": "비즈니스"}, {"name": "캐주얼 블레이저 셋업", "weather": 3, "formality": 4, "style": "미니멀"}, {"name": "데님 자켓+팬츠 셋업", "weather": 3, "formality": 2, "style": "스트릿"}, {"name": "스웨트 (맨투맨) 셋업", "weather": 3, "formality": 1, "style": "스포티"}, {"name": "후드 조거 셋업", "weather": 3, "formality": 1, "style": "캐주얼"}, {"name": "나일론 바람막이 셋업", "weather": 3, "formality": 1, "style": "아웃도어"}, {"name": "트랙탑 트레이닝 셋업", "weather": 3, "formality": 1, "style": "스트릿"}, {"name": "워크웨어 (퍼티그) 셋업", "weather": 4, "formality": 2, "style": "아메카지"}, {"name": "코듀로이 자켓 셋업", "weather": 4, "formality": 3, "style": "빈티지"}, {"name": "울 블렌드 수트 셋업", "weather": 5, "formality": 5, "style": "클래식"}, {"name": "기모 스웨트 셋업", "weather": 5, "formality": 1, "style": "코지"}, {"name": "기모 후드 조거 셋업", "weather": 5, "formality": 1, "style": "스포티"}, {"name": "플리스 (뽀글이) 셋업", "weather": 5, "formality": 1, "style": "아웃도어"}, {"name": "벨벳 트레이닝 셋업", "weather": 5, "formality": 2, "style": "유니크"}, {"name": "트위드 남성 셋업", "weather": 4, "formality": 5, "style": "파티"}, {"name": "아노락 하프집업 셋업", "weather": 3, "formality": 1, "style": "테크웨어"}, {"name": "스트라이프 수트 셋업", "weather": 4, "formality": 5, "style": "포멀"}, {"name": "카디건+슬랙스 니트 셋업", "weather": 4, "formality": 4, "style": "모던"}, {"name": "반집업 니트 셋업", "weather": 4, "formality": 3, "style": "코지"}, {"name": "블루종 점퍼 셋업", "weather": 4, "formality": 2, "style": "아메카지"}, {"name": "테일러드 더블 수트 셋업", "weather": 5, "formality": 5, "style": "클래식"}, {"name": "아방가르드 오버핏 셋업", "weather": 4, "formality": 4, "style": "스트릿"}, {"name": "체크 패턴 수트 셋업", "weather": 4, "formality": 5, "style": "프레피"}, {"name": "피그먼트 스웨트 셋업", "weather": 3, "formality": 1, "style": "빈티지"}, {"name": "조끼+팬츠 쓰리피스 셋업", "weather": 4, "formality": 5, "style": "클래식"}, {"name": "숏자켓 와이드 셋업", "weather": 3, "formality": 4, "style": "미니멀"}]
m_outer_list = [{"name": "여름용 반팔 블레이저", "weather": 2, "formality": 4, "style": "모던"}, {"name": "린넨 셔츠 자켓", "weather": 2, "formality": 3, "style": "시티보이"}, {"name": "얇은 나일론 바람막이", "weather": 2, "formality": 1, "style": "스포티"}, {"name": "기본 블레이저 자켓", "weather": 3, "formality": 5, "style": "비즈니스"}, {"name": "오버핏 블레이저", "weather": 3, "formality": 4, "style": "미니멀"}, {"name": "청자켓 (데님 자켓)", "weather": 3, "formality": 2, "style": "캐주얼"}, {"name": "바람막이 (윈드브레이커)", "weather": 3, "formality": 1, "style": "고프코어"}, {"name": "가죽 자켓 (라이더)", "weather": 3, "formality": 3, "style": "시크"}, {"name": "MA-1 (항공점퍼)", "weather": 3, "formality": 2, "style": "스트릿"}, {"name": "트렌치 코트", "weather": 3, "formality": 5, "style": "클래식"}, {"name": "맥코트", "weather": 4, "formality": 4, "style": "모던"}, {"name": "바시티 자켓 (야구점퍼)", "weather": 4, "formality": 2, "style": "프레피"}, {"name": "가디건 (오버핏)", "weather": 3, "formality": 3, "style": "남친룩"}, {"name": "스웨이드 자켓", "weather": 4, "formality": 4, "style": "미니멀"}, {"name": "경량 패딩 조끼", "weather": 4, "formality": 3, "style": "직장인"}, {"name": "경량 패딩 점퍼", "weather": 4, "formality": 2, "style": "실용적"}, {"name": "코듀로이 자켓", "weather": 4, "formality": 2, "style": "아메카지"}, {"name": "플리스 자켓", "weather": 4, "formality": 1, "style": "캐주얼"}, {"name": "퀼팅 자켓 (깔깔이)", "weather": 4, "formality": 3, "style": "클래식"}, {"name": "울 싱글 코트", "weather": 5, "formality": 5, "style": "포멀"}, {"name": "울 발마칸 코트", "weather": 5, "formality": 4, "style": "시티보이"}, {"name": "더플 코트", "weather": 5, "formality": 3, "style": "프레피"}, {"name": "무스탕 자켓", "weather": 5, "formality": 4, "style": "시크"}, {"name": "숏패딩 (푸퍼)", "weather": 5, "formality": 2, "style": "스트릿"}, {"name": "헤비 다운 롱패딩", "weather": 5, "formality": 1, "style": "생존템"}, {"name": "야상 패딩 (파카)", "weather": 5, "formality": 2, "style": "아웃도어"}, {"name": "오버핏 더블 코트", "weather": 5, "formality": 5, "style": "클래식"}, {"name": "해리스 트위드 자켓", "weather": 4, "formality": 4, "style": "포멀"}, {"name": "레더 블루종", "weather": 4, "formality": 3, "style": "모던"}, {"name": "체크 블루종 점퍼", "weather": 4, "formality": 2, "style": "캐주얼"}]

solo_list = [
    {"name": "동네 숨은 카페에서 책 읽기", "crowd": 1, "energy": 1, "solo_level": 1, "note": "감성 충전"},
    {"name": "혼자 코인노래방 2시간 달리기", "crowd": 2, "energy": 4, "solo_level": 1, "note": "스트레스 해소"},
    {"name": "사람 많은 핫플 카페에서 사람 구경", "crowd": 5, "energy": 1, "solo_level": 2, "note": "트렌드 파악"},
    {"name": "조조 영화 혼자 보며 팝콘 먹기", "crowd": 2, "energy": 1, "solo_level": 1, "note": "소확행"},
    {"name": "심야 영화 공포물 혼자 보기", "crowd": 1, "energy": 2, "solo_level": 3, "note": "오싹함"},
    {"name": "집 근처 편의점 신상 털기", "crowd": 1, "energy": 1, "solo_level": 1, "note": "가성비 갑"},
    {"name": "혼자 한강 공원 벤치에서 물멍", "crowd": 3, "energy": 1, "solo_level": 2, "note": "사색의 시간"},
    {"name": "혼자 도서관 가서 관심 없는 분야 책 읽기", "crowd": 2, "energy": 1, "solo_level": 2, "note": "지식 확장"},
    {"name": "혼자 따릉이 타고 목적지 없이 달리기", "crowd": 3, "energy": 4, "solo_level": 1, "note": "바람 쐬기"},
    {"name": "다이소 가서 1만원으로 소확행 쇼핑", "crowd": 3, "energy": 2, "solo_level": 1, "note": "탕진잼"},
    {"name": "올리브영 혼자서 1시간 구경하기", "crowd": 4, "energy": 2, "solo_level": 1, "note": "뷰티 힐링"},
    {"name": "대형 서점 베스트셀러 코너 정독", "crowd": 4, "energy": 2, "solo_level": 2, "note": "마음의 양식"},
    {"name": "혼자 전시회 가서 오디오 가이드 듣기", "crowd": 3, "energy": 2, "solo_level": 3, "note": "문화 생활"},
    {"name": "혼자 미술관 가서 작품 감상", "crowd": 2, "energy": 2, "solo_level": 3, "note": "예술적 영감"},
    {"name": "독립 서점 투어하며 굿즈 사기", "crowd": 1, "energy": 3, "solo_level": 2, "note": "감성 스팟"},
    {"name": "혼자 사진관 가서 네컷 사진 찍기", "crowd": 2, "energy": 2, "solo_level": 2, "note": "추억 남기기"},
    {"name": "혼자 셀프 세차장 가서 차 닦기", "crowd": 2, "energy": 5, "solo_level": 2, "note": "노동의 땀방울"},
    {"name": "동네 마트에서 혼술 안주 장보기", "crowd": 3, "energy": 2, "solo_level": 1, "note": "저녁 준비"},
    {"name": "혼자 방탈출 카페 가기", "crowd": 2, "energy": 4, "solo_level": 4, "note": "뇌섹남녀"},
    {"name": "혼자 보드게임 카페 가서 퍼즐 풀기", "crowd": 2, "energy": 3, "solo_level": 3, "note": "집중력 향상"},
    {"name": "혼자 PC방 가서 컵라면 먹으며 게임", "crowd": 4, "energy": 2, "solo_level": 1, "note": "국룰 힐링"},
    {"name": "혼자 만화카페 가서 짜파게티 먹기", "crowd": 2, "energy": 1, "solo_level": 1, "note": "시간 순삭"},
    {"name": "혼자 찜질방 가서 식혜에 계란 까먹기", "crowd": 4, "energy": 1, "solo_level": 2, "note": "피로 회복"},
    {"name": "혼자 볼링장 가서 3게임 치기", "crowd": 3, "energy": 4, "solo_level": 3, "note": "스포츠"},
    {"name": "혼자 당구장 가서 연습하기", "crowd": 3, "energy": 3, "solo_level": 3, "note": "스킬업"},
    {"name": "혼자 동전 야구장에서 배팅 연습", "crowd": 2, "energy": 5, "solo_level": 2, "note": "스트레스 해소"},
    {"name": "혼자 실내 클라이밍장 가기", "crowd": 3, "energy": 5, "solo_level": 3, "note": "성취감"},
    {"name": "혼자 헬스장 가서 하체 조지기", "crowd": 4, "energy": 5, "solo_level": 1, "note": "득근득근"},
    {"name": "혼자 동네 뒷산 등산하기", "crowd": 1, "energy": 5, "solo_level": 2, "note": "자연 힐링"},
    {"name": "혼자 북한산 등 험한 산 등반하기", "crowd": 2, "energy": 5, "solo_level": 3, "note": "도전 정신"},
    {"name": "혼자 한강공원 러닝 5km", "crowd": 3, "energy": 5, "solo_level": 1, "note": "유산소"},
    {"name": "혼자 수영장 가서 자유수영 1시간", "crowd": 4, "energy": 5, "solo_level": 2, "note": "칼로리 버닝"},
    {"name": "혼자 식물원 가서 피톤치드 쐬기", "crowd": 2, "energy": 2, "solo_level": 2, "note": "안구 정화"},
    {"name": "혼자 동물원/아쿠아리움 가기", "crowd": 4, "energy": 3, "solo_level": 4, "note": "동심 회복"},
    {"name": "혼자 고궁(경복궁 등) 산책하기", "crowd": 4, "energy": 3, "solo_level": 2, "note": "역사 나들이"},
    {"name": "혼자 남산타워 걸어 올라가기", "crowd": 4, "energy": 5, "solo_level": 3, "note": "야경 감상"},
    {"name": "혼자 이케아/가구점 쇼룸 구경하기", "crowd": 5, "energy": 4, "solo_level": 2, "note": "인테리어 뽐뿌"},
    {"name": "혼자 백화점 아이쇼핑 3시간", "crowd": 5, "energy": 4, "solo_level": 1, "note": "다리 아픔"},
    {"name": "혼자 성수동 팝업스토어 투어", "crowd": 5, "energy": 4, "solo_level": 3, "note": "힙스터 등극"},
    {"name": "혼자 플리마켓 구경하며 소품 사기", "crowd": 4, "energy": 3, "solo_level": 2, "note": "득템 찬스"},
    {"name": "혼자 공방 가서 도자기/향수 만들기", "crowd": 1, "energy": 3, "solo_level": 3, "note": "원데이 클래스"},
    {"name": "혼자 베이킹 클래스 참여하기", "crowd": 2, "energy": 3, "solo_level": 3, "note": "요리왕"},
    {"name": "혼자 국밥집 가서 뜨끈한 국밥 먹기", "crowd": 3, "energy": 1, "solo_level": 1, "note": "혼밥 하수"},
    {"name": "혼자 패스트푸드점에서 세트 먹기", "crowd": 4, "energy": 1, "solo_level": 1, "note": "빠른 식사"},
    {"name": "혼자 분식집에서 떡튀순 클리어", "crowd": 3, "energy": 1, "solo_level": 1, "note": "소울 푸드"},
    {"name": "혼자 중국집에서 짜장면 완그릇", "crowd": 3, "energy": 1, "solo_level": 1, "note": "기본 혼밥"},
    {"name": "혼자 라멘집/텐동집 다찌석 앉기", "crowd": 4, "energy": 1, "solo_level": 1, "note": "프로 혼밥러석"},
    {"name": "혼자 파스타/양식집 가서 식사", "crowd": 3, "energy": 1, "solo_level": 3, "note": "분위기 있는 혼밥"},
    {"name": "혼자 유명 맛집 1시간 웨이팅하기", "crowd": 5, "energy": 2, "solo_level": 4, "note": "의지의 한국인"},
    {"name": "혼자 회전초밥집 가서 접시 쌓기", "crowd": 4, "energy": 1, "solo_level": 2, "note": "플렉스"},
    {"name": "혼자 패밀리 레스토랑(아웃백) 가기", "crowd": 5, "energy": 1, "solo_level": 5, "note": "혼놀 만렙"},
    {"name": "혼자 뷔페(애슐리, 쿠우쿠우) 가기", "crowd": 5, "energy": 2, "solo_level": 5, "note": "눈치 안 보고 먹방"},
    {"name": "혼자 고기집 가서 삼겹살 2인분 굽기", "crowd": 4, "energy": 3, "solo_level": 5, "note": "진정한 용자"},
    {"name": "혼자 곱창집/막창집 가기", "crowd": 4, "energy": 2, "solo_level": 5, "note": "소주 땡김"},
    {"name": "혼자 이자카야 가서 꼬치에 맥주", "crowd": 3, "energy": 1, "solo_level": 4, "note": "고독한 미식가"},
    {"name": "혼자 바(Bar) 가서 칵테일 마시기", "crowd": 2, "energy": 1, "solo_level": 3, "note": "분위기 깡패"},
    {"name": "혼자 동네 호프집 가서 치맥", "crowd": 3, "energy": 1, "solo_level": 4, "note": "퇴근 후 힐링"},
    {"name": "혼자 혼술 전용 술집 탐방", "crowd": 1, "energy": 1, "solo_level": 2, "note": "혼술 환영"},
    {"name": "혼자 야구장/축구장 직관 가기", "crowd": 5, "energy": 4, "solo_level": 4, "note": "열정 응원"},
    {"name": "혼자 콘서트/뮤직 페스티벌 가기", "crowd": 5, "energy": 5, "solo_level": 4, "note": "음악에 미치다"},
    {"name": "혼자 뮤지컬/연극 맨 앞줄 관람", "crowd": 4, "energy": 2, "solo_level": 3, "note": "감동 백배"},
    {"name": "혼자 호캉스 가기 (룸서비스 필수)", "crowd": 1, "energy": 1, "solo_level": 3, "note": "돈이 최고야"},
    {"name": "혼자 모텔/호텔 대실해서 넷플릭스", "crowd": 1, "energy": 1, "solo_level": 2, "note": "완벽한 고립"},
    {"name": "혼자 KTX 타고 당일치기 기차 여행", "crowd": 3, "energy": 4, "solo_level": 4, "note": "낭만 여행"},
    {"name": "혼자 고속버스 타고 낯선 도시 가기", "crowd": 3, "energy": 4, "solo_level": 4, "note": "모험가"},
    {"name": "혼자 바다 보러 훌쩍 떠나기", "crowd": 2, "energy": 4, "solo_level": 4, "note": "감성 폭발"},
    {"name": "혼자 캠핑장 가서 텐트 치고 불멍", "crowd": 2, "energy": 5, "solo_level": 5, "note": "솔로 캠퍼"},
    {"name": "혼자 글램핑장 예약해서 고기 굽기", "crowd": 2, "energy": 3, "solo_level": 4, "note": "럭셔리 휴식"},
    {"name": "혼자 놀이공원 가서 롤러코스터 타기", "crowd": 5, "energy": 5, "solo_level": 5, "note": "놀이기구 마스터"},
    {"name": "혼자 워터파크 가서 파도풀 타기", "crowd": 5, "energy": 5, "solo_level": 5, "note": "시선 강탈"},
    {"name": "혼자 스키장/썰매장 가기", "crowd": 5, "energy": 5, "solo_level": 5, "note": "겨울 레포츠"},
    {"name": "혼자 아이스 스케이트장 가기", "crowd": 4, "energy": 5, "solo_level": 4, "note": "트리플 악셀"},
    {"name": "혼자 실내 서핑/웨이크보드 타기", "crowd": 3, "energy": 5, "solo_level": 4, "note": "이색 액티비티"},
    {"name": "혼자 VR 카페/게임장 가기", "crowd": 3, "energy": 3, "solo_level": 3, "note": "가상 현실"},
    {"name": "혼자 보타닉 가든/수목원 출사", "crowd": 2, "energy": 3, "solo_level": 2, "note": "사진 작가"},
    {"name": "혼자 독립영화관 가서 예술영화 보기", "crowd": 1, "energy": 1, "solo_level": 2, "note": "씨네필"},
    {"name": "혼자 동네 철물점/문구점 구경", "crowd": 1, "energy": 2, "solo_level": 1, "note": "잡동사니 쇼핑"},
    {"name": "혼자 시장 가서 떡볶이 사먹기", "crowd": 4, "energy": 3, "solo_level": 1, "note": "인심 가득"},
    {"name": "혼자 타로/사주 보러 가기", "crowd": 2, "energy": 1, "solo_level": 2, "note": "미래 궁금증"},
    {"name": "혼자 마사지샵 가서 전신 관리", "crowd": 1, "energy": 1, "solo_level": 2, "note": "자본주의 힐링"},
    {"name": "혼자 네일아트/패디큐어 받기", "crowd": 1, "energy": 1, "solo_level": 1, "note": "기분 전환"},
    {"name": "혼자 미용실 가서 염색/파마", "crowd": 2, "energy": 1, "solo_level": 1, "note": "이미지 변신"},
    {"name": "혼자 바버샵 가서 풀 코스 관리", "crowd": 1, "energy": 1, "solo_level": 2, "note": "멋쟁이"},
    {"name": "혼자 드라이브하며 음악 크게 틀기", "crowd": 1, "energy": 2, "solo_level": 2, "note": "나만의 콘서트"},
    {"name": "혼자 목적지 없이 버스 종점까지 가기", "crowd": 2, "energy": 1, "solo_level": 2, "note": "멍 때리기"},
    {"name": "혼자 지하철 순환선 한 바퀴 돌기", "crowd": 3, "energy": 1, "solo_level": 2, "note": "인간 관찰"},
    {"name": "혼자 자전거 타고 한강 다리 건너기", "crowd": 3, "energy": 4, "solo_level": 2, "note": "야경 명소"},
    {"name": "혼자 헌혈의 집 가서 헌혈하기", "crowd": 2, "energy": 1, "solo_level": 2, "note": "착한 일"},
    {"name": "혼자 유기견 보호소 봉사활동 가기", "crowd": 3, "energy": 4, "solo_level": 3, "note": "뿌듯함"},
    {"name": "혼자 성당/절/절에 가서 명상", "crowd": 1, "energy": 1, "solo_level": 2, "note": "이너 피스"},
    {"name": "혼자 대형 마트 시식 코너 투어", "crowd": 5, "energy": 3, "solo_level": 3, "note": "눈치 게임"},
    {"name": "혼자 동네 놀이터 그네 타기", "crowd": 1, "energy": 2, "solo_level": 1, "note": "동심 회복"},
    {"name": "혼자 강아지 산책 시키며 다른 강아지 보기", "crowd": 2, "energy": 3, "solo_level": 1, "note": "멍멍이 힐링"},
    {"name": "혼자 템플스테이 1박 2일", "crowd": 1, "energy": 2, "solo_level": 4, "note": "속세 탈출"},
    {"name": "혼자 원데이 디제잉 클래스", "crowd": 1, "energy": 3, "solo_level": 3, "note": "둠칫둠칫"},
    {"name": "혼자 퍼스널 컬러 진단 받기", "crowd": 1, "energy": 1, "solo_level": 2, "note": "나를 찾아서"},
    {"name": "혼자 방 구석에서 스마트폰 전원 끄기", "crowd": 1, "energy": 1, "solo_level": 3, "note": "디지털 디톡스"},
    {"name": "혼자 레고/프라모델 조립 카페 가기", "crowd": 2, "energy": 2, "solo_level": 2, "note": "취미 집중"},
    {"name": "혼자 피시방 10시간 정액제 끊기", "crowd": 4, "energy": 2, "solo_level": 3, "note": "폐인 모드"},
    {"name": "혼자 헌책방 가서 희귀본 찾기", "crowd": 1, "energy": 2, "solo_level": 2, "note": "보물 찾기"},
    {"name": "혼자 한강 유람선 타기", "crowd": 3, "energy": 2, "solo_level": 4, "note": "고독한 선장"},
    {"name": "혼자 식기/그릇 편집샵 구경", "crowd": 2, "energy": 3, "solo_level": 2, "note": "살림 장만"},
    {"name": "혼자 셀프 스튜디오에서 컨셉 사진", "crowd": 1, "energy": 3, "solo_level": 3, "note": "모델 놀이"},
    {"name": "혼자 방청객으로 예능 녹화 참여", "crowd": 5, "energy": 3, "solo_level": 4, "note": "리액션 알바"},
    {"name": "혼자 동네 문화센터 요가 클래스", "crowd": 3, "energy": 4, "solo_level": 2, "note": "유연성 기르기"},
    {"name": "혼자 실내 스카이다이빙", "crowd": 3, "energy": 5, "solo_level": 4, "note": "익스트림"},
    {"name": "혼자 한복 빌려 입고 고궁 투어", "crowd": 4, "energy": 4, "solo_level": 5, "note": "외국인 코스프레"},
    {"name": "혼자 LP바 가서 신청곡 듣기", "crowd": 2, "energy": 1, "solo_level": 3, "note": "아날로그 감성"},
    {"name": "혼자 전통 찻집 가서 쌍화차 마시기", "crowd": 1, "energy": 1, "solo_level": 2, "note": "다도 체험"},
    {"name": "혼자 만보 걷기 챌린지 달성", "crowd": 2, "energy": 5, "solo_level": 1, "note": "건강이 최고"},
    {"name": "혼자 오픈런으로 베이글 맛집 가기", "crowd": 5, "energy": 2, "solo_level": 3, "note": "빵지순례"},
    {"name": "혼자 수산시장 가서 회 떠먹기", "crowd": 4, "energy": 3, "solo_level": 4, "note": "흥정의 신"},
    {"name": "혼자 포장마차 가서 우동에 소주", "crowd": 3, "energy": 2, "solo_level": 4, "note": "으른의 맛"},
    {"name": "혼자 조립식 가구 사와서 조립하기", "crowd": 1, "energy": 4, "solo_level": 2, "note": "목수 빙의"},
    {"name": "혼자 전시회 오픈 파티 가기", "crowd": 4, "energy": 3, "solo_level": 4, "note": "인싸 빙의"},
    {"name": "혼자 게스트하우스 1박", "crowd": 3, "energy": 3, "solo_level": 4, "note": "새로운 만남"},
    {"name": "혼자 폴댄스 일일 체험", "crowd": 2, "energy": 5, "solo_level": 3, "note": "코어 단련"},
    {"name": "혼자 크로스핏 체험반 가기", "crowd": 4, "energy": 5, "solo_level": 3, "note": "죽음의 WOD"}
]


if st.sidebar.button("🔄 전체 영수증 초기화", key="reset"):
    st.session_state.results = {'오늘의 운세 🍀': None, '오늘 뭐 먹지? 🍽️': None, '오늘 뭐 마시지? ☕': None, '오늘 뭐 입지? 👕': None, '오늘 뭐 보지? 🎬': None, '오늘 우리 뭐 하지? 👫': None, '오늘 혼자 뭐 하지? 🏃': None, '오늘 뭐 듣지? 🎧': None}
    st.session_state.candidates_text = ""
    st.session_state.show_balloons = False
    st.rerun()

if menu == '오늘의 운세 🍀':
    st.subheader("오늘의 운세 🍀")
    
    if st.button("오늘의 운세 뽑기 🥠"):
        fortune_status = st.empty()
        for i in range(15):
            cookie_pos = " " * i + "🥠"
            fortune_status.markdown(f"**당신의 행운을 배달하는 중입니다...**\n\n{cookie_pos} 슝~")
            time.sleep(0.08) 
        fortune_status.empty() 
        
        # [수정된 부분] 철학적 문구와 별점 추가
      # [완벽 수정] 철학적 문구와 별점 추가
        picked_text = random.choice(philosophical_fortunes)
        star_count = random.randint(1, 5)
        stars = "⭐" * star_count
        picked_item = random.choice(lucky_items)
        
        # 데이터를 딕셔너리로 깔끔하게 저장합니다.
        st.session_state.results['오늘의 운세 🍀'] = {
            "stars": stars, "text": picked_text, "item": picked_item
        }
        st.rerun() 

    if st.session_state.results['오늘의 운세 🍀']:
        res = st.session_state.results['오늘의 운세 🍀']
        # 요청하신 형식대로 텍스트 레이블을 명시적으로 붙여 출력합니다.
        st.markdown(f"### 오늘의 운세 별점: {res['stars']}")
        st.write("---")
        st.success(f"🔮 {res['text']}")
        st.info(f"행운의 아이템: {res['item']}")
else:
    st.subheader(f"[{menu}] 어떻게 결정할까요?")
    
    if menu == '오늘 뭐 입지? 👕':
        gender = st.radio("성별을 선택하세요:", ["여성", "남성"], horizontal=True)

    # ── 모임 마스터 탭 ────────────────────────────────────────────────
    if menu == '오늘 우리 뭐 하지? 👫':
        col_mt, col_tr = st.columns(2)
        with col_mt:
            meeting_type_choice = st.radio("모임 유형", ["💕 데이트", "🍻 친구 모임"], horizontal=True)
        with col_tr:
            transport_choice = st.radio("교통수단", ["👟 뚜벅이", "🚗 자차 있음"], horizontal=True)

        choice_mode = st.radio("선택 방식을 골라주세요:", ["완전 랜덤 🎲", "내 맘대로 조건 선택 🎛️"])

        user_awk, user_crowd, user_energy = 3, 3, 3
        if choice_mode == "내 맘대로 조건 선택 🎛️":
            user_awk    = st.slider("어색함 지수 (1: 찐친/연인 ~ 5: 소개팅/초면)", 1, 5, 3)
            user_crowd  = st.slider("인파 지수 (1: 조용하고 프라이빗 ~ 5: 시끌벅적 핫플)", 1, 5, 3)
            user_energy = st.slider("활동 지수 (1: 가만히 힐링 ~ 5: 땀나는 액티비티)", 1, 5, 3)

    else:
        choice_mode = st.radio("선택 방식을 골라주세요:", ["완전 랜덤 🎲", "내 맘대로 조건 선택 🎛️"])

    # key 설정
    if menu == '오늘 뭐 보지? 🎬':
        # 애니메이션 탭이 추가된 버전입니다!
        watch_category = st.radio("어떤 종류의 영상을 볼까요?", ["유튜브", "드라마", "예능", "영화", "애니메이션"], horizontal=True)
        if watch_category == "유튜브": current_list = youtube_list
        elif watch_category == "드라마": current_list = drama_list
        elif watch_category == "예능": current_list = variety_list
        elif watch_category == "애니메이션": current_list = ani_list # 추가된 애니메이션 연결
        else: current_list = movie_list
        key1, key2, key3 = 'duration', 'immersion', None
    elif menu == '오늘 뭐 먹지? 🍽️': 
        # 1. 사용자에게 카테고리, 무게감, 다이어트 여부를 물어봅니다.
        food_category = st.multiselect("선호 카테고리 (최소 하나 선택)", ["한식", "중식", "일식", "양식", "동남아식", "퓨전", "디저트"], default=["한식"])
        
        col_w, col_d = st.columns(2)
        with col_w:
            food_weight = st.radio("식사 무게감", ["상관없음", "라이트", "헤비"])
        with col_d:
            is_diet = st.checkbox("🏃 다이어트 중 (저칼로리/건강식)")

        # [필터링 로직 강화] 버튼을 누르기 전에 리스트를 미리 걸러냅니다.
        # 1. 카테고리 필터링
        current_list = [f for f in food_list if f['category'] in food_category]
        
        # 2. 다이어트 필터링 (체크 시 True인 것만 남김)
        if is_diet:
            current_list = [f for f in current_list if f.get('is_diet') == True]
            
        # 3. 무게감 필터링
        if food_weight != "상관없음":
            current_list = [f for f in current_list if f.get('weight') == food_weight]
            
        # [중요] 필터 결과가 없을 때 경고창을 띄웁니다.
        if not current_list:
            st.warning("⚠️ 선택하신 조건(카테고리+다이어트+무게감)을 모두 만족하는 음식이 없습니다. 조건을 조금 더 넓혀주세요!")
            
        # 매칭 알고리즘에 사용할 키 설정
        key1, key2, key3 = 'budget', 'laziness', None
    elif menu == '오늘 우리 뭐 하지? 👫':
        current_list = together_list
        key1, key2, key3 = 'awkwardness', 'crowd', 'energy'
    elif menu == '오늘 뭐 듣지? 🎧':
        current_list = bgm_list
        key1, key2, key3 = 'energy', 'focus', None
    elif menu == '오늘 뭐 마시지? ☕':
        current_list = cafe_list
        key1, key2, key3 = 'caffeine', 'sweetness', None
    elif menu == '오늘 뭐 입지? 👕':
        key1, key2, key3 = None, None, None
    elif menu == '오늘 혼자 뭐 하지? 🏃':
        current_list = solo_list
        key1, key2, key3 = 'crowd', 'energy', 'solo_level'

    user_val1, user_val2, user_val3 = 3, 3, None
    exclude_keywords = []

    if menu != '오늘 우리 뭐 하지? 👫' and choice_mode == "내 맘대로 조건 선택 🎛️":
        if menu == '오늘 뭐 입지? 👕':
            user_val1 = st.slider("날씨 (1: 한여름 폭염 ~ 5: 한겨울 꽁꽁)", 1, 5, 3)
            user_val2 = st.slider("격식 (1: 동네 마실 ~ 5: 격식 있는 자리)", 1, 5, 3)
        elif menu == '오늘 뭐 듣지? 🎧':
            user_val1 = st.slider("에너지 (1: 차분함 ~ 5: 텐션 폭발)", 1, 5, 3)
            user_val2 = st.slider("집중도 (1: 집중력 필요 ~ 5: 생각 없이 신나게)", 1, 5, 3)
        elif menu == '오늘 뭐 마시지? ☕':
            user_val1 = st.slider("카페인 (1: 디카페인/논커피 ~ 5: 고카페인 수혈)", 1, 5, 3)
            user_val2 = st.slider("당 충전 (1: 전혀 안 담 ~ 5: 당 충전 100%)", 1, 5, 3)
        elif menu == '오늘 뭐 보지? 🎬':
            # [수정] 유튜브일 때만 영상 길이 슬라이더가 나타납니다.
            if watch_category == "유튜브":
                user_val1 = st.slider("영상 길이 (1: 10분 이하 ~ 5: 1시간 이상)", 1, 5, 3)
            else:
                user_val1 = 5 # 드라마, 영화, 애니 등은 자동으로 '긴 영상'으로 처리합니다.
            
            # 몰입도는 어떤 장르든 공통적으로 조절합니다.
            user_val2 = st.slider("몰입도 (1: 오디오용 ~ 5: 화면 뚫어져라)", 1, 5, 3)
        elif menu == '오늘 혼자 뭐 하지? 🏃':
            user_val1 = st.slider("인파 지수 (1: 조용한 곳 ~ 5: 북적이는 핫플)", 1, 5, 3)
            user_val2 = st.slider("활동 지수 (1: 가만히 힐링 ~ 5: 땀나는 액티비티)", 1, 5, 3)
            user_val3 = st.slider("혼놀 레벨 (1: 혼놀 하수 ~ 5: 혼놀 만렙)", 1, 5, 3)
        else:
            user_val1 = st.slider("예산 (1: 돈 없어ㅠ ~ 5: 플렉스!)", 1, 5, 3)
            user_val2 = st.slider("귀찮음 지수 (1: 완전 활동적 ~ 5: 침대 밖은 위험해)", 1, 5, 3)
            
        if menu == '오늘 뭐 먹지? 🍽️':
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.checkbox("밀가루 빼기"): exclude_keywords.append("밀가루")
            with col2:
                if st.checkbox("고기 빼기"): exclude_keywords.append("고기")
            with col3:
                if st.checkbox("매운거 빼기"): exclude_keywords.append("매운거")

    def get_best_choice(data, u_val1, u_val2, excludes, k1, k2, u_val3=None, k3=None):
        # 1. 제외 키워드 필터링
        filtered_data = [item for item in data if not any(ex_word in item.get('note', '') or ex_word in item.get('style', '') for ex_word in excludes)]
        
        # [엄격한 통제] 조건에 안 맞으면 강제로 전체 데이터를 불러오던 코드를 삭제했습니다.
        # 이제 조건에 안 맞으면 무조건 0개(None)를 반환하여 결과를 엄격하게 차단합니다.
        if not filtered_data:
            return None, []

        scored_data = []
        for item in filtered_data:
            diff = abs(item.get(k1, 3) - u_val1) + abs(item.get(k2, 3) - u_val2)
            if k3 is not None and u_val3 is not None:
                diff += abs(item.get(k3, 3) - u_val3)
            scored_data.append({'item': item, 'diff': diff})
        
        scored_data.sort(key=lambda x: x['diff'])
        min_diff = scored_data[0]['diff']
        best_candidates = [x['item'] for x in scored_data if x['diff'] <= min_diff + 1] 
        
        return random.choice(best_candidates), best_candidates

        scored_data = []
        for item in filtered_data:
            # 슬라이더 값과의 차이 계산 (차이가 적을수록 좋은 점수)
            # .get(key, 3)을 사용하여 해당 데이터가 없을 경우 중간값(3)으로 처리해 에러를 방지합니다.
            diff = abs(item.get(k1, 3) - u_val1) + abs(item.get(k2, 3) - u_val2)
            if k3 is not None and u_val3 is not None:
                diff += abs(item.get(k3, 3) - u_val3)
            scored_data.append({'item': item, 'diff': diff})
        
        # 차이가 적은 순서대로 정렬
        scored_data.sort(key=lambda x: x['diff'])
        
        # 최적의 후보들 추출 (가장 차이가 적은 것부터 약간의 오차 범위를 줌)
        min_diff = scored_data[0]['diff']
        best_candidates = [x['item'] for x in scored_data if x['diff'] <= min_diff + 1] 
        
        return random.choice(best_candidates), best_candidates

    
    st.write("---")
    
    # ── [수정] 횟수 제한 삭제: 언제든 무제한으로 돌릴 수 있습니다! ──
    if st.button("운명의 결정 내리기! 🔮"):
        progress_bar = st.progress(0)
        status_text = st.empty() 
        
        for i in range(100):
            progress_bar.progress(i + 1)
            ball_pos = " " * ((i // 3) % 15) + "🔮"
            status_text.markdown(f"**선택 천재가 당신의 운명을 결정 중입니다...**\n\n{ball_pos} 데구르르...")
            time.sleep(0.03) 
            
        progress_bar.empty() 
        status_text.empty()  

        # ── 1. 모임 마스터 로직 ──
        if menu == '오늘 우리 뭐 하지? 👫':
            mt_key   = '데이트' if meeting_type_choice == "💕 데이트" else '친구모임'
            is_walk  = (transport_choice == "👟 뚜벅이")

            filtered = [x for x in together_list if x['meeting_type'] in (mt_key, '공통')]
            if is_walk:
                filtered = [x for x in filtered if x['mobility'] <= 2] # 뚜벅이는 가까운 곳만
            else:
                filtered = [x for x in filtered if x['mobility'] >= 4] # 자차는 드라이브/여행 필수

            if not filtered:
                st.error("조건이 너무 깐깐합니다! 슬라이더 조건을 조금 완화해주세요.")
                st.stop()

            if choice_mode == "내 맘대로 조건 선택 🎛️":
                final_result, candidates = get_best_choice(
                    filtered, user_awk, user_crowd, [], 'awkwardness', 'crowd', user_energy, 'energy'
                )
                if not final_result:
                    st.error("조건이 너무 깐깐합니다! 슬라이더 조건을 조금 완화해주세요.")
                    st.stop()
                c_names = [c['name'] for c in candidates]
                st.session_state.candidates_text = f"💡 (참고) 최종 후보에 올랐던 것들: {', '.join(c_names)}"
            else:
                final_result = random.choice(filtered)
                st.session_state.candidates_text = "🎲 완전 랜덤으로 뽑은 결과입니다."

            final_result = dict(final_result)
            final_result['_meeting_type_choice'] = meeting_type_choice
            final_result['_transport_choice'] = transport_choice
            st.session_state.results[menu] = final_result

        # ── 2. 오늘 뭐 입지 코디 로직 ──
        elif menu == '오늘 뭐 입지? 👕':
            is_onepiece_or_setup = random.choice([True, False])
            need_outer = True if (choice_mode == "내 맘대로 조건 선택 🎛️" and user_val1 >= 3) or (choice_mode == "완전 랜덤 🎲" and random.choice([1,2,3,4,5]) >= 3) else False
            coordi = {}
            
            if gender == "여성":
                if choice_mode == "내 맘대로 조건 선택 🎛️":
                    if is_onepiece_or_setup:
                        coordi['원피스'], _ = get_best_choice(f_onepiece_list, user_val1, user_val2, [], 'weather', 'formality')
                    else:
                        coordi['상의'], _ = get_best_choice(f_top_list, user_val1, user_val2, [], 'weather', 'formality')
                        coordi['하의'], _ = get_best_choice(f_bottom_list, user_val1, user_val2, [], 'weather', 'formality')
                    if need_outer:
                        coordi['겉옷'], _ = get_best_choice(f_outer_list, user_val1, user_val2, [], 'weather', 'formality')
                else:
                    if is_onepiece_or_setup: coordi['원피스'] = random.choice(f_onepiece_list)
                    else:
                        coordi['상의'] = random.choice(f_top_list)
                        coordi['하의'] = random.choice(f_bottom_list)
                    if need_outer: coordi['겉옷'] = random.choice(f_outer_list)
            else: 
                if choice_mode == "내 맘대로 조건 선택 🎛️":
                    if is_onepiece_or_setup:
                        coordi['수트/셋업'], _ = get_best_choice(m_setup_list, user_val1, user_val2, [], 'weather', 'formality')
                    else:
                        coordi['상의'], _ = get_best_choice(m_top_list, user_val1, user_val2, [], 'weather', 'formality')
                        coordi['하의'], _ = get_best_choice(m_bottom_list, user_val1, user_val2, [], 'weather', 'formality')
                    if need_outer:
                        coordi['겉옷'], _ = get_best_choice(m_outer_list, user_val1, user_val2, [], 'weather', 'formality')
                else:
                    if is_onepiece_or_setup: coordi['수트/셋업'] = random.choice(m_setup_list)
                    else:
                        coordi['상의'] = random.choice(m_top_list)
                        coordi['하의'] = random.choice(m_bottom_list)
                    if need_outer: coordi['겉옷'] = random.choice(m_outer_list)
            
            st.session_state.candidates_text = "💡 (참고) 날씨와 상황에 맞춘 최적의 AI 코디입니다!" if choice_mode == "내 맘대로 조건 선택 🎛️" else "🎲 완전 랜덤으로 뽑은 코디 결과입니다."
            st.session_state.results[menu] = coordi

        # ── 3. 나머지 공통 로직 (음식, 영상, 음악 등) ──
        else:
            if not current_list:
                st.error("조건이 너무 깐깐합니다! 카테고리를 더 고르거나 조건을 완화해주세요.")
                st.stop()

            if choice_mode == "내 맘대로 조건 선택 🎛️":
                final_result, candidates = get_best_choice(current_list, user_val1, user_val2, exclude_keywords, key1, key2, user_val3, key3)
                
                if not final_result:
                    st.error("조건이 너무 깐깐합니다! 카테고리를 더 고르거나 조건을 완화해주세요.")
                    st.stop()

                st.session_state.results[menu] = final_result 
                c_names = [c['name'] for c in candidates]
                st.session_state.candidates_text = f"💡 (참고) 최종 후보에 올랐던 것들: {', '.join(c_names)}"
            else:
                st.session_state.results[menu] = random.choice(current_list)
                st.session_state.candidates_text = "🎲 완전 랜덤으로 뽑은 결과입니다."

        st.session_state.show_balloons = True
        st.rerun()
            

    if st.session_state.results[menu] is not None:
        if menu == '오늘 뭐 입지? 👕':
            st.success("🎉 선택 천재의 추천 코디 세트가 완성되었습니다!")
            for k, v in st.session_state.results[menu].items():
                st.write(f"**{k}:** {v['name']} ({v['style']})")
        elif menu == '오늘 우리 뭐 하지? 👫':
            item = st.session_state.results[menu]
            st.success(f"🎉 선택 천재의 추천: **{item['name']}**")
            st.write(f"- 모임 유형: {item['_meeting_type_choice']} | 교통수단: {item['_transport_choice']}")
            st.write(f"- 어색함 지수: {item['awkwardness']}/5 | 인파 지수: {item['crowd']}/5 | 활동 지수: {item['energy']}/5")
            st.caption(f"💬 {item['note']}")
        else:
            st.success(f"🎉 선택 천재의 추천: **{st.session_state.results[menu]['name']}**")
        st.info(st.session_state.candidates_text)
        
        if st.session_state.show_balloons:
            st.balloons()          
            show_seasonal_effect() 
            st.session_state.show_balloons = False 

if any(value is not None for value in st.session_state.results.values()):
    st.write("---")
    st.markdown(f"### 🧾 {user_nickname}님의 완벽한 하루 영수증!")
    st.write("친구에게 공유해서 약속을 확정 지어보세요!")
    
    receipt_text = "========================================\n"
    receipt_text += f"            {user_nickname}님의 영수증        \n"
    receipt_text += "========================================\n\n"
    
    if st.session_state.results['오늘의 운세 🍀']:
        res = st.session_state.results['오늘의 운세 🍀']
        receipt_text += f"🍀 [오늘의 운세]\n"
        receipt_text += f" - 별점: {res['stars']}\n"
        receipt_text += f" - 한줄평: {res['text']}\n"
        receipt_text += f" - 행운템: {res['item']}\n"
        receipt_text += "----------------------------------------\n"
        
    for m in ['오늘 뭐 입지? 👕', '오늘 뭐 먹지? 🍽️', '오늘 뭐 마시지? ☕', '오늘 뭐 보지? 🎬', '오늘 우리 뭐 하지? 👫', '오늘 혼자 뭐 하지? 🏃', '오늘 뭐 듣지? 🎧']:
        item = st.session_state.results[m]
        if item is not None: 
            receipt_text += f"📍 [{m.split(' ')[-2]}]\n" 
            if m == '오늘 뭐 입지? 👕':
                for part, piece in item.items():
                    receipt_text += f" - {part} : {piece['name']} ({piece['style']})\n"
            elif m == '오늘 뭐 듣지? 🎧':
                receipt_text += f" - 추천 음악 : {item['name']}\n"
                receipt_text += f" - 에너지 지수 : {item['energy']} / 5 단계\n"
                receipt_text += f" - 집중도 지수 : {item['focus']} / 5 단계\n"
            elif m == '오늘 뭐 마시지? ☕':
                receipt_text += f" - 추천 음료 : {item['name']}\n"
                receipt_text += f" - 카페인 지수 : {item['caffeine']} / 5 단계\n"
                receipt_text += f" - 당 충전 지수 : {item['sweetness']} / 5 단계\n"
            elif m == '오늘 뭐 보지? 🎬':
                receipt_text += f" - 추천 영상 : {item['name']}\n"
                receipt_text += f" - 영상 길이 : {item['duration']} / 5 단계\n"
                receipt_text += f" - 몰입도 지수: {item['immersion']} / 5 단계\n"
            elif m == '오늘 혼자 뭐 하지? 🏃':
                receipt_text += f" - 추천 활동 : {item['name']}\n"
                receipt_text += f" - 인파 지수 : {item['crowd']} / 5 단계\n"
                receipt_text += f" - 활동 지수 : {item['energy']} / 5 단계\n"
                receipt_text += f" - 혼놀 레벨 : {item['solo_level']} / 5 단계\n"
            elif m == '오늘 우리 뭐 하지? 👫':
                receipt_text += f" - 추천 활동 : {item['name']}\n"
                receipt_text += f" - 모임 유형 : {item['_meeting_type_choice']}\n"
                receipt_text += f" - 교통수단 : {item['_transport_choice']}\n"
                receipt_text += f" - 어색함 지수: {item['awkwardness']} / 5 단계\n"
                receipt_text += f" - 인파 지수 : {item['crowd']} / 5 단계\n"
                receipt_text += f" - 활동 지수 : {item['energy']} / 5 단계\n"
                receipt_text += f" - 특징 : {item['note']}\n"
            else:
                receipt_text += f" - 추천 메뉴 : {item['name']}\n"
                receipt_text += f" - 소비 예산 : {item['budget']} / 5 단계\n"
                receipt_text += f" - 소모 에너지: {item['laziness']} / 5 단계\n"
            receipt_text += "----------------------------------------\n"
            
    receipt_text += "\n   이 영수증을 캡처해서 약속을 확정하세요!\n"
    receipt_text += "========================================"

    st.code(receipt_text, language="text")
    st.info("📸 **위 영수증 화면을 캡처**하거나, 영수증 오른쪽 위에 있는 **복사 아이콘(📋)**을 눌러 하루 전체 일정을 카톡으로 보내보세요!")