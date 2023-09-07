# 회원 가입을 위한 아이디와 패스워드 입력 받기
user = input("아이디 입력 : ")
if len(user) >= 10: # 입력 받은 아이디의 길이가 10이상이면,
    pw = input("비밀번호 입력 : ")
    # if pw.__len__() < 8 or pw.__len__() > 16:
    if len(pw) < 8 or len(pw) > 16:
        print("비밀번호는 8~16 사이어야 합니다.")
    elif pw.find(user) >= 0: # 포함되지 않으면 -1을 반환
        print("비밀번호에 아이디를 포함시킬 수 없습니다.")
    else:
        print("아이디 : {}".format(user))
        print("비밀번호 : {}".format(pw))
else:
    print("아이디는 반드시 10자리 이상이어야 합니다.")

