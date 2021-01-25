class funNumbers:

    def __init__(self, file):
        self.file = file
        self.data = self.parseData()
        self.preamble = [self.data[i] for i in range(0,25)]
        self.number = self.oddOneOut()
        self.range = []
        self.getRange(self.data)
    
    """
    Returns an array of data depending on the given file
    """
    def parseData(self):
        pointer = open(self.file,'r')
        return [int(i.strip("\n")) for i in pointer]

    """
    Helper function that resets the range array
    """
    def clear(self):
        self.range = []

    """
    Helper function that adds an item to the
    preamble array
    """
    def add(self, item):
        self.preamble.append(item)
    
    """
    Helper function that removes the first number of
    the preamble array
    """
    def remove(self):
        self.preamble.remove(self.preamble[0])

    """
    Check if the previous 25 numbers sums up to the given number
    """
    def isSum(self, item):
        for i in range(0,len(self.preamble)):
            for j in range(0,len(self.preamble)):
                if self.preamble[i] + self.preamble[j] == item:
                    return True
        return False
    
    """
    Part2 function that finds the range of numbers that add 
    to the faulting number and returns min + max values in that range
    """

    def getRange(self,data):
        index = data.index(self.number)
        if sum(self.range) > self.number:
            self.clear()
            data.remove(self.data[0])
        else:
            for i in range(0, index - 1):
                if data[i] < self.number:
                    self.range.append(data[i])   

                if sum(self.range) == self.number:
                    print(min(self.range) + max(self.range))
                    return min(self.range) + max(self.range)
        
        self.getRange(data)



    """
    Main functon that loops through the data that is not the preamble
    Returns the number that doesn't meet the requirement of being the sum
    of the previous 25 numbers
    """
    def oddOneOut(self):
        for i in range(25,len(self.data)):
            if not self.isSum(self.data[i]):
                return self.data[i]
            else:
                self.add(self.data[i])
                self.remove()

                   
if __name__ == "__main__":
    funNumbers("data.txt")