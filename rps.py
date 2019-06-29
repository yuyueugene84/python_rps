from random import randint

# 將數字轉成相對應的字串
def num_to_gesture(num):
    if num == 1:
        return "剪刀"
    elif num == 2:
        return "石頭"
    elif num == 3:
        return "布"

# 主程式從這邊開始執行
if __name__ == "__main__":
    print("-------歡迎來到剪刀石頭布！-------")

    name = input("請輸入您的名稱：")

    user_hand = int(input("請出拳 (1) 剪刀 (2) 石頭 (3) 布："))

    # 電腦出拳
    comp_hand = randint(1,3)

    print("==================================================================")
    print(f"{name} 出了: {num_to_gesture(user_hand)}, '電腦出了: {num_to_gesture(comp_hand)}")
    print("==================================================================")

    # 判斷玩家是贏還是輸
    if user_hand == comp_hand:
        print('平手!')
    elif user_hand == 1 and comp_hand == 3:
        print('你贏了!')
    elif user_hand == 2 and comp_hand == 1:
        print('你贏了!')
    elif user_hand == 3 and comp_hand == 2:
        print('你贏了!')
    else:
        print('你輸了!')

    print("感謝你玩剪刀石頭布！")