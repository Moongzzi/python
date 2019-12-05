import pyautogui as pag

if __name__ == '__main__':
    pag.moveTo(43, 432, duration=2)     #-> 목적지
    #pag.click()
    #pag.click()            -> 1번 방법
    #pag.click(clicks=2)    -> 2번 방법
    pag.doubleClick()
    pag.move(100, 200, duration=1)      #-> 상대 좌표 이동
    pag.rightClick()
    pag.click(button="right")
    pag.drag(0, 200, duration=2)