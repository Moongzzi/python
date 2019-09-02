for x in range(3, 9, 2):
    print(x)

for ch in "LOVE":
    print(ch)

for item in [ "힙합", "발라드"]:
    print(item)

for item in (2560,  1440):
    print(item)

pl = {"c":1972, "Java":1995, "Python":1991}

for key in pl:
    print(key, ":", pl[key])

for item in {"HTML5", "CSS3", "JavaScript"}:
    print(item + "를 할 수 있다.")

table = [ ["월", "화", "수"], [1,2,3] ]

for row in table:
    for col in row:
        print(col)
    print("==========")