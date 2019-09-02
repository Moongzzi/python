num = input("숫자를 입력하세요")
total = 0

for i in range(len(num)):
    total += int(num[i])

print(total)