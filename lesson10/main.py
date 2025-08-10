import datasource

def main():
    results = datasource.get_query()
    if results:
        for queryA in results:
            print(queryA)
    else:
        print("無法取得車站資料")

if __name__ == "__main__":
    main()