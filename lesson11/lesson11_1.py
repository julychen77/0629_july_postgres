import streamlit as st
import pandas as pd
import datasource

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

st.sidebar.title("台鐵車站")
st.title("台鐵車站資訊")
st.subheader("2023年進出站人數顯示")

@st.cache_resource
def get_querys():
    """取得車站資料"""
    return datasource.get_query()

stations= get_querys()
if stations is None:
    st.error("check")
    st.stop()
    
station = st.sidebar.selectbox(
    "請選擇車站",
    stations,
)

st.write("你選擇的車站:",station)


