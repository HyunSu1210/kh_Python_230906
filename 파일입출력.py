# 파일쓰기 : 파일을 읽거나 쓰기 위해서는 반드시 open() 해야 함
# 파일객체 : open(파일명, 파일모드, 인코딩)
# 파일명 : 파일경로 + 파일명 (파일경로를 입력하지 않으면 현재위치에 저장)
# 파일모드 : r(읽기), w(쓰기), a(추가, 파일이 없으면 생성하고 추가, 있으면 파일의 마지막에 추가)

# 파일 쓰기
# score_file = open("score.txt", "w", encoding='utf-8')
# print("수학 : 50", file=score_file)
# print("영어 : 90", file=score_file)
# score_file.write("국어 : 98" + "\n") # end나 sep 없음
# score_file.write("과학 : 45" + "\n")
# score_file.close()

# 파일 읽기
# read() : 파일 내의 모든 내용을 읽어 하나의 문자열로 반환
# readline() : 해당 파일의 내용을 한 라인씩 읽어 들여 문자열로 반환하며, 파일의 끝(EOF)에 도달하여 더 이상 가져올 라인이 없을 경우에는 None을 반환
# readlines() : 각각의 라인을 하나의 요소로 저장하는 하나의 리스트를 반환

# score_file = open("score.txt", "r", encoding='utf-8')
# print(score_file.read())
# score_file.close()

# while True:
#     line = score_file.readline() # 한줄씩 문자열로 반환
#     if not line: # 라인이 거짓 => None, False 등등이면 (더 이상 읽을 라인이 없으면)
#         break
#     print(line, end="") # 한줄씩 읽어서 출력하기 때문에 줄바꿈 문자가 포함되어 있음
# score_file.close()

# lines = score_file.readlines()
# for e in lines:
#     print(e, end="")
# score_file.close()
#
# # with 키워드 : open() 이후에 자동으로 close()를 호출해주는 기능
# with open("score.txt" ,"r",encoding='utf-8') as score_file:
#     print(score_file.read())
#
# print("프로그램 끝")

import pickle

# 객체를 직렬화하여 파일에 저장하기
# data = {'name': 'Alice', 'age': 30, 'city': 'Ney York'}
# with open('data.pickle', 'wb') as file:
#     pickle.dump(data, file)

with open('data.pickle','rb') as file :
    restored_data = pickle.load(file)

print(restored_data)
