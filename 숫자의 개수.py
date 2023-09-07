while 1:
    a = int(input("A : "))
    if 100 <= a <= 1000: break
    print("다시입력하세요.")
while 1:
    b = int(input("B : "))
    if 100 <= b <= 1000: break
    print("다시입력하세요.")
while 1:
    c = int(input("C : "))
    if 100 <= a <= 1000: break
    print("다시입력하세요.")
mul = str(a*b*c)
print(type(mul))
for i in range(len(mul)):
    print(mul.count(str(i)))


