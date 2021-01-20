import csv
import math

class SeatFinder:

    def __init__(self,file):
        self.file = file
        self.row = 0
        self.seats = []
        self.seat = 0
        self.col = 0
        self.data = []
        self.front = 0
        self.back = 0

    def __repr__(self):
        print(self.seat)
    def parse_data(self):
        pointer = open(self.file)
        self.data = [i.strip("\n") for i in pointer]
        for i in self.data:
            self.find_seat(i)
        self.front = min(self.seats)
        self.back = max(self.seats)
        self.my_seat()

    def find_seat(self,data):
        low_row = 0
        low_col = 0
        upper_row = 127
        upper_col = 7
        for i in range(0,7,1):
            if data[i] == "F":
                upper_row = math.floor(upper_row / 2) + round(low_row / 2)
            if data[i] == "B":    
                low_row = round(upper_row / 2) + round(low_row / 2)
        self.row = min(int(upper_row),int(low_row)) if data[6] == "F" else max(int(upper_row),int(low_row))
        
        for i in range(7,10,1):
            if data[i] == "R":
                low_col = round(upper_col / 2) + round(low_col / 2)
            if data[i] == "L":
                upper_col = math.floor(upper_col / 2) + round(low_col / 2)
        self.col = min(int(upper_col),int(low_col)) if data[9] == "L" else max(int(upper_col),int(low_col))
        self.seats.append(self.row * 8 + self.col)
        
    def my_seat(self):
        self.seats = sorted(self.seats)
        for i in range(0,len(self.seats)-1):
            diff = self.seats[i+1] - self.seats[i]
            seat = self.seats[i] + 1
            if diff == 2 and seat not in self.seats:
                self.seat = seat
                self.__repr__()
                
                
                    


if __name__ == "__main__":
    seatfinder = SeatFinder("data.txt")
    seatfinder.parse_data()

