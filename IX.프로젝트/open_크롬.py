import pyautogui as pag
import time

if __name__ == '__main__':
    #크롬 이미지 인식하자
    data = pag.locateAllOnScreen("크롬 아이콘.PNG")
    print(data)
    #가운데 좌표 찾자
    # center = (data.left + (data.width/2), data.top + (data.height/2))
    center = pag.center(data)
    #마우스 이동
    pag.moveTo(center, duration=2)
    #더블 클릭
    pag.doubleClick(center, duration=2)