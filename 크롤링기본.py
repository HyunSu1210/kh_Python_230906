import requests # 서버로부터 정보를 요청해서 가져옴, get 방식으로 가져올 예정
from bs4 import BeautifulSoup
# url = "https://www.weather.go.kr/weather/observation/currentweather.jsp"
# html = requests.get(url).text
# soup = BeautifulSoup(html, "html.parser")
# print(soup)

# 날씨 정보 가져오기
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

# HTTP GET 요청
response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

for loc in soup.select("location"):
    print("도시 : ",loc.select_one("city").string)
    print("날씨 : ",loc.select_one("wf").string)
    print("최저기온 : ",loc.select_one("tmn").string)
    print("최고기온 : ",loc.select_one("tmx").string)
    print("-"*20)