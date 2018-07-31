# 리스트와 튜플에 있는 수 중 임의의 값 하나 뽑기.

import random
list_1 = [1, 2, 3, 4 ,5]
tuple_1 = (1, 2, 3, 4, 5)
random_list = random.choice(list_1)
random_tuple = random.choice(tuple_1)
print(random_list)
print(random_tuple)

# 두 수 사이에 랜덤 값 뽑기.
random_value = random.randint(1, 100)
print(random_value)
