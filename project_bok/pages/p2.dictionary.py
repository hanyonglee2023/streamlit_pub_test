import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="page2",page_icon=":smiley:")

plt.rcParams['font.family'] = 'gulim'
st.title('극성 사전')
neg_dic = pd.read_csv("/streamlit_pub_test/data/neg_dic_total.csv")
pos_dic = pd.read_csv("/streamlit_pub_test/data/pos_dic_total.csv")
neg_sent = pd.read_csv("/streamlit_pub_test/data/do_ngram_minsent.csv")
pos_sent = pd.read_csv("/streamlit_pub_test/data/hw_ngram_minsent.csv")
#----------------------------------------------------------------------------
neg_10 = neg_dic.sort_values('Down', ascending=False).head(10)
neg_10['neg_dic'] = neg_10['neg_dic'].apply(lambda x: x.split('/')[0])
# 막대 그래프 생성
n_fig, n_ax = plt.subplots()
n_bars = n_ax.bar(neg_10['neg_dic'], neg_10['Down'],color = 'orange')
for n_bar in n_bars:
    yval = n_bar.get_height()
    n_ax.text(n_bar.get_x() + n_bar.get_width()/2, yval + 0.05, round(yval, 2), ha='center', va='bottom')
st.header('🕊️ Dovish 사전')
dic, n_bar = st.columns(2)
dic.dataframe(neg_dic)
n_bar.pyplot(n_fig)
st.subheader('🕊️ n-gram이 포함된 의사록 문장')
n_options = neg_dic['neg_dic'].unique()
select_option = st.selectbox('값을 선택하세요:', n_options)
neg_sent = neg_sent.drop('Unnamed: 0',axis=1)
filtered_ndf = neg_sent[neg_sent['Dovish'] == select_option]
st.dataframe(filtered_ndf)
#----------------------------------------------------------------------------
pos_10 = pos_dic.sort_values('Up', ascending=False).head(10)
pos_10['pos_dic'] = pos_10['pos_dic'].apply(lambda x: x.split('/')[0])
# 막대 그래프 생성
h_fig, h_ax = plt.subplots()
h_bars = h_ax.bar(pos_10['pos_dic'], pos_10['Up'],color = 'blue')
for h_bar in h_bars:
    yval = h_bar.get_height()
    h_ax.text(h_bar.get_x() + h_bar.get_width()/2, yval + 0.05, round(yval, 2), ha='center', va='bottom')
st.header('🦅 Hawkish 사전')
dic, h_bar = st.columns(2)
dic.dataframe(pos_dic)
h_bar.pyplot(h_fig)
st.subheader('🦅 n-gram이 포함된 의사록 문장')
p_options = pos_dic['pos_dic'].unique()
select_option = st.selectbox('값을 선택하세요:', p_options)
pos_sent = pos_sent.drop('Unnamed: 0',axis=1)
filtered_pdf = pos_sent[pos_sent['Hawkish'] == select_option]
st.dataframe(filtered_pdf)