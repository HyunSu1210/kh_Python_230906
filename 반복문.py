# 반복문 : 조건이 참인 동안 계속 수행되는 구문
# n = int(input("정수를 입력하세요 : "))
# sum = 0
# while n :
#     sum += n
#     n -= 1 # 파이썬은 증감연산자가 없음
# print(sum)
#
# while True :
#     age = int(input("나이를 입력하세요 : "))
#     if 0 < age < 200: break
#     else: print("나이 입력 범위를 벗어났습니다.")

# for 요소 in 시퀀스:
# fruits = ["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)

# 구구단 찍기
# for i in range(2,10) : # 2단~ 9단
#     for j in range(1,10):
#         print(f"{i} x {j} = {i*j}")
#     print()

# 홀/짝 나누어 찍기
# n = int(input("정수 입력 : "))
# for i in range(0,n):
#     for j in range(0,n):
#         if j % 2 == 0 : print("$", end=' ')
#         else : print("*", end=' ')
#     print()

# 사각형 찍기
# 정수 n을 입력받아 n * n 크기의 행렬을 출력하는 프로그램 작성
# 값은 1부터 시작
# n = int(input("정수 입력 : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print("*", end=' ')
#     print()
# ######################
# n = int(input("정수 입력 : "))
# for i in range(1, n * n + 1):
#     print(f"{i:>3}", end=" ")
#     if i % n == 0: print()

# 별찍기1
# n = int(input("↘ : "))
# for i in range (n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# 별찍기2
# n = int(input("↙ : "))
# for i in range (n):
#     for j in range(n-i):
#         print("*", end=' ')
#     print()

# 별찍기3
# n = int(input("▽ : "))
# for i in range (n):
#     for k in range(i):
#         print("", end=' ')
#     for j in range(n-i):
#         print("*", end=' ')
#     print()

# 별찍기4
# n = int(input("↘ : "))
# for i in range (n):
#     for k in range(i):
#         print(" ", end=' ')
#     for j in range(n-i):
#         print("*", end=' ')
#     print()

# 문자와 아스키코드
# chr : 유니코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
# ord : 문자를 유니코드 값으로 변환
# for i in range(ord("A"),ord("Z")+1):
#     print(chr(i), end=" ") # chr 문자 출력
# print()
#
# for i in range(65,91): #A:65 Z:90
#     print(chr(i), end=" ")
# print()