# 제어문 : 조건문과 반복문을 의미하며 순차적인 흐름을 제어하는 목적으로 사용됨
# n = int(input("정수를 입력하세요 :"))
# if n > 100:
#     print(f"{n}은 100보다 커요")
# elif n < 100:
#     print(f"{n}은 100보다 작아요")
# else :
#     print("100과 같아요")

# 조건문에서 문자열 비교
while True:
    season = input("현재 계절을 입력하세요 : ")
    if season == "spring":
        print("봄이 왔어요.")
        break
    elif season == "summer":
        print("여름이 왔어요.")
        break
    elif season == "fall" or season == "autumn":
        print("쓸쓸한 가을입니다,")
        break
    elif season == "winter":
        print("아직 겨울이네요ㅜㅜ")
        break
    else:
        print("계절을 잘못 입력하셨습니다.")
