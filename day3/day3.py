import csv
data = []
with open('data.csv',newline="") as csvfile:
    getData = csv.reader(csvfile,delimiter=" ")
    for i in getData:
         data.append(i[0])


def trees():
    treeCount = 0
    pos = 0
    for space in data:
        pos += 3
        if pos >=0  and pos < len(space)
            if space[pos] == "#":
                treeCount +=1
        else 

    print(treeCount)

def move():
    

trees()