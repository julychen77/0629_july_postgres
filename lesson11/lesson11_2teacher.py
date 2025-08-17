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

st.subheader("2023年"+ station + "站進出站人數顯示")

date_range = get_date_range()
if date_range is None:
    st.error("無法取得日期範圍，請稍後再試。")
    st.stop()

# 轉換為 datetime.date（如果 datasource 回傳字串）
try:
    min_date, max_date = date_range
    if isinstance(min_date, str):
        min_date = datetime.date.fromisoformat(min_date)
    if isinstance(max_date, str):
        max_date = datetime.date.fromisoformat(max_date)
except Exception as e:
    st.error(f"無法解析日期範圍: {e}")
    st.stop()

# 在 sidebar 顯示只限於此範圍的日期選擇器（選擇範圍）
selected_dates = st.sidebar.date_input(
    "選擇日期範圍",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# 如果使用者只選單一日期，將其視為起訖相同
if isinstance(selected_dates, tuple) and len(selected_dates) == 2:
    start_date, end_date = selected_dates
else:
    start_date = end_date = selected_dates

# st.write("您選擇的車站:", station)
st.write("日期範圍:", start_date, "至", end_date)


