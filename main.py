import streamlit as st
import pandas as pd

# 페이지 기본 설정
st.set_page_config(
    page_title="지역 맞춤형 재생에너지 추천 시스템",
    page_icon="🌱",
    layout="centered"
)

# 타이틀 및 동기 설명
st.title("🌱 지역별 맞춤형 재생에너지 추천 솔루션")
st.caption("기후위기 극복을 위한 지속가능한 에너지전환 탐구 프로젝트 (개발자: 박서진)")

st.markdown("""
> **탐구 배경:** 재생에너지의 단순한 양적 확대는 발전의 불안정성과 지역적 한계를 동반합니다. 
> 본 프로그램은 지역별 일사량, 풍속 등 기후 특성을 분석하여 **가장 효율적인 재생에너지원**을 추천합니다.
""")

st.divider()

# 간단한 지역별 기후 데이터 예시 (실제 공공데이터 API나 CSV로 확장 가능)
region_data = {
    "제주특별자치도": {"일사량": "높음", "평균풍속": "7.5m/s (매우 높음)", "해안인접": True, "추천": "풍력 (해상풍력) 및 태양광"},
    "강원특별자치도 (대관령 등)": {"일사량": "보통", "평균풍속": "6.8m/s (높음)", "해안인접": False, "추천": "육상풍력 및 소수력"},
    "전라남도 (신안/목포 등)": {"일사량": "매우 높음", "평균풍속": "6.0m/s (높음)", "해안인접": True, "추천": "태양광 및 조류/해상풍력"},
    "경상북도 (안동/의성 등)": {"일사량": "높음", "평균풍속": "3.5m/s (보통)", "해안인접": False, "추천": "태양광 및 바이오매스"},
    "서울특별시 / 수도권": {"일사량": "보통", "평균풍속": "2.8m/s (낮음)", "해안인접": False, "추천": "건물일체형 태양광(BIPV) 및 연료전지"}
}

# 사용자 입력 받기
selected_region = st.selectbox(
    "🔍 탐구하고 싶은 지역을 선택하세요:",
    list(region_data.keys())
)

# 결과 출력
if selected_region:
    info = region_data[selected_region]
    
    st.subheader(f"📍 {selected_region} 분석 결과")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="☀️ 평균 일사량 수준", value=info["일사량"])
    with col2:
        st.metric(label="💨 평균 풍속 수준", value=info["평균풍속"])
        
    st.success(f"💡 **최적 추천 재생에너지:** {info['추천']}")
    
    # 상세 제언 (발표문 정리부 내용 연계)
    st.markdown("---")
    st.markdown("### 🛠️ 지속가능한 에너지전환을 위한 제언")
    st.info(f"""
    1. **지역 맞춤형 발전:** {selected_region}의 기후 특성에 맞춰 발전 효율성을 극대화해야 합니다.
    2. **전력망 및 ESS 구축:** 날씨에 따른 발전량 변동성에 대비해 **에너지저장장치(ESS)** 확충과 타 지역과의 **전력망 연계**가 필수적입니다.
    """)

# 하단 정보
st.markdown("---")
st.caption("참고 문헌: 《기후 블랙홀》(박상욱 저) | 데이터: 기상청/전력통계정보시스템 참조 예시")
