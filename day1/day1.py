import csv

class Vacation:
    def __init__(self, data):
        self.file = data
        self.data = self.parseData()

        print(self.vacation1())
        print(self.vacation2())

    def parseData(self):
        data = []
        with open(self.file, newline='') as csvfile:
            pointer = csv.reader(csvfile,delimiter = ' ',)
            for i in pointer:
                data.append(int(i[0]))
        return data
    
    def vacation1(self):
        for i in self.data:
            for j in self.data:
                if i + j == 2020:
                    return i * j

    def vacation2(self):
        for i in self.data:
            if 2020 - i in self.data:
                jindex = self.data.index(2020 - i)
                return i * self.data[jindex]


if __name__ == "__main__":
    vacation = Vacation("data.csv")