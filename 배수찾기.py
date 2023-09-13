# 정수 n과 수의 목록이 주어졌을 때, 목록에 들어있는 수가 n의 배수인지 아닌지를 구하는 프로그램
# 0 < n < 1000
# 0 < 목록 < 10000, 목록의 마지막은 0으로 끝남


# n = int(input("n : ")) # 정수 n 입력
# if 0 < n < 1000:
#     num_list = map(int, input("list : ").split()) # 목록 입력받기
#      # if num_list == 0: # 0이면
#     for i in num_list: # num_list의 값 i로 순회
#         if i % n == 0: print(f"{i} is a multiple of {n}")
#         else: print(f"{i} is NOT a multiple of {n}")
# else : print("범위를 초과하였습니다.")

n = int(input()) # 정수 n 입력
num_list = [] # 빈 리스트 생성

while True:
    x = int(input())
    if x == 0: break
    num_list.append(x)

for i in num_list: # num_list의 값 i로 순회
     if i % n == 0: print(f"{i} is a multiple of {n}")
     else: print(f"{i} is NOT a multiple of {n}")
