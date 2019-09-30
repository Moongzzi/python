f = open("file.txt", "r", encoding="utf8")
text = f.read()
print(text)
f.close()

#한줄씩
f = open("file.txt", "r", encoding="utf8")

text0 = f.readline()
print(text0)
text1 = f.readline()
print(text1)

f.close()