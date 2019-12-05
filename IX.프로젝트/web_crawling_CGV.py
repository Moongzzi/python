#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '_main_':
    #씨지비 > 현재 상영작 제목 가져오기
    data = urlopen("http://www.cgv.co.kr/movies/")
    soup = BeautifulSoup(data, "lxml") #httpResponse -> HTML
    data.close()
    # print(soup)
    html = "<html><head><meta charset='uft-8'></head><body>"
    cartoon_titles = soup.find_all("strong",attrs={"class":"title"}) #<td class = "title">...</td>
    for cartoon_title in cartoon_titles:                          #cartoon_titles[:2]
        title = cartoon_title.find("a").text                      #<a href>text</a>
        link = cartoon_title.find("a").get("href")               #텍스트 가져오기
        link = "http://www.cgv.co.kr/" + link
        print(title)
        # print(link)
        html+= "<a href = '{}'>{}</a><br />".format(link, title)       #<a href = 'link'>title</a>
    html+= "</body></html>"
    # print(html)
    outputSoup = BeautifulSoup(html, "lxml")
    prettyHtml = str(outputSoup.prettify())
    with open("CGV.html", "w", encoding = "utf-8") as f:
        f.write(prettyHtml)