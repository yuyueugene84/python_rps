from random import randint

def num_to_gesture(num):
    if num == 1:
        return "剪刀"
    elif num == 2:
        return "石頭"
    elif num == 3:
        return "布"

if __name__ == "__main__":
    print("-------歡迎來到剪刀石頭布！-------")

    name = input("請輸入您的名稱：")

    while True:
        while True:
            user_hand = input("請出拳 (1) 剪刀 (2) 石頭 (3) 布：")
            # 若玩家輸入的内容是數字，而且是 1, 2, 3 的其中一個
            if user_hand.isdigit() and (user_hand in ["1", "2", "3"]):
                # 跳出 loop
                user_hand = int(user_hand)
                break
            else:
                print("請輸入合法的選項！")

        comp_hand = randint(1,3)

        print("==================================================================")
        print(f"{name} 出了: {num_to_gesture(user_hand)}, '電腦出了: {num_to_gesture(comp_hand)}")
        print("==================================================================")

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
        # 詢問玩家是否再玩一次
        keep_play = input("想要再玩一次嗎？ Y) 是 N) 否")

        if keep_play.upper() == "N" and keep_play.upper() in ["Y", "N"]:
            break

print("感謝你玩剪刀石頭布！")