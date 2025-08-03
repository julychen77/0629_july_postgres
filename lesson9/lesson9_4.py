

import psycopg2

#一個function，傳入connection參數，建立一個cursor，執行query
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

def get_query():
    conn = create_connection()
    cursor = conn.cursor()

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

# 老師的語法
import psycopg2


def create_connection():
    conn = psycopg2.connect(
        host="host.docker.internal",
        database="postgres",
        user="postgres",
        password="raspberry",
        port="5432"
    )
    return conn

#建立一個function,功能是取得所有台鐵車站資訊的站點名稱
def get_all_stations():
    """
    取得所有台鐵車站的名稱。

    此函式會連接至資料庫，查詢「台鐵車站資訊」資料表中的所有車站名稱，並以列表形式回傳查詢結果。

    回傳值:
        list: 包含所有車站名稱的查詢結果，每個元素為一個元組(tuple)。
    """
    conn = create_connection()
    cursor = conn.cursor()
    query = """
    SELECT "name"
    FROM "台鐵車站資訊";
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def main():
    stations = get_all_stations()
    print("所有台鐵車站資訊的站點名稱：", stations)


if __name__ == "__main__":
    main()