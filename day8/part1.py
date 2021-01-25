import re

class gameLoop:

    def __init__(self,file):
        self.file = file
        self.data = self.parseData()
        self.count = self.accumulate()
        print(self.count)
    
    def parseData(self):
        pointer = open(self.file,'r')
        parsed = [[i for i in re.split(" |\n",x) if i != ''] for x in pointer]
        data = []
        for i in parsed:
            data.append(node(i[0],i[1]))
        return data
        
    def accumulate(self):
        c = 0
        n = 0
        while n <= len(self.data):
            temp = n
            if self.data[temp].isVisted():
                return c
            
            elif "nop" == self.data[temp].name:
                n += 1
            elif "acc" == self.data[temp].name:
                if self.data[temp].number[0] == '+':
                    c += int(self.data[temp].number[1:])
                else:
                    c -= int(self.data[temp].number[1:])
                n += 1
            else:
                if self.data[temp].number[0] == '+':
                    n += int(self.data[temp].number[1:])
                else:
                    n -= int(self.data[temp].number[1:])
        
            self.data[temp].visitNode()


class node:

    def __init__(self, name, number):
        self.visited = False
        self.name = name
        self.number = number

    def visitNode(self):
        self.visited = True
    
    def isVisted(self):
        return self.visited


if __name__ == "__main__":
    loop = gameLoop("test.txt")




