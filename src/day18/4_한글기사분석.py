#day18 > 4_한글기사분석.py
#주제 : 다음 경제 뉴스의 최신 10페이지 기사들 제목의 단어 빈도수 분석
#https://news.daum.net/breakingnews/economic?page=1
import re
import urllib.request

from bs4 import BeautifulSoup

#1. 데이터 준비
textData = []
for page in range(1,11) :
    url = f'https://news.daum.net/breakingnews/economic?page={page}'
    response = urllib.request.urlopen(url)
    htmlData = response.read()
    soup = BeautifulSoup(htmlData,"html.parser")
    list_news2 = soup.select_one('.list_news2') #특정 클래스 파싱
    for li in list_news2('li') :
        title = li.select_one('.tit_thumb > a').string
        # print(title)
        textData.append(title)
# print(textData)

#2. 품사 태깅
    #1. 정규표현식
messages = ''
for msg in textData :
    messages += re.sub(r'[^\w]', ' ', msg)
    #2. 태깅
from konlpy.tag import Okt
okt = Okt()
words = okt.nouns(messages)
# print(words)
#3. 분석(빈도수)
    #1. 빈도수 체크
from collections import Counter
wordsCount = Counter(words)
# print(wordsCount)
    #2. 상위 N개 추출
bestWords = wordsCount.most_common(30)
# print(bestWords)
    #3. 딕셔너리 변환
wordDict = {}
for word , count in bestWords :
    if len(word) > 1 :
        wordDict[word] = count
#4. 시각화(히스토그램, 워드클라우드)
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wc = WordCloud("c:/windows/fonts/malgun.ttf", background_color='ivory').generate_from_frequencies(wordDict)

plt.imshow(wc)
plt.show()