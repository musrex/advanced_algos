# Worksheet 4 - Task 3 & 4
# Leandro Lopez
# Merrimack College, CS 2063

# knapsack unbounded - Greedy approach

def knapsack(v, w, cap):
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(v)):
        rwv.append([v[i]/w[i],w[i],v[i],i])
    rwv.sort(reverse=True)    # sort from high to low rate
    ans = []                     # the list of added items
    tw = 0                                  # total weight
    found = True
    while (found):        # until no fitting item is found
        found = False
        for t in rwv:              # search an item to add
            if (t[1] + tw) <= cap:      # if the item fits
                ans.append(t[3])                  # add it
                tw += t[1]
                found = True
                break
    return ans           # returns the list of added items

def main():
    items = int(input("Number of distinct items: "))
    values, weights = [],[]
    for i in range(items):
        v = int(input("Value of item "+str(i+1)+": "))
        w = int(input("Weight of item "+str(i+1)+": "))
        values.append(v)
        weights.append(w)
    capacity = int(input("Maximum weight (capacity): "))
    answer = knapsack(values, weights, capacity)
    tv, tw = 0, 0
    for a in answer:
        print("Item - Value:", values[a], "- Weight:", weights[a])
        tv += values[a]
        tw += weights[a]
    print("Items:", len(answer), "- Value:", tv, "- Weight:", tw)

main()

############
#  Task 3  #
############

# ([5,10] [8,20] [12,30]) - capacity 838
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Item - Value: 5 - Weight: 10
# Items: 83 - Value: 415 - Weight: 830

# ([3,17] [5,23] [7,29] [11,31] [13,37] - capacity 997
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Item - Value: 11 - Weight: 31
# Items: 32 - Value: 352 - Weight: 992

# ([5,25] [6,36] [7,49] [8,64]) - capacity 250
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Items: 10 - Value: 50 - Weight: 250

# ([5,25] [6,36] [7,49] [8,64]) - capacity 360
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Item - Value: 5 - Weight: 25
# Items: 14 - Value: 70 - Weight: 350




############
#  Task 4  #
############

# ([1/3] [2,6] [3,8] [1,4] [4,11]) - capacity 100
# Item - Value: 3 - Weight: 8
# Item - Value: 3 - Weight: 8
# Item - Value: 3 - Weight: 8
# Item - Value: 3 - Weight: 8
# Item - Value: 3 - Weight: 8
# Item - Value: 3 - Weight: 8
# Item - Value: 3 - Weight: 8
# Item - Value: 3 - Weight: 8
# Item - Value: 3 - Weight: 8
# Item - Value: 3 - Weight: 8
# Item - Value: 3 - Weight: 8
# Item - Value: 3 - Weight: 8
# Item - Value: 1 - Weight: 3
# Items: 13 - Value: 37 - Weight: 99