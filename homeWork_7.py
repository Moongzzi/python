#야구 게임
import random

r0 = random.randrange(1, 9+1)
r0 = str(r0)

r1 = random.randrange(1, 9+1)
r1 = str(r1)

r2 = random.randrange(1, 9+1)
r2 = str(r2)

computer = r0 + r1 + r2

l = list(range(1,9+1))
random.shuffle(l)
l[:3]



l = random.sample(range(1,9+1),3)
computer = ''.join(str(i) for i in l[:3])

while True:
    player = input("숫자 세자리 맞춰봐: ")
    strike = 0
    ball = 0

    for i in range(len(computer)):
        for j in range(len(player)):
            if computer[i] == player[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1

    #print(player, "strike: ", strike, "ball: ",ball)
    print("{}\tstrike:{}\tball:{}".format(player, strike, ball))

    print(player, strike, ball)
    if computer == player:
        print("Hit")
        break