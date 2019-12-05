#pip install beautifulsoup4
#pip install lxml

from urllib.request import urlopen
import json

if __name__ == '__main__':
    #다음웹툰 > 취향저격 그녀
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite") as data:
        j = json.loads(data.read())      #httpResponse -> json
    #print(j["data"]["webtoon"]["webtoonEpisodes"][3]["title"])
    cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]
    for cartoon_title in cartoon_titles:
        title = cartoon_title["title"]
        print(title)
