import csv

class Validation:
    
    def __init__(self, data):
        self.file = data
        self.data = self.parseData()

        print(self.validPassword())
        print(self.validPassword2())

    def parseData(self):
        data = []
        with open('day2.csv',newline='') as csvfile:
            pointer = csv.reader(csvfile,delimiter=' ')
            
            for i in pointer:
                data.append(i)
        
        return data

    def validPassword(self):
        valid = 0
        
        for code in self.data:
            xrange = code[0].split("-")
            letter = code[1]
            password = [char for char in code[2]]
            
            if password.count(letter[0]) >= int(xrange[0]) and password.count(letter[0]) <= int(xrange[1]):
                valid += 1;
        
        return valid


    def validPassword2(self):
        valids = 0
        data = [["1-5","f:","fasbfweg"],["1-3","a:","abcde"],["1-3", "b:", "cdefg"],["2-9","c:","ccccccccc"]]
        
        for code in data:
            xrange = code[0].split("-")
            xrange = [int(i) for i in xrange]
            letter = code[1]
            password = code[2]
            count = 0
            
            for i in xrange:
                if password[i-1] == letter[0]:
                    count +=1
            
            valids += 1 if count == 1 else 0
            
        return valids

if __name__ == "__main__":
    validation = Validation("day2.csv")