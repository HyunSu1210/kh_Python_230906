name = input("이름 : ")
while 1 :
    age = int(input("나이 : "))
    if 0 < age < 200: break
    print("나이를 잘못입력했습니다.")
while 1 :
    gender = input("성별 : ")
    if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f': break
    print("성별을 잘못입력했습니다.")
while 1 :
    jobs = int(input("직업 : [1]학생 [2]회사원 [3]주부 [4]무직 : "))
    if 0 < jobs < 5: break
    print("직업을 잘못입력했습니다.")

# if jobs == 1:
#     jobs = str("학생")
# elif jobs == 2:
#     jobs = str("회사원")
# elif jobs == 3:
#     jobs == str("주부")
# elif jobs == 4:
#     jobs == str("무직")

jobs_name = ("", "학생","회사원","주부","무직")

print(f"""이름 : {name}
나이 : {age}
성별 : {gender}
직업 : {jobs_name[jobs]}""")