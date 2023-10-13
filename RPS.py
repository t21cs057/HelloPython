'''
Created on 2023/10/13

@author: t21cs057
'''
import random

def get_user_choice():
    while True:
        print("0. グー (Rock)")
        print("1. チョキ (Scissors)")
        print("2. パー (Paper)")
        user_choice = input("じゃんけんポン！ (0/1/2): ")
        if user_choice in ['0', '1', '2']:
            return int(user_choice)
        else:
            print("無効な選択です。もう一度選んでください。")

def get_computer_choice():
    return random.randint(0, 2)

def setUserPoint(x):
    userPoint = x
    return userPoint

def getUserPoint():
    return 

def setComputerPoint(x):
    computerPoint = x
    return computerPoint

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "引き分け"
    elif (user_choice == 0 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 0):
        return "あなたの勝ち"
    else:
        return "コンピューターの勝ち"
    
def give_point(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "引き分け"
    elif (user_choice == 0 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 0):   
        return "あなたの勝ち"
    else:
        return "コンピューターの勝ち"
#
#
# def three(user_choice, computer_choice):
#     userPoint = 0
#     computerPoint = 0
#
#     while True:
#         user_choice = get_user_choice()
#         computer_choice = get_computer_choice()
#
#         user_choice_name = {0: "グー", 1: "チョキ", 2: "パー"}
#         result = determine_winner(user_choice, computer_choice)
#
#         print("「" + f"あなた: {user_choice_name[user_choice]}" + " v.s " \
#               + f"コンピューター: {user_choice_name[computer_choice]}" + " → "\
#                + f"結果: {result}" + "」")
#
#         if result == "あなたの勝ち":
#             userPoint++
#         else if == "コンピューターの勝ち":
#             computerPoint += 1
#
#         print("あなた:" + userPoint + "点, コンピューター:" + computerPoint + "点")
#
#         if userPoint >= 3 or computerPoint >= 3
        

def main():
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        user_choice_name = {0: "グー", 1: "チョキ", 2: "パー"}
        result = determine_winner(user_choice, computer_choice)
        
        print("「" + f"あなた: {user_choice_name[user_choice]}" + " v.s " \
              + f"コンピューター: {user_choice_name[computer_choice]}" + " → "\
               + f"結果: {result}" + "」")
        
        # print("あなた:" + userPoint + "点")

        play_again = input("もう一度プレイしますか？ (はい/いいえ): ")
        if play_again.lower() != "はい":
            break

if __name__ == "__main__":
    main()
