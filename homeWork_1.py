classes = [
    ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어 디자인과"], 
    ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어 디자인과"], 
    ["인터렉티브미디어과", "뉴미디어디자인과", "뉴미디어솔루션과"]
]

s_num = input("학번을 입력하세요: ")

grade = s_num[0]
grade = int(grade)

c_room = s_num[1]
c_room = int(c_room)

num = s_num[2:]
num = int(num)

print( grade, "학년", classes[grade-1][(c_room-1) // 2], c_room,"반", num, "번입니다") 