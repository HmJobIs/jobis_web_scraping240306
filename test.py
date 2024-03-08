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
      <a href="https://www.naver.com">네이버로 이동</a>
    </li>
    <li>
      <a href="https://www.naver.com">다음으로 이동</a>
    </li>
  </ul>
</nav> 
'''
# BeautifulSoup을 사용하여 HTML을 파싱합니다.
soup = BeautifulSoup(html, 'html.parser')
#select() 다가져오는거 selext(one)은 검색된 하나를 가져오는것
a_tags = soup.select('a')
a_tag = soup.select_one('a')
print(a_tag)

#for tags in a_tags:
#  print(tags.get_text())
