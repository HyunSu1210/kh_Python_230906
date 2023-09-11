# 계좌 개설
def open_account(name):
    print(f"{name}님의 계좌가 개설되었습니다.")
    return name # 반환 값으로 이름을 전달

# 입금 함수
def deposit(balance, input): # 잔고와 입금액을 매개변수로 전달
    print(f"{input}이 입금되었습니다. 잔액은 {balance+input}입니다.")
    return balance + input

# 출금 함수
def withdraw(balance, output):
    if balance >= output:
        print(f"{output}이 출금되었습니다. 잔액은 {balance - output}입니다.")
        return balance-output
    else:
        print(f"출금을 실패하였습니다. 잔액은 {balance}입니다.")

balance = 0 # 외부에서 선언했지만 매개변수로 전달하여 결과를 리턴 받음
name = open_account("곰돌이사육사")
balance = deposit(balance,1000)
balance = withdraw(balance,500)
print(f"{name}의 잔액은 {balance}입니다.")

