# 내장함수 : 파이썬이 기본적으로 제공, import가 필요없음

# 큰 값 작은 값 찾기
# print(max(1,2,3,4,5,65,99,77,100))
# print(min(1,2,3,4,5,65,99,77,100))
#
# # 총합 구하기
# print(sum([1,2,3,4,5,65,99,77,100])) # 리스트에 대한 총합
# print(sum((1,2,3,4,5,65,99,77,100))) # 튜플 대한 총합
# num = list(map(int, input("정수값 입력 : ").split()))
# print(f"입력받은 수의 총합 : {sum(num)}")
# print(f"입력받은 수의 평균 : {sum(num)/len(num)}")

# 몫과 나머지 구하기
# print(f"몫과 나머지 구하기 : {divmod(10, 4)}") # 자바와는 다르게 두개의 반환값이 나옴, 튜플의 동작 원리

# 여러개의 값을 한번에 입력받아 리스트로 만들기
# 최대값, 최소값, 합계, 평균, 몫과 나머지
# num = list(map(int,input("여러 개의 값 입력 : ").split())) # 리스트로 입력받기
# print(f"최대값 : {max(num)}")
# print(f"최소값 : {min(num)}")
# print(f"합계 : {sum(num)}")
# print(f"평균 : {sum(num)/len(num)}")
# print(f"몫과나머지 : {divmod(sum(num),5)}")

# 오름차순 정렬
# my_list = [1,2,3,4,45,56,87,98,45,100]
# print(sorted(my_list,reverse=True))
# print(sorted(my_list))