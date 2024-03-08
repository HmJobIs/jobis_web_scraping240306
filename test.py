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

#select() 다가져오는거 selext(one)은 검색된 하나를 가져오는것

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
soup = BeautifulSoup(html, 'html.parser')

# find_all
menu_item_text = soup.find_all('a', class_='menu-item-text')

for el in menu_item_text:
  print(el.get('text'))