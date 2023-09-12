# [1]예매하기 [2]종료하기
# 좌석번호 입력받아 예매하는 시스템 (좌석은 총 10개)
# 이미 예매가 완료된 좌석은 재구매할 수 없음
# 한 좌석당 예매 가겨은 12000원
# 종료 후, 총 매출액 출력

seat = [0] * 10
TICKET_PRICE = 12000 # 총 매출액
# 좌석 상태를 표시하는 메뉴 만들기
def print_seat():
    for e in seat : # 향상된 for 문으로 좌석의 갯수만큼 순회
        if e == 0 : print("[ ]", end=' ') # 판매 안 된 좌석
        else: print("[V]",end=' ')
    print()


# 총 매출액 구하기
def amount():
    cnt = 0
    for e in seat:
        if e == 1 : cnt += 1 # 팔린 좌석의 총 갯수 구하기
    return cnt * TICKET_PRICE

# 좌석 예약하기
def select_seat():
    print_seat() # 현재 예약 가능한 좌석 보여주기
    num = int(input("좌석 번호를 선택하세요 : ")) - 1 # 선택된 좌석번호는 1부터 시작, 인덱스에 맞춰주기 위해 -1
    if seat[num] == 0:
        seat[num] = 1
        print_seat()
    else: print("이미 예약된 좌석입니다.")

while True:
    sel = int(input("[1]예매하기 [2]종료하기 : "))
    if sel == 1: select_seat()
    else:
        print(f"총 매출액은 {amount()}입니다. 종료합니다.")
        break


# while True :
#     menu = int(input("[1]예매하기 [2]종료하기 : ")) # 메뉴 입력 받기
#     if menu == 1:
#         # 현재 좌석 보여주기
#         seat = int(input()) # 좌석 선택하기
#         if seat == 1:
#
#         else: print("이미 선택된 좌석입니다.")
#     elif menu == 2:
#         print(f"종료되었습니다. 총 매출액은 {sum}원 입니다.") break
#     else: print("메뉴를 잘못 입력하셨습니다.")