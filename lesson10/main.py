import datasource
import streamlit as st

def main():
    st.title("台鐵車站名稱列表")
    results = datasource.get_query()
    if results:
        st.dataframe(results,width=400,height=600)
    else:
        print("無法取得車站資料")

if __name__ == "__main__":
    main()


# import datasource

# def main():
#     results = datasource.get_query()
#     if results:
#         for queryA in results:
#             print(queryA)
#     else:
#         print("無法取得車站資料")

# if __name__ == "__main__":
#     main()

#在終端機執行streamlit run main.py