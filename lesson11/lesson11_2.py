import streamlit as st
import pandas as pd
import datasource

st.sidebar.title("台鐵車站")
st.title("台鐵車站資訊")
# st.subheader("2023年進出站人數顯示")

@st.cache_data
def get_querys():
    """取得車站資料"""
    return datasource.get_stations()

@st.cache_data
def get_date_range():
    """取得日期範圍"""
    return datasource.get_min_and_max_date()

stations= get_querys()
if stations is None:
    st.error("check")
    st.stop()
#sidebar要先顯示common stations名稱，再使用selectbox
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
# 取得可選日期範圍，並在 sidebar 顯示只能在此範圍內的日期區間選擇器
    date_window = get_date_range()
    if date_window is None:
        st.error("無法取得日期範圍，請稍後再試。")
        st.stop()

    try:
        min_date = pd.to_datetime(date_window[0]).date()
        max_date = pd.to_datetime(date_window[1]).date()
    except Exception:
        st.error("日期格式錯誤，請聯絡管理員。")
        st.stop()

    selected_range = st.sidebar.date_input(
        "請選擇日期區間",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    if isinstance(selected_range, tuple) and len(selected_range) == 2:
        start_date, end_date = selected_range
    else:
        start_date = end_date = selected_range

st.subheader("2023年"+ station + "站進出站人數顯示")
date_range = get_date_range()
if date_range is None:
    st.error("無法取得日期範圍，請稍後再試。")
    st.stop()

try:
    st.write("您選擇的日期區間：", start_date.strftime("%Y-%m-%d"), "至", end_date.strftime("%Y-%m-%d"))
except Exception:
    st.write("尚未選擇或無法解析日期區間")
st.write("日期範圍:", min_date, "至", max_date)


