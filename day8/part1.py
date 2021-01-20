import re
pointer = open("test.txt",'r')
data = [[i for i in re.split(" |\n",x)] for x in pointer]

c = 0
for i in data:
    if "" in i:
        i.remove("")

n = 0
while n < len(data):
    print("loop start",c)
    if "nop" in data[n]:
        print("no operation")
        n += 1
    if "acc" in data[n]:
        if data[n][1][0] == '+':
            c += int(data[n][1][1:])
        else:
            c -= int(data[n][1][1:])
        n += 1

    if "jmp" in data[n]:
        if data[n][1][0] == '+':
            n += int(data[n][1][1:])
        else:
            n -= int(data[n][1][1:])
