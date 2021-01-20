import csv
import time

data = []
with open('data.csv',newline='') as csvfile:
    pointer = csv.reader(csvfile,delimiter = ' ',)
    for i in pointer:
        data.append(int(i[0]))
    
def vacation1():
    for i in data:
        for j in data:
            if i + j == 2020:
                print(i*j)
                return


start = time.time()
vacation1()
end = time.time()
print("first: ", end - start)



def vacation2(numbers):
    for i in numbers:
        if 2020 - i in numbers:
            jindex = numbers.index(2020 - i)
            print(i * numbers[jindex])
            return

start = time.time()
vacation2(data)
end = time.time()
print("second: ", end - start)