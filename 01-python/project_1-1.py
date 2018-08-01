import random

# 1) 리스트를 만든다.
korean_food = ("김치찌개", "비빔밥", "국수")
chinese_food = ("짜장면", "탕수육", "짬뽕")
japanese_food = ("라멘", "돈까스", "돈부리")

# 2) 사용자로부터 입력
user_choice = input("한식, 중식, 일식 중 한 가지를 고르세요(맛집추천) : ")

# 3) 임의로 추천


if user_choice == "한식":
    choice_result = random.choice(korean_food)
elif user_choice == "중식":
    choice_result = random.choice(chinese_food)
elif user_choice == "일식":
    choice_result = random.choice(japanese_food)
else:
    print("한식, 중식, 일식 중에서 선택하셔야 됩니다.")

if choice_result:
    print("{} 중에서 {}가 선택 되었습니다.".format(user_choice, choice_result))
