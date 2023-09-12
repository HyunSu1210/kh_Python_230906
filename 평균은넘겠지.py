# C : 테스트 케이스의 개수
# N : 각 테스트 케이스마다 학생의 수 (1 ≤ N ≤ 1000, N은 정수)가 첫 수로 주어짐
# 이어서 N명의 점수가 주어짐(0 <= score <= 100, 정수)
# 입력하는 부분을 함수로 구현, C 입력, N 입력, score 입력 후 평균 구하기.
# for 문으로 평균과 score 비교해서 평균 넘는 학생의 비율 구한 후 출력.
# 리스트[N, [score1, score2 ...]] 중첩 리스트?

# 리스트를 마지막에 돌리도록
# c를 먼저 입력 받고 for문으로 c의 개수만큼 함수 호출
#:.3f -> 소숫점 나타내기

def over_rate():
    ls = list(map(int, input().split()))  # 공백 기준으로 입력 받아서 정수형 리스트로 저장
    average = sum(ls[1:]) / len(ls[1:])  # 리스트에서 맨 앞의 요소는 인원수이므로 제외, 총합 / 인원수 = 평균
    cnt = 0  # 평균이 넘는 %를 구하기 위해서는 인원에 카운트가 필요
    for i in range(1, len(ls)):  # 맨 앞의 요소는 인원수이므로 제외
        if ls[i] > average: cnt += 1
    return cnt / (len(ls) - 1) * 100 # 백분율로 변경

n = int(input()) # 총 테스트 횟수
rst = [] # 각 테스트 케이스에 대한 결과 값을 받기 위한 리스트
for i in range(n) : # 총 테스트 횟수만큼 반복 수행
    rst.append(over_rate())

for e in rst:
    print(f"{e:.3f}")