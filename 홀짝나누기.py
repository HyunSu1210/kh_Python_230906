# 무작위 수를 공백으로 기준하여 입력받아 홀수와 짝수로 리스트에 나누어 담아 출력하는 문제
# num = list(map(int, input("무작위 수 입력 : ").split()))
# a_list = []
# b_list = []
# for e in num :
#    if e % 2 == 0: a_list.append(e)
#    else: b_list.append(e)
# print(f"홀수 : {a_list}")
# print(f"짝수 : {b_list}")

#람다식 버전
num = list(map(int, input("무작위 수 입력 : ").split()))
odd = list(filter(lambda e:e % 2 == 1, num))
even = list(filter(lambda e:e % 2 == 0, num))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")
