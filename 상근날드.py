# 상근날드
# 햄버거와 음료 세트로 구매하면 가격의 합계에서 50원을 뺀 가격이 세트메뉴의 가격이 됨
# 햄버거는 상덕버거, 중덕버거, 하덕버거
# 음료는 콜라, 사이다
# 햄버거와 음료의 가격이 주어졌을 때, 가장 싼 세트 메뉴의 가격을 출력하는 프로그램을 작성

menu = []
for i in range(5):
    menu.append(int(input()))
min_burger = min(menu[:3])
min_cola = min(menu[3:])
print(min_cola + min_burger - 50)