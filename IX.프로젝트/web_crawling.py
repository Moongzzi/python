#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    data = urlopen(https://page.kakao.com/home?seriesId=53297664)
    soup = BeautifulSoup(data, "lxml")
    print(soup)
    cartoon_titles = soup.find_all("td", attrs = {"class":"title"})
    for cartoon_title in cartoon_titles:
        title = cartoon_title.find("a").text
        print(title)