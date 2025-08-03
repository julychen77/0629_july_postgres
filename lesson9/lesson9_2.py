import argparse
import random

def get_user_name()->str:
    """
    取得使用者姓名。

    此函式會先嘗試從命令列參數取得使用者姓名（-n 或 --name），
    若未提供則會提示使用者輸入姓名。回傳取得的姓名字串。

    回傳:
        str: 使用者的姓名
    """
    parser = argparse.ArgumentParser(description="猜數字遊戲")
    parser.add_argument("-n","--name",type=str,help="姓名")
    parser.add_argument("-f","--frequency",type=int,help="玩的次數",default=1)
    args = parser.parse_args()

    if not args.name:
        name = input("請輸入您的姓名:")
    else:
        name = args.name

    return name

def play_game(name:str)->None:
    """
    猜數字遊戲函式。

    參數:
        name (str): 玩家名稱。

    功能說明:
        此函式會隨機產生一個1到100之間的整數作為目標數字，玩家需在指定範圍內猜數字。
        每次猜測後，會提示玩家猜大了還是猜小了，並根據猜測調整範圍。
        當玩家猜中目標數字時，顯示猜對訊息及總猜測次數，遊戲結束。
    """
    i = 0
    print(f"========猜數字遊戲第{i+1}次=========\n\n")
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(target)
    while(True):
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"{name}共猜了{count}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!再小一點")
                max = keyin - 1
            else:
                print(f"猜錯了!再大一點")
                min = keyin + 1
            print(f"{name}已經猜{count}次\n")
        else:
            print("請輸入提示範圍內的數字\n")

def main():
    frequency = 1
    name = get_user_name()
    for i in range(frequency):
        play_game(name)
    print(f"遊戲結束,{name}共玩了{frequency}次")

if __name__ == '__main__':
    main()