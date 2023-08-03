import csv
from collections import defaultdict

class Item:
    '''Summary of Item class
    This class is used to create an item object that has a name, value, height, width, and depth.
    We use these attributes to calculate the volume and ratio of the item.
    We also have a display method to print out the attributes of the item, for development purposes.
    '''
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
    '''Summary of knapsack function
    This function takes in a list of items and a capacity.
    It then sorts the items by their ratio of value to volume and returns the 
    optimal number of items based on the capacity and value.
    
    Input: list of items, capacity
    Output: list of items, dictionary of item counts, total volume
    '''
    ratios = []
    for i in range(len(items)):
        ratios.append([items[i].ratio(), items[i].value, items[i].volume(), i])
    ratios.sort(reverse=True)
    answer = []
    item_counts = defaultdict(int) #this is a cool way to initialize a dictionary with default values
    total_volume = 0
    found = True
    while found:
        found = False
        for num in ratios:
            if num[2] + total_volume <= capacity:
                answer.append(num[3])
                item_counts[items[num[3]].name] += 1
                total_volume += num[2]
                found = True
                break
    return answer, item_counts, total_volume

def main():
    '''Summary of main function
    This function takes in a csv file of items and a capacity.
    With the items in the csv file, it creates a list of item objects.
    We then pass this list of item objects and our capacity to the knapsack function.
    After the knapsack function returns the optimal items,
    we calculate the total value of the items and print out the results.
    '''
    csv_file = input("Enter file location: ")
    items = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            item = Item(name=row[0], value=row[1], height=row[2], width=row[3], depth=row[4])
            items.append(item)
    capacity = int(input("Enter capacity: "))            
    result, item_counts, total_volume = knapsack(items, capacity)
    total_value = 0
    for i in result:
        item = items[i]
        total_value += item.value
        
    result_string = "The suggested items are: "
    for item, count in item_counts.items():
        result_string += f"{count} {item}, "

    leftover_space = capacity - total_volume
    result_string = result_string.rstrip(", ") + f" with a total value of ${total_value}. There were {leftover_space} square inches left unused."
    print(result_string)



if __name__ == "__main__":
    main()