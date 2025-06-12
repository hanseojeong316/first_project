import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="🖐️✊✌️ 가위바위보 게임 🎉",
    page_icon="✂️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 스타일 커스텀 (컬러풀 배경과 글씨)
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        color: #4b0082;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 0 20px #ff8c00;
    }
    .title {
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px #ffb347;
    }
    .subtitle {
        font-size: 1.5rem;
        margin-bottom: 30px;
        color: #ff4500;
        font-weight: bold;
    }
    .result {
        font-size: 2rem;
        margin: 20px 0;
        font-weight: 700;
        color: #008000;
        text-shadow: 1px 1px 2px #006400;
    }
    .choice-button {
        font-size: 2rem;
        padding: 15px 25px;
        margin: 10px;
        border-radius: 15px;
        border: none;
        cursor: pointer;
        background: linear-gradient(45deg, #ff6a00, #ee0979);
        color: white;
        box-shadow: 0 0 10px #ff6a00;
        transition: transform 0.2s ease-in-out;
    }
    .choice-button:hover {
        transform: scale(1.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 타이틀
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">🖐️✊✌️ 가위바위보 게임 🎉</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 선택을 눌러주세요! 🤩</div>', unsafe_allow_html=True)

# 가위바위보 이모지와 매핑
choices = {
    "✊ (주먹)": "rock",
    "✌️ (가위)": "scissors",
    "🖐️ (보)": "paper"
}
emoji_map = {"rock": "✊", "paper": "🖐️", "scissors": "✌️"}

# 사용자 선택 받기 (버튼으로)
user_choice_text = None
cols = st.columns(3)
for idx, (text, val) in enumerate(choices.items()):
    if cols[idx].button(text, key=val):
        user_choice_text = text

if user_choice_text is not None:
    user_choice = choices[user_choice_text]
    comp_choice = random.choice(list(choices.values()))

    # 승부 결정
    if user_choice == comp_choice:
        result = "무승부! 😮‍💨"
        color = "#FFA500"
    elif (
        (user_choice == "rock" and comp_choice == "scissors") or
        (user_choice == "scissors" and comp_choice == "paper") or
        (user_choice == "paper" and comp_choice == "rock")
    ):
        result = "당신이 이겼어요! 🎉🎊"
        color = "#00CC00"
    else:
        result = "컴퓨터가 이겼어요! 💻🔥"
        color = "#FF0000"

    # 결과 출력
    st.markdown(f'<div class="result" style="color:{color};">')
    st.markdown(f'👤 당신: {emoji_map[user_choice]} VS 💻 컴퓨터: {emoji_map[comp_choice]}')
    st.markdown(f'<br><strong>{result}</strong>')
    st.markdown('</div>')

st.markdown("</div>", unsafe_allow_html=True)
