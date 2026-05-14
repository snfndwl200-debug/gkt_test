import streamlit as st
import random
import time

# --- 1. 원형 룰렛 디자인 생성 함수 (HTML/CSS) ---
def generate_roulette_html(items):
    n = len(items)
    if n == 0: return ""
    
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC', '#99CCFF', '#E2F0CB', '#FFB7B2', '#C7CEEA', '#B5EAD7']
    
    conic_parts = []
    for i in range(n):
        start = i * (360 / n)
        end = (i + 1) * (360 / n)
        color = colors[i % len(colors)]
        conic_parts.append(f"{color} {start}deg {end}deg")
    conic_str = ", ".join(conic_parts)
    
    labels_html = ""
    for i, item in enumerate(items):
        angle = i * (360 / n) + (360 / n) / 2
        short_item = item[:5] 
        labels_html += f"""
        <div style="position: absolute; left: 50%; top: 0; height: 150px; width: 40px; 
                    transform-origin: bottom center; transform: translateX(-50%) rotate({angle}deg); 
                    display: flex; justify-content: center; align-items: flex-start; padding-top: 15px; 
                    font-weight: bold; font-size: 15px; color: #333; text-shadow: 1px 1px 2px white; z-index: 2;">
            <span style="writing-mode: vertical-rl; text-orientation: upright;">{short_item}</span>
        </div>
        """
        
    html = f"""
    <style>
    @keyframes spinWheel {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(1800deg); }} 
    }}
    .wheel-wrapper {{ position: relative; width: 320px; height: 320px; margin: 20px auto; }}
    .roulette-wheel {{
        width: 300px; height: 300px; border-radius: 50%; border: 8px solid #FFD700;
        background: conic-gradient({conic_str});
        position: absolute; top: 10px; left: 10px; overflow: hidden;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        animation: spinWheel 2.5s cubic-bezier(0.2, 0.8, 0.3, 1) forwards;
    }}
    .pointer {{
        position: absolute; top: -5px; left: 50%; transform: translateX(-50%);
        width: 0; height: 0; 
        border-left: 20px solid transparent; 
        border-right: 20px solid transparent; 
        border-top: 35px solid #FF4136; 
        z-index: 10;
        filter: drop-shadow(0 4px 2px rgba(0,0,0,0.3));
    }}
    .center-dot {{
        position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
        width: 30px; height: 30px; background: #333; border-radius: 50%; z-index: 5;
        border: 4px solid #FFD700;
    }}
    </style>
    <div class="wheel-wrapper">
        <div class="pointer"></div>
        <div class="roulette-wheel">
            {labels_html}
            <div class="center-dot"></div>
        </div>
    </div>
    """
    return html

# --- 2. 초기 데이터 설정 ---
if 'menus' not in st.session_state:
    st.session_state.menus = {
        '한식': ['제육볶음', '김치찌개', '된장찌개', '비빔밥', '불고기', '국밥'],
        '중식': ['짜장면', '짬뽕', '탕수육', '마라탕', '볶음밥'],
        '일식': ['초밥', '돈가스', '우동', '라멘', '규동'],
        '양식': ['파스타', '피자', '수제버거', '스테이크', '리조또'],
        '분식': ['떡볶이', '김밥', '라면', '순대', '튀김']
    }

if 'roulette_winners' not in st.session_state:
    st.session_state.roulette_winners = []

st.set_page_config(page_title="점심 복불복 사다리", layout="wide")
st.title("🍽️ 점심 복불복! 한 명은 굶는다! 😱")

# --- 3. 사이드바: 친구 이름 및 메뉴 셋팅 ---
st.sidebar.header("👥 참가자 명단")
friends_input = st.sidebar.text_input("친구들의 이름을 쉼표(,)로 구분해서 적어주세요", "은형, 민희, 지연")
# 빈칸 제거 및 리스트화
friends_list = [f.strip() for f in friends_input.split(",") if f.strip()]
num_friends = len(friends_list)

st.sidebar.info(f"현재 참가자: {num_friends}명\n\n룰렛으로 {max(0, num_friends - 1)}개의 메뉴를 뽑습니다.")

st.sidebar.header("⚙️ 메뉴 셋팅")

with st.sidebar.form(key="add_menu_form", clear_on_submit=True):
    st.subheader("새로운 메뉴 추가")
    new_cat = st.selectbox("카테고리", list(st.session_state.menus.keys()))
    new_food = st.text_input("메뉴 이름 입력")
    submit_btn = st.form_submit_button("추가하기")
    
    if submit_btn and new_food:
        if new_food not in st.session_state.menus[new_cat]:
            st.session_state.menus[new_cat].append(new_food)
            st.rerun()

selected_total_menus = []
st.sidebar.subheader("룰렛 후보 선택")

for cat, foods in st.session_state.menus.items():
    with st.sidebar.expander(f"{cat} (현재 {len(foods)}개)"):
        selected = st.multiselect(f"{cat} 선택", options=foods, default=foods, key=f"ms_{cat}")
        selected_total_menus.extend(selected)

# --- 4. 메인 화면 1단계: 원형 룰렛 ---
st.write("---")
st.header(f"1단계: 원형 룰렛으로 메뉴 {max(0, num_friends - 1)}개 뽑기 🎯")

wheel_placeholder = st.empty()
result_placeholder = st.empty()

if st.button("원형 룰렛 돌리기!", key="roulette_btn"):
    if num_friends < 2:
        st.error("참가자가 최소 2명 이상이어야 사다리 게임이 가능합니다!")
    elif len(selected_total_menus) < (num_friends - 1):
        st.warning(f"메뉴를 최소 {num_friends - 1}개 이상 선택해주세요!")
    else:
        wheel_placeholder.markdown(generate_roulette_html(selected_total_menus), unsafe_allow_html=True)
        result_placeholder.info("룰렛이 힘차게 돌아갑니다... 🎲")
        
        time.sleep(2.5)
        
        # (인원수 - 1) 개의 메뉴 추출
        st.session_state.roulette_winners = random.sample(selected_total_menus, num_friends - 1)
        
        cands_html = "".join([f"<div style='padding: 10px 20px; background: #4A90E2; color: white; border-radius: 30px; font-size: 18px; font-weight: bold; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);'>{c}</div>" for c in st.session_state.roulette_winners])
        
        res_html = f"""
        <div style='text-align: center; margin-top: 10px; padding: 20px; background: #F8F9FA; border-radius: 15px;'>
            <h2 style='color: #E24A4A; margin-bottom: 20px;'>🎉 {num_friends - 1}개 메뉴 확정! 🎉</h2>
            <div style='display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;'>
                {cands_html}
            </div>
        </div>
        """
        result_placeholder.markdown(res_html, unsafe_allow_html=True)

# --- 5. 메인 화면 2단계: 사다리 게임 ---
st.write("---")
st.header("2단계: 운명의 사다리 게임 🪜 (한 명은 굶어!)")

if st.session_state.roulette_winners:
    if st.button("사다리 타기 시작!", key="ladder_btn"):
        ladder_placeholder = st.empty()
        
        # 메뉴 리스트에 '굶어!' 추가
        final_items = st.session_state.roulette_winners.copy()
        final_items.append("❌ 굶어!")
        
        # 리스트 무작위 섞기 (사다리 결과 배정)
        random.shuffle(final_items)
        
        # 사다리 타는 애니메이션 효과
        ladder_placeholder.info("사다리를 타고 내려가는 중입니다... 🏃💨 다들 긴장하세요!")
        time.sleep(2)
        
        # 결과 화면 구성 (친구별로 하나씩 공개)
        ladder_placeholder.empty()
        cols = st.columns(num_friends)
        
        for idx, (friend, item) in enumerate(zip(friends_list, final_items)):
            with cols[idx]:
                st.markdown(f"<h3 style='text-align: center;'>{friend}</h3>", unsafe_allow_html=True)
                st.markdown("<div style='text-align: center; font-size: 40px;'>⬇️</div>", unsafe_allow_html=True)
                
                # 순차적으로 공개하는 쫄깃한 효과
                time.sleep(1) 
                
                if "굶어!" in item:
                    st.error(f"**{item}**")
                    st.toast(f"앗! {friend}님 당첨... 😱")
                else:
                    st.success(f"**{item}**")
                    
        st.balloons()
        st.markdown("<h2 style='text-align: center; margin-top: 30px; color: #2E86C1;'>결과 발표 끝! 식사하러(또는 굶으러) 가시죠! 🏃‍♂️</h2>", unsafe_allow_html=True)
else:
    st.info("먼저 위에서 룰렛을 돌려 메뉴를 확정해 주세요.")