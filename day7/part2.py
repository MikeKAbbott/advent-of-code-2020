import re
class Luggage:

    def __init__(self, file):
        self.file = file
        self.data = self.parse_data()
        self.containers = self.get_containers()
        self.my_bag = "shiny gold bags"
        self.count = []

        self.get_results(self.my_bag)

    def __repr__(self):
        print(f'{len(self.count)}')
        
    def parse_data(self):
        pointer = open(self.file,"r")
        return [i for i in pointer]
        
    def get_containers(self):
        containers = {} 
        for i in self.data:
            vals = {}
            y = re.search(".bags",i).span()
            key = i[:y[1]]
            x = re.search("contain.",i).span()
            value = i[x[1]:].split(",")
            value = [val.strip(".\n") for val in value]
            
            for item in value:
                if item == "no other bags":
                    item = '0 ' + item
                cap = re.search("\d",item).group()
                span = re.search("\d",item).span()
                bag = item[span[1]:]
                bag = bag.strip(" ")
                if bag[len(bag) -1] != "s":
                    bag = bag + "s"
                vals[bag] = int(cap)

            if len(vals):    
                containers[key] = vals
        
        return containers
    
    
    def get_results(self,bag):
        children = self.containers[bag]
        for child in children:
            n = child
            q = int(children[child])
            for x in range(q):
                self.count.append(item for item in self.get_results(n))
        return self.count
                 

if __name__ == "__main__":
    luggage = Luggage("testData.txt")
    luggage.__repr__()

#guesses: 89 132 176035