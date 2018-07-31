import random

korea = ["반기다", "한식좋아", "만남류"]
china = ["선혜향", "즐겨찾기", "중화맛"]
japan = ["헬로우스시", "해피초밥", "서다우"]

a = input("한식, 중식, 일식 중 한 가지를 고르세요(맛집추천) : ")

if a == "한식":
    print(random.choice(korea))
elif a == "중식":
    print(random.choice(china))
elif a == "일식":
    print(random.choice(japan))
else:
    print("값을 잘못 입력하셨습니다.")
