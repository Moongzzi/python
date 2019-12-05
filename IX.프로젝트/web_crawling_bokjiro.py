from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "https://www.bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do"
    data = {"searchIntClId":"03", "pageUnit":"200"}
    with requests.post(url, data) as response:
        soup = BeautifulSoup(response.text, "lxml")
    print(soup)
    titles = soup.select("dt.tit > a")
    for title in titles:
        print(title.text)