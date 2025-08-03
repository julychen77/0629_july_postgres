

import psycopg2

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
    stations = get_query()
    print("所有台鐵車站資訊的站點名稱：", stations)
if __name__ == "__main__":
    main()

