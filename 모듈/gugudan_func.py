def gugudan(n):
    print(n, "단을 출력합니다.")
    for i in range(1, 9+1):
        print(n, "+", i, "=", n*i)

if __name__ == '__main__':
        gugudan(3)