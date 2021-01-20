import csv

data = []
with open('day2.csv',newline='') as csvfile:
    pointer = csv.reader(csvfile,delimiter=' ')
    for i in pointer:
        data.append(i);
#print(data)
def validPassword():
    valid = 0
    for code in data:
        xrange = code[0].split("-")
        letter = code[1]
        password = [char for char in code[2]]
        if password.count(letter[0]) >= int(xrange[0]) and password.count(letter[0]) <= int(xrange[1]):
            valid +=1;
    print(valid)

#validPassword()


def validPassword2():
    valid = 0
    thisdata = [["1-5","f:","fasbfweg"],["1-3","a:","abcde"],["1-3", "b:", "cdefg"],["2-9","c:","ccccccccc"]]
    for code in data:
        xrange = code[0].split("-")
        xrange = [int(i) for i in xrange]
        letter = code[1]
        password = code[2]
        count = 0
        for i in xrange:
            if password[i-1] == letter[0]:
                count +=1
        valid += 1 if count == 1 else 0
        
    print(valid)
validPassword2()