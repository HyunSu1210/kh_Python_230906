# C : 테스트 케이스의 개수
# N : 각 테스트 케이스마다 학생의 수 (1 ≤ N ≤ 1000, N은 정수)가 첫 수로 주어짐
# 이어서 N명의 점수가 주어짐(0 <= score <= 100, 정수)
# 입력하는 부분을 함수로 구현, C 입력, N 입력, score 입력 후 평균 구하기.
# for 문으로 평균과 score 비교해서 평균 넘는 학생의 비율 구한 후 출력.
# 리스트[N, [score1, score2 ...]] 중첩 리스트?

# 리스트를 마지막에 돌리도록
# c를 먼저 입력 받고 for문으로 c의 개수만큼 함수 호출


c = int(input("테스트 케이스의 개수 : "))

def average(c):
    for i in c : # c의 개수만큼
