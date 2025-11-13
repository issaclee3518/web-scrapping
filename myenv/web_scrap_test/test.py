import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/section/100"
response = requests.get(url)
if response.status_code == 200:
    bs = BeautifulSoup(response.text, "html.parser")
    print(bs.get_text())
else:
    print("Failed to fetch the page")

news_title = bs.find_all('strong', class_="sa_text_strong")

for idx, title in enumerate(news_title):
    print(idx, title.get_text())

search_keyword = "장동혁"
keyword_news_list = []

for keyword_news in news_title:
    if search_keyword in keyword_news.get_text():
        keyword_news_list.append(keyword_news.get_text())
print("--------------------------------")
print(f"{search_keyword} 관련 뉴스 제목:")
for idx, keyword_news in enumerate(keyword_news_list):
    print(idx+1, keyword_news)