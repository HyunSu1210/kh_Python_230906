# 저항
# 처음 색 2개 : 저항의 값
# 마지막 색 : 곱해야 하는 값
color = ["black","brown","red","orange","yellow","greed","blue","violet","grey","white"]
first = color.index(input())
second = color.index(input())
third = color.index(input())
print(int(str(first) + str(second)) * (10**third))