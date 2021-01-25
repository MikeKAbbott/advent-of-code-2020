class funNumbers:

    def __init__(self, file):
        self.file = file
        self.data = self.parseData()
        self.preamble = [self.data[i] for i in range(0,25)]
        self.oddOneOut()
    
    """
    Returns an array of data depending on the given file
    """
    def parseData(self):
        pointer = open(self.file,'r')
        return [int(i.strip("\n")) for i in pointer]

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
    Main functon that loops through the data that is not the preamble
    Returns the number that doesn't meet the requirement of being the sum
    of the previous 25 numbers
    """
    def oddOneOut(self):
        for i in range(25,len(self.data)):
            if not self.isSum(self.data[i]):
                print(self.data[i])
                return self.data[i]
            else:
                self.add(self.data[i])
                self.remove()

                   
if __name__ == "__main__":
    funNumbers("data.txt")