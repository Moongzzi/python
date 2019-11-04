from tictactoe import TicTacToe


class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        #게임판 보여주기
        print(self.ttt)

        while True:
            #row, col 입력받기
            row = int(input("row : "))
            col = int(input("col : "))

            self.ttt.set(row, col)
            print(self.ttt)

            #check_winner 면 끝내자
            if self.ttt.check_winner() == "o":
                print("o Win!")
                break
            elif self.ttt.check_winner() == "x":
                print("x Win!")
                break
            elif self.ttt.check_winner() == "d":
                print("무승부")
                break

if __name__ == '__main__':
    gm = GameManager()
    gm.play()