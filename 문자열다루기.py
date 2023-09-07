a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
# a[1] = "L" # 문자열의 요소는 읽을 수는있지만 변경은 되지 않음. 리터럴 상수

# 대소문자 바꾸기
aa = "Hello Python Program..."
print(aa.upper())
print(aa)
aa = aa.upper()
print(aa)

# 문자열 변경 : replace("")
input_str = "Hello Python Program..."
new_str = input_str.replace("Python", "JavaScript")
print(new_str)

# 문자열에 포함된 문자 갯수 세기, 길이 확인
input_str2 = "Hello Python Program..."
print(input_str2.count("lo")) # 문자열에서 포함된 문자의 갯수를 반환
print(len(input_str2)) # 문자열의 길이를 반환. 별도의 외부 함수를 사용하는 방식
test = [1,2,3,4,5,6,7,8,9,10]
print(f"길이 {len(test)}")
print(input_str2.__len__())

# 문자열 찾기 : find(), rfind(), index()
# find() : 찾은 문자열의 첫번째 인덱스를 반환, 못찾으면 -1
# index() : 찾은 문자열의 첫번째 인덱스를 반환, 못찾으면 ValueError
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장")) # 찾는 건 뒤에서부터 찾지만 인덱스 번호는 앞부터
print(phrase.index("포기"))

print(phrase.find("나에게"))
new_phrase = phrase.replace("가장","나에게")
print(new_phrase)

# 문자열 연산
print("태양고" + "")
#print("태양고" + 2) # 문자열과 정수의 연산 불가능
print("안녕하세요"*3) # 문자열을 숫자만큼 반복
print("안녕하세요", "!"*5 ,"\n","\t","="*3,"태양고","="*3,"\n나희도"*3,"입니다.")

# 문자열 앞/뒤 공백 제거 : strip()
input_a = """안녕하세요.
문자열 함수를 알아봅니다."""
print(input_a.strip())