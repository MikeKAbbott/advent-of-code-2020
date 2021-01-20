import re
class Luggage:

    def __init__(self, file):
        self.file = file
        self.data = self.parse_data()
        self.containers = self.get_containers()
        self.my_bag = "shiny gold bags"
        self.count = self.get_results()

    def __repr__(self):
        print(f'{self.count}')
        
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
                if item != "no other bags":
                    cap = re.search("\d",item).group()
                    span = re.search("\d",item).span()
                    bag = item[span[1]:]
                    bag = bag.strip(" ")
                    if bag[len(bag) -1] != "s":
                        bag = bag + "s"
                    vals[bag] = cap

            if len(vals):    
                containers[key] = vals
        
        return containers
    
    
    def get_results(self):
        c = 0    
        for i, j in self.containers.items():
            if i != self.my_bag: 
                c += self.results_helper(self.containers,i)
        return c
         
    def results_helper(self,bags,current_bag):
        if self.my_bag == current_bag:
            return 1
        if self.containers.get(current_bag) is None:
            return 0
        else:
            x = []
            for k, v in bags[current_bag].items():
                x.append(self.results_helper(bags,k))
            return max(x)   
        



if __name__ == "__main__":
    luggage = Luggage("data.txt")
    luggage.__repr__()
