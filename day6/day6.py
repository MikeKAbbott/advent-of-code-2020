import csv
import re
class Questions:

    def __init__(self,file):
        self.file = file
        self.data = []
        self.everyone_total = 0
        self.yes_total = 0

    def parse_data(self):
        pointer = open(self.file,"r").read().strip("\n")
        self.data = [[y for y in re.split(" |\n",x)] for x in pointer.split("\n\n")]
        for i in self.data:
            self.count_everyone(i)
        self.count_only_yes()

    #part one
    def count_everyone(self,data):
        temp = []
        for group in data:
            for answer in range(0,len(group),1):
                if group[answer] not in temp:
                    temp.append(group[answer])
                    self.everyone_total += 1
    #part two
    def count_only_yes(self):
        for group in self.data:
            x = set(group[0])
            for i in range(1,len(group)):
                x &= set(group[i])
            self.yes_total += len(x)
        print(self.yes_total)

if __name__ == "__main__":
    questions = Questions("data.txt")
    questions.parse_data()