f = open("file.txt","r")
str=""

for i in range(0,100):
    str=str + f.read(i)

print(str)
