from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "https://www.bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do"
    data = {"searchIntClId":"03", "pageUnit":"100"}
    with requests.post(url, data) as response:
        soup = BeautifulSoup(response.text, "lxml")
    print(soup)
    titles = soup.select("a > dit.tit > a")