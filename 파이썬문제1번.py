# 1. 정해진 형식으로 시간을 입력받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분 05초
# 2. 3개의 정수를 입력받아 최대값과 최소값 구하기
# 3. 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
# 4. 갯수가 정해지지 않은 여러개의 정수를 입력 받아 합계와 평균 구하기

# 1
# hour, min, sec = map(int, input("시:분:초 입력하세요 : ").split(":"))
# if hour > 12 :
#     hour -= 12
#     print(f"오후 {hour:02}시 {min:02}분 {sec:02}초")
# else :
#     print(f"오전 {hour:02}시 {min:02}분 {sec:02}초")

# 2
# a, b, c = map(int, input("정수 3개를 입력하세요 : ").split(" "))
# if a > b :
#     if a > c : print(a)
#     else : print(c)
# else :
#     if b > c : print(b)
#     else : print(c)

# 3
num = input("주민등록번호를 입력하세요 : ")
print(type(num))
front = num[:6]
gender = num[7:8]
age = int(num[:2])
if gender == 1 or gender == 3:
    gender = "남자"
else:
    gender = "여자"
if age <= 23:
    age = 23 - age + 1
else:
    age = 123 - age + 1
print(f"""생년월일 : {front}
성별 : {gender}
나이 : {age}""")

# 4
# score = list(map(int, input("여러개의 정수를 입력 : ").split(" ")))
# print(f"총점 : {sum(score)}")
# print(f"평균 : {sum(score)/len(score)}")