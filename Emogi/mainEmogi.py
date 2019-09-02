#2305 김선옥
#요즘 자주사용하는 키보드 이모지를 검색하고 찾아 쓸 수 있는 프로그램입니다.

class menu:
    _love = ["๑❤‿❤๑","(ɔ ˘⌣˘)˘⌣˘ c)","(ɔ ˘⌣˘)˘⌣˘ c)","（*´з)(ε｀*)","ლ(◞‿◟ლ)"]
    _angry = ["(оﾟдﾟо)","(╬☉д⊙)","(；◔д◔)","٩(๑`^´๑)۶","(ﾉﾟ⊿ﾟ)ﾉ"]
    _smile = ["ლ( ╹ ◡ ╹ ლ)","o(๑◕‿‿◕๑)o~♪","๑•‿•๑","٩(∗ ›ω‹ ∗)و","(๑˃̵ᴗ˂̵)و","( ´^益^｀)","(*´ ワ `*)"]
    _sad = ["(・´з`・)","(´ﾟЗﾟ｀)","(´～｀)"]

    def allEmogi(self):     #모든 이모지를 보여주는 함수
        print(self._angry + self._love + self._sad + self._smile)
	
        feel = input("찾으시는 감정을 영어로 검색해주세요.")
        if feel == "love":
            print(self._love)
        elif feel == "angry":
            print(self._angry)
        elif feel == "smile":
            print(self._smile)
        elif feel == "sad":
            print(self._sad)
        else:
            print("해당하는 감정이 없습니다.")

	
    def showCategory(self):     #현재 있는 카테고리를 보여주는 함수
        print("======================")
        print("1.Love")
        print("2.angry")
        print("3.smile")
        print("4.sad")
        print("======================")

    def chooseCategory(self, num):      #카테고리를 골랐을 때 그 카테고리 안에 있는 이모티콘들을 보여주는 함수
        if num == 1:
            print(self._love)
        elif num == 2:
            print(self._angry)
        elif num == 3:
            print(self._smile)
        elif num == 4:
            print(self._sad)
        else:
            print("해당 카테고리가 존재하지 않습니다.")

    def Menu(self):         #메인 메뉴를 보여주는 함수
        print("=======================")
        print("1.전체 이모지 보러가기")
        print("2.감정 검색하기")
        print("3.카테고리별 분류 보기")
        print("4.프로그램 종료하기")
        print("=======================")

    def choice(self):       #프로그램을 종료할지 다시 메뉴로 돌아갈지 물어보는 함수
	    print("돌아가시려면 1번")
	    print("종료 하시려면 2번")

    def main(self):         #전체 프로그램을 반복 동작시키는 함수
        while True:
            m.Menu()
            num = int(input("몇 번을 고르시겠습니까? "))
                
            if num == 1:
                m.allEmogi()
                m.choice()
                num = int(input("몇 번을 고르시겠습니까? "))
                
                if num == 1:
                    pass
                elif num == 2:
                    print("이용해주셔서 감사합니다.")
                    break

            elif num == 2:
                m.searchEmogi()
                m.choice()
                num = int(input("몇 번을 고르시겠습니까? "))
                
                if num == 1:
                    pass
                elif num == 2:
                    print("이용해주셔서 감사합니다.")
                    break        

            elif num == 3:
                m.showCategory()
                num = int(input("몇 번을 고르시겠습니까? "))
                m.chooseCategory(num)
                m.choice()
                num = int(input("몇 번을 고르시겠습니까? "))

                if num == 1:
                    pass
                elif num == 2:
                    print("이용해주셔서 감사합니다.")
                    break
            
            elif num == 4:
                print("이용해주셔서 감사합니다.")
                break

            else:
                print("해당 메뉴가 존재하지 않습니다.")
                m.Menu()


m = menu()
m.main()