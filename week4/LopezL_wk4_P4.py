import csv

class Item:
    def __init__(self, name, value, height, width, depth,) -> None:
        self.name = name
        self.value = int(value)
        self.height = int(height)
        self.width = int(width)
        self.depth = int(depth)
        

    def volume(self) -> int:
        return int(self.height * self.width * self.depth)
    
    def ratio(self) -> int:
        return int(self.value/self.volume())

    def display(self) -> str:
        print(f"{self.name}: {self.value}, {self.height}, {self.width}, {self.depth}, {self.volume}")            

def knapsack(items, capacity):
    ratios = []
    for i in range(len(items)):
        ratios.append([items[i].ratio(), items[i].value, items[i].volume(), i])
    ratios.sort(reverse=True)
    answer = []
    total_weight = 0
    found = True
    while found:
        found = False
        for num in ratios:
            if num[1] + total_weight <= capacity:
                answer.append(num[2])
                total_weight += num[1]
                found = True
                break
    return answer

def main():
    #csv_file = input("Enter file location: ")
    items = []
    with open('/home/leandro/Documents/advanced_algos/week4/packs.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            item = Item(name=row[0], value=row[1], height=row[2], width=row[3], depth=row[4])
            items.append(item)
    capacity = int(input("Enter capacity: "))            
    result = knapsack(items, capacity)
    print(result)
    #total_value, total_weight = 0, 0
    #for item in result:
    #    print(f"{item.name}: ${item.value}")


if __name__ == "__main__":
    main()