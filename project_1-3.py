import random

ROCK = "바위"
SCISSORS = "가위"
PAPER = "보"
RSP_LIST = (ROCK, SCISSORS, PAPER)

win_count = 0
lose_count = 0

while win_count<3 and lose_count < 3:
    # 1) 사용자 입력
    user_choice = input("{}, {}, {}: ".format(SCISSORS, ROCK, PAPER))
    # 2) 컴퓨터 임의 선택
    computer_choice = random.choice(RSP_LIST)
    # 3) 3번 지거나 이기면 승패 확정
    if user_choice == computer_choice:
        print("비겼습니다.")
    elif user_choice not in RSP_LIST:
        print("가위, 바위, 보 중에서 하나를 입력해주세요.")
    elif ((user_choice == ROCK and computer_choice == SCISSORS)
        or(user_choice == SCISSORS and computer_choice == PAPER)
        or(user_choice == PAPER and computer_choice == ROCK)):
        win_count += 1
        print("이겼습니다.")
    else:
        lose_count += 1
        print("졌습니다.")

if win_count == 3:
    print("사용자가 {} : {}으로 최종 승리하였습니다.".format(win_count, lose_count))
else:
    print("컴퓨터가 {} : {}으로 최종 승리하였습니다.".format(lose_count, win_count))
