import csv
import re

class Passport:
    def __init__(self,file):
        self.valid = 0
        self.file = file
        self.data = []
        self.fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

    def __repr__(self):
        return (f'{self.valid}')

    def parse_data(self):
        pointer = open(self.file).read().strip('\n')
        self.data = [[y.split(':') for y in re.split(' |\n', x)] for x in pointer.split('\n\n')]
        
        for item in self.data:
            self.present(item)
            
        print(self.__repr__())

    def present(self,data):
        c = 0
        for item in data: 
            if item[0] in self.fields:
                if self.validate(item[0],item[1]):
                    c += 1        
        if c == 7:
            c = 0
            self.count()
    
    def validate(self,key,value):
        if key == 'byr':
            if len(value) == 4 and (int(value) >= 1920 and int(value) <= 2002):
                return True
        if key == 'iyr':
            if len(value) == 4 and (int(value) >= 2010 and int(value) <= 2020):
                return True
            
        if key == 'eyr':
            if len(value) == 4 and (int(value) >= 2020 and int(value) <= 2030):
                return True

        if key == 'hgt':
            if re.search("in",value):
                value = int(re.search(".+?(?=[a-z])",value).group())
                if value >= 59 and value <= 76:
                    return True
            
            elif re.search("cm",value):
                value = int(re.search(".+?(?=[a-z])",value).group())
                if value >= 150 and value <= 193:
                    return True

        if key == 'hcl':
            if re.search('^#(\d|[a-f]){6}$',value):
                return True
                
        if key == 'ecl':
            if value in ["amb","blu","brn","gry","grn","hzl","oth"]:
                return True

        if key == 'pid':
            if len(value) == 9:
                return True
        else:
            return False

    def count(self):
        self.valid += 1;




if __name__ == "__main__":
    passport = Passport("data.txt")
    passport.parse_data()
