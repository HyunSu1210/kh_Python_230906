# 1 : 세자리 정수를 입력 받은 후 가장 큰 수 찾기 (123 => 3)

# 2 : 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 근무 : 9620원
# 야간근무 : 주간 시급 * 1.5
# - 주간근무 [1], 야간근무[2]를 입력 하세요 :
# - 근무 시간을 입력해 주세요 :
# - 입력한 시간 동안 근무한 주간 또는 야간 급여는 ___원 입니다

# 3 : 문자열 추가하기
# 2개의 문자열을 포인터 변수 s와 k에 입력받기
# 양의 정수를 정수형 변수 n에 각각 전달받아 s 문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성

# 1.
# num = int(input("세자리 정수 입력 : "))
# a = num // 100 # 백의 자리
# b = num % 100 // 10 # 십의 자리
# c = num % 10 # 일의 자리
# if a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# else: # a < b
#     if(b > c):
#         print(b)
#     else: # b < c
#         print(c)

# 2.
# day_night = int(input("주간근무 [1] 야간근무 [2] 입력하세요 : "))
# time = int(input("근무 시간을 입력해주세요 : "))
# if day_night == 1:
#     print(f"{time}시간동안 근무한 주간 또는 야간 급여는 {time*9620}원 입니다.")
# elif day_night == 2:
#     print(f"{time}시간동안 근무한 주간 또는 야간 급여는 {int(time*9620*1.5)}원 입니다.")
# else:
#     print("잘못 입력하셨습니다.")

# 3.
s = input("s 문자열을 입력하세요 : ")
k = input("k 문자열을 입력하세요 : ")
n = int(input("잘라낼 문자열의 길이를 입력하세요 : "))
print(s[-n:] + k)