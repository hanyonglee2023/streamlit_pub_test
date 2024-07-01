import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

st.set_page_config(page_title="page1",page_icon=":smiley:")
st.title("Chart")

# 데이터 불러오기
data = pd.read_csv("streamlit_pub_test/data/doc_tone_base_rate.csv")

# 데이터 프레임 변환
df = pd.DataFrame(data)

# 라인차트
# df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
test = plt.figure(figsize=(10,7))

ax1 = df.doc_tone.plot(color='blue', grid=True, label='doc_tone')
ax2 = df.baserate.plot(color='red', grid=True, secondary_y=True, label='base_rate')

# 왼쪽 y축 범위 설정
ax1.set_ylim(-1, 0)

# # x 축 날짜 형식 설정
# date_format = DateFormatter('%y-%m')
# ax1.xaxis.set_major_formatter(date_format)

# 범례 합치기
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper right')

# ax = plt.gca()
# ax.xaxis.set_major_locator(dates.MonthLocator())

# # x 축 레이블 설정
# plt.xlabel('date')

# # x 축 날짜 형식 설정
# date_format = DateFormatter('%y-%m')  # 여기서 '%y-%m-%d'는 원하는 날짜 형식으로 변경할 수 있습니다.
# ax1.xaxis.set_major_formatter(mdates.date_format)

# 그래프 출력
st.pyplot(test)

# col1, col2 = st.columns(2)

# 산점도
graph1 = plt.figure(figsize=(10,7))
plt.rc("font", family = "gulim", size = 12)
# plt.rcParams["axes.unicode_minus"] = False
sns.regplot(x = "doc_tone", y = "baserate", data = df)
plt.xlabel("어조")
plt.ylabel("기준금리")
plt.title("의사록 어조에 따른 기준금리 분포")
st.pyplot(graph1)


# 데이터 프레임 출력(정렬 기능 제공)
st.dataframe(df, use_container_width = True)






