# ** 제곱?
# 피타고라스 정리

rst = []  # 결과를 출력하기 위한 리스트
while True:
    li = list(map(int, input().split()))
    li.sort()
    if li[0] == 0 and li[1] == 0 and li[2] == 0:
        break
    elif li[2] ** 2 == li[1] ** 2 + li[0] ** 2:
        rst.append("right")
    else:
        rst.append("wrong")

for e in rst: print(e)
