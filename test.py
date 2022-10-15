import urllib.request as req
from bs4 import BeautifulSoup
import re

url = "https://news.naver.com/"

res = req.urlopen(url)
source = res.read()
source = source.decode("utf-8")

html = BeautifulSoup(source, 'html.parser')
print(html)

atags = html.select('p[class=cjs_dept_desc]')
print('a tag 수=' , len(atags))

crawling_data = []

cnt = 0
for atag in atags :
    cnt += 1
    atagLine = str(atag.string)
    for atagStrTemp in atagLine.split():
        atagStr = atagStrTemp
        for loop in range(3):
            atagStr = re.sub("\[(\w|[가-힣]|\ |\+|[一-龥]|\·|\"|\'|\?|\!|\`|\:)*\]", "", atagStr)
            atagStr = re.sub("\((\w|[가-힣]|\ |\+|[一-龥]|\·|\"|\'|\?|\!|\`|\:)*\)", "", atagStr)
            atagStr = re.sub("\<(\w|[가-힣]|\ |\+|[一-龥]|\·|\"|\'|\?|\!|\`|\:)*\>", "", atagStr)
            atagStr = atagStr.replace('?', '')
            atagStr = atagStr.replace('"', '')
            atagStr = atagStr.replace('\'', '')
            atagStr = atagStr.replace('<', '')
            atagStr = atagStr.replace('>', '')
            atagStr = atagStr.replace('”', '')
            atagStr = atagStr.replace('·', '')
            atagStr = atagStr.replace('…', '')
            atagStr = atagStr.replace('…', '')
            atagStr = atagStr.replace('...', '')
            atagStr = atagStr.replace('..', '')
            atagStr = atagStr.replace('‘’', '')
            atagStr = atagStr.replace('[', '')
            atagStr = atagStr.replace(']', '')
            atagStr = atagStr.replace('‥', '')
            atagStr = atagStr.replace('“', '')
            atagStr = atagStr.replace('‘', '')
            atagStr = atagStr.replace('’', '')
            atagStr = atagStr.strip()
            atagStr = atagStr.rstrip('는')
            atagStr = atagStr.rstrip('까')
            atagStr = atagStr.rstrip('있')
            atagStr = atagStr.rstrip('에서')
            atagStr = atagStr.rstrip('다')
            atagStr = atagStr.rstrip('요')
            atagStr = atagStr.rstrip('와')
            atagStr = atagStr.rstrip('은')
            atagStr = atagStr.rstrip('가')
            atagStr = atagStr.rstrip('니')
            atagStr = atagStr.rstrip('도')
            atagStr = atagStr.rstrip('에')
            atagStr = atagStr.rstrip('서')
            atagStr = atagStr.rstrip('겨')
            atagStr = atagStr.rstrip('을')
            atagStr = atagStr.rstrip('는')
            atagStr = atagStr.rstrip('서')
            atagStr = atagStr.rstrip('야')
            atagStr = atagStr.rstrip('면')
            atagStr = atagStr.rstrip('선')
            atagStr = atagStr.rstrip('는')
            atagStr = atagStr.rstrip('라')
            atagStr = atagStr.rstrip('다')
            atagStr = atagStr.rstrip('지')
            atagStr = atagStr.rstrip('에')
            atagStr = atagStr.rstrip('도')
            atagStr = atagStr.rstrip('요')
            atagStr = atagStr.rstrip('의')
            atagStr = atagStr.rstrip('은')
            atagStr = atagStr.rstrip('다')
            atagStr = atagStr.rstrip('만')
            atagStr = atagStr.rstrip('선')
            atagStr = atagStr.rstrip('인')
            atagStr = atagStr.rstrip('고')
            atagStr = atagStr.rstrip('가')
            atagStr = atagStr.rstrip('의')
            atagStr = atagStr.rstrip('을')
            atagStr = atagStr.rstrip('이')
            atagStr = atagStr.rstrip('는')
            atagStr = atagStr.rstrip('면')
            atagStr = atagStr.rstrip('요')
            atagStr = atagStr.rstrip('이')
            atagStr = atagStr.rstrip('라')
            atagStr = atagStr.rstrip('한')
            atagStr = atagStr.rstrip('에')
            atagStr = atagStr.rstrip('서')
            atagStr = atagStr.rstrip('의')
            atagStr = atagStr.rstrip('가')
            atagStr = atagStr.rstrip('다')
            atagStr = atagStr.rstrip('터')
            atagStr = atagStr.rstrip('은')
            atagStr = atagStr.rstrip('에')
            atagStr = atagStr.rstrip('이')
            atagStr = atagStr.rstrip('에서')
            atagStr = atagStr.rstrip('의')
        if len(atagStr) <= 1:
            continue
        crawling_data.append(atagStr)
    '''
    string.strip() : 문단 끝 불용어(공백, tab,\n\r) 제거
    '''
print("수집한 자료 확인")

words = list(set(crawling_data))
counts = []
for word in words:
    count_word = crawling_data.count(word)
    counts.append(count_word)

words_dict = dict(zip(words, counts))
print(words_dict)

from collections import Counter
counter = Counter(words_dict)
top10_word = counter.most_common(10)
words = []
counts = []

for word, count in top10_word :
    words.append(word)
    counts.append(count)

print(words)
print(counts)
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties (
fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

print('선그래프')
plt.plot(words, counts)
plt.show()

print('막대그래프')
plt.bar(words, counts)
plt.show()