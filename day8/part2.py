import re

class gameLoop:

    def __init__(self,file):
        self.file = file
        self.tried = []
        self.data = self.parseData()
        self.count = self.fixLoop(self.data)
        print(self.count)


    def resetData(self, data):
        for i in data:
            i.reset()
            

    def parseData(self):
        pointer = open(self.file,'r')
        parsed = [[i for i in re.split(" |\n",x) if i != ''] for x in pointer]
        data = []
        for i in parsed:
            data.append(node(i[0],i[1]))
        return data

    def accumulate(self, data):
        c = 0
        n = 0
        while n < len(data):
            temp = n
            if data[temp].isVisited():
                return False
            
            elif "nop" == data[temp].name:
                n += 1
            elif "acc" == data[temp].name:
                if data[temp].number[0] == '+':
                    c += int(data[temp].number[1:])
                else:
                    c -= int(data[temp].number[1:])
                n += 1
            else:
                if data[temp].number[0] == '+':
                    n += int(data[temp].number[1:])
                else:
                    n -= int(data[temp].number[1:])
            data[temp].visitNode()
        print(c)
        return c

    
    def swap(self, index):
        data = self.parseData()
        if data[index].name == 'nop':
            data[index].name = 'jmp'
        
        elif data[index].name == 'jmp':
            data[index].name = 'nop'
        return data

    def fixLoop(self, data):
        if self.accumulate(data):
            return self.accumulate(data)
        else:
            n = 0
            while n < len(data):
                if n not in self.tried:
                    self.tried.append(n)
                    data = self.swap(n)
                    break
                n += 1
            self.fixLoop(data)



class node:

    def __init__(self, name, number):
        self.visited = False
        self.name = name
        self.number = number

    def visitNode(self):
        self.visited = True
    
    def isVisited(self):
        return self.visited
    
    def reset(self):
        self.visited = False

    


if __name__ == "__main__":
    loop = gameLoop("data.txt")




