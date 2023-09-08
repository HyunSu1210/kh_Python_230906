# 외장함수 : 파이썬이 기본적으로 제공, improt가 필요함
# randint(0, 4) : 0 ~ 4까지의 임의의 정수값이 반환
# randrange(0, 4) : 0 ~ 4 미만의 정수값이 반환

import random

for i in range(100):
    rand = random.randint(0, 4)
    print(rand)

# 현재 시간 가져오기
import datetime

datetime.datetime.today()

from datetime import datetime  # 하나만 뽑아오겠다라는 의미

print(datetime.today())
print(datetime.today().year)
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

# 수학 계산을 위한 math
import math

print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.log(100))
print(math.ceil(100))
print(math.floor(100.9999))

# 로또 번호 자동 생성기
print("로또 번호 자동 생성기 ")
ls = []  # 빈 리스트 만들기
while True:
    rand = random.randrange(1, 46)
    if rand not in ls: # list에 생성된 rand 값이 포함되어 있지 않으면
        ls.append(rand)
    if len(ls) == 6: break
print(ls)
