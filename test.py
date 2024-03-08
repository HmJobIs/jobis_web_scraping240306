import requests
from bs4 import BeautifulSoup

# 웹페이지 URL
url = 'https://www.naver.com/'

# HTTP GET 요청을 보냅니다.
response = requests.get(url)

#<div></div> div 태그 열린태그, 닫는태그, 구성요소 ->엘리먼트 div 엘리먼트
html = '''
<nav class="menu-box-1" id= "menu-box">
  <ul>
    <li>
      <a class="menu-item-text" href="https://www.naver.com">네이버로 이동</a>
    </li>
    <li>
      <a class="menu-item-text" href="https://www.naver.com">다음으로 이동</a>
    </li>
  </ul>
</nav> 
'''

#select() 다가져오는거 selext(one)은 검색된 하나(첫번쨰)를 가져오는것 / 리스트반환

# 모든 일치하는 요소로 접근할 때 사용, 리스트 반환
#a_tags = soup.select('a')

# 첫 번째로 일치하는 단일 요소의 접근
#a_tag = soup.select_one('a')
#print(a_tag)

#해당 엘리먼트가 품고 있는 텍스트 추출
#for tags in a_tags:
#  print(tags.get_text())
  
#해당 엘리먼트가 가지고 있는 href 속성값을 출력
#for tags in a_tags:
#  print(tags.get('href'))

# BeautifulSoup을 사용하여 HTML을 파싱합니다.

# find_all / find 조건으로 검색 + (find)검색된 하나(첫번쨰)엘리먼트로 검색가능 / 리스트반환
# 해당 엘리먼트의 클래스 이름으로 접근 id를 적는경우에는 아디로 접근
#menu_item_text = soup.find_all('a', class_='menu-item-text')


#for el in menu_item_text:
#  print(el.get('text'))

# 네이버 뉴스 url
url = 'https://news.naver.com/section/101'

#지정 웹사이트의 웹 get요청을 보내서
#리퀘스트를 이용해서 웹페이지에 html 문서 내용 가져오기

response = requests.get(url)

# 웹 페이지의 html 내용을 뷰티폴숩프 객체로 변환
soup = BeautifulSoup(response.text, 'html.parser')

news_title = soup.find_all('a', class_= 'sa_text_title')
#print(news_title)

news_title_list = []
#for title in news_title:
#  print(title.get_text())
for title in news_title:
  news_title_list.append(title.get_text())

# 뉴스 제목 안에 있던 /n 제거하는 코드
cleanlist = [item.replace('\n', '') for item in news_title_list]
#print(cleanlist)
for idx, til in enumerate(cleanlist):
  print(f"{idx + 1} : {til}")
#  print(title.get_text())


