# 각 사이트 비밀번호 만들기
# 규칙1 : http:// 잘라내기
# 규칙2 : 처음 만나는 점 이후 제거
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'o'의 갯수 + 글자에 포함된 'k' 갯수+ '!' + 자신의이니셜(예: 'jks')

file_name = "password1.txt"
f = open(file_name, "wt") #t는 텍스트 모드이며 기본 값
while True:
    url = input("사이트 : ")
    if url == "exit": break
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")] # 슬라이싱, 처음부터 . 위치 미만까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("o")) + "!" + "jks"
    print("비밀번호 : " + password)# 각 사이트 비밀번호 자동으로 만들기
    f.write(password + "\n")
f.close()
