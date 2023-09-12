# 손익분기점
# A : 고정 비용 (노트북 갯수와 상관없음)
# B : 가변 비용 (노트북 갯수만큼 곱해야 함)
# C : 노트북 가격
# 총 수입 > 총 비용(=고정비용+가변비용) -> 손익분기점
# 총 수입(노트북갯수*노트북가격), 총 비용(고정비용 + (가변비용*노트북갯수))

fix, var, sell = map(int, input().split())
cnt = 0
if sell <= var: print(-1)
else: print(fix // (sell - var) + 1)

# while True:
#     if cnt > fix // (sell - val): break
#     cnt += 1
# print(cnt)