import pyautogui as pag
import time

if __name__ == '__main__':
    #메모장 실행
    pag.moveTo(190, 1030, 2)
    pag.click()
    pag.press("hangul")
    pag.typewrite("apah")
    pag.press("hangul")
    pag.moveTo(260, 310, 2)
    pag.click(interval=0.5)
    pag.click()
    pag.typewrite("hello world")
    # 두번 내리자
    pag.press("enter")
    pag.press("enter")
    # 반갑구나 세상아 치자
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")
    pag.press("hangul")
    # 저장하자
    pag.hotkey('ctrl', 's')
    time.sleep(1)
    # pag.moveTo(30, 50, 2)
    # pag.click()
    # pag.moveTo(90, 150, 2)
    # pag.click()
    # 파일이름 : 파이썬월드
    pag.press("hangul")
    pag.typewrite("C:\\Users\\김선옥\\OneDrive\\바탕 화면\\")
    pag.typewrite("vkdlTjs dnjfem")
    pag.press("hangul")
    pag.moveTo(740, 630, 2)
    # pag.click()