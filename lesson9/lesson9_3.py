

import psycopg2

#一個function，傳入connection參數，建立一個cursor，
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

#一個function，連線至postgres DB，建立連線環境參數的樣版
def create_connection():
    conn = psycopg2.connect(
        host="host.docker.internal",
        database="postgres",
        user="postgres",
        password="raspberry",
        port="5432"
    )
    return conn


def main():
    conn = create_connection()
    if conn:
        print("成功連接到資料庫！")
#執行SQL查詢，回傳查詢結果
        query = """
        SELECT count(*) AS "筆數"
        FROM "台鐵車站資訊";
        """
        result = execute_query(conn, query)
        print("台鐵車站資訊：", result)

        conn.close()
    else:
        print("無法連接到資料庫，請檢查設定！")
        return

if __name__ == "__main__":
    main()

