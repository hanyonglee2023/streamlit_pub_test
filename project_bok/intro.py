import streamlit as st

st.set_page_config(page_title="Hello",page_icon=":sunglasses:")

# 제목 설정
st.title("텍스트마이닝을 활용한 금리예측 프로젝트")
st.header("금융통화위원회 의사록 분석")
st.subheader("key point: 긍정 사전 / 부정 사전 만들기")
st.caption("eKoNLPy : 한국어를 지원하는 경제분석을 위한​ 자연어처리 라이브러리")

# 데이터 출력
st.markdown("의사록의 톤을 분석해서 **금리의 상승/하락**을 예측해봅시다.")

st.image("https://blog.fint.co.kr/app/uploads/2022/11/%EC%A7%80%EC%8B%9D%ED%95%80_%EB%A7%A4%ED%8C%8C%EC%A0%81_04-1-1024x666.jpg", width=800)
