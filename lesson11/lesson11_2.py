import streamlit as st
import pandas as pd
import datasource

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
#sidebar要先顯示常用的車站名稱
#使用者可以很快的選擇
#如果不常用的車站名稱,再使用selectbox

common_stations = [
    "臺北", "桃園", "臺中", "新竹", "彰化", "高雄", "花蓮","其他"
]

choice = st.sidebar.radio("快速選擇常用車站", common_stations)

if choice == "其他":
    station = st.sidebar.selectbox(
        "請選擇車站",
        stations,
    )
else:
    station = choice

st.subheader("2023年進出站人數顯示")
st.write("你選擇的車站:",station)


