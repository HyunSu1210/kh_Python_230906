# 산술 연산자 : 사칙연산자(+, -, *, /) //몫, **(제곱연산자), %(나머지 연산자)
i = 10 # 값을 대입할 때 데이터 형이 결정됨, 왜냐면 파이썬은 데이터형이 없음
j = 3
print(f"덧셈 : {i+j}")
print(f"뺄셈 : {i-j}")
print(f"곱셈 : {i*j}")
print(f"나눗셈 : {i/j}")
print(f"몫 : {i//j}")
print(f"나머지 : {i%j}")
print(f"제곱연산 : {i**j}")
test = "Python"
print(test + " Hello")
print(test + str(100))
print(test * 3) # test 문자열을 3번 반복하겠다는 의미
i += 1 # 파이썬은 증감 연산자가 없음
print(f"증감연산자 시험 {i}")

# 간단 예제
# tax_rate = 0.10
# income = int(input("당신은 수업이 얼마입니까?"))
# print(f"당신이 내야 할 세금은 {income * tax_rate:.2f}입니다.")

# 관계 연산자 : AND(&&) => and, OR(||) => or, NOT(!) => not
x = 10
y = 20
z = 30
rst1 = x > 0 and x > y # false
rst2 = x > 0 or x > y # True
rst3 = not(x > 0 or x > y) #False
print(rst1,rst2,rst3, sep="\t")

# 다항(3항)연산자
num = int(input("정수 입력 : "))
rst = (num % 2 == 0) and "짝수" or "홀수"
print(f"{num}은 {rst}입니다.")

# 2진수 입력 받기 (0b)
number = 0b1010101
# 8진수 입력 받기 (0o)
number = 0o1234567
# 16진수 입력 받기 (0x) (0123456789ABCDEF)
number = 0xffffff