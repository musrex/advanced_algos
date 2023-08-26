# Leandro Lopez
# Merrimacl College, CSC 6023

# Task 1
# Create a program that generates a random array of 10,000 elements
# with equal number of 0's and 1's
# and then implement the randomized Las Vegas algorithm
# that searches for an element holding a 1
# Your program should output the position of the first 1 found, plus the number of tries before finding it.

import random

def mixer():
    '''Summary of mixer() function
    This function creates a randomized list.
    It has no input paramaters and ouputs a list.
    '''
    arr = []
    for i in range(10000):
        arr.append(random.randint(0,1))
    return arr

def vegas(arr):
    '''Summary of vegas() function
    This function searches for a 1 in an array
    using the Las Vegas algorithm. It returns
    the position of the 1 found and the number
    of tries it took to find it. 

    Input: List, array, []
    Output: Tuple, (1, tries)
    '''
    tries = 0
    for i in arr:
        tries += 1
        if i == 1:
            return i, tries
    return i, tries


# Task 2
# Create a program that generates a random array of 10,000 elements
# with equal number of 0's and 1's
# and then implement the randomized Monte Carlo algorithm
# that searches for an element holding a 1
# Set k equal to 10
# Your program should output the position of the first 1 found, plus the number of tries before finding it or a message stating that it did not find the 1 after k attempts.

def monte(arr, k):
    '''Summary of monte() function
    This function searches for a 1 in an array
    using the Monte Carlo algorithm. It takes
    a list, arr, and a number of tries, k, as input and
    returns the position of the 1 found and the number
    of tries it took to find it. If the 1 is not found
    after k tries, it returns a message stating so.

    Input: List, array, []
    Output: Tuple, (1, tries) 
    '''
    tries = 0
    
    found = False
    while not found:
        tries += 1
        pick = random.randint(0, len(arr)-1)
        if arr[pick] == 1:
            found = True
            return pick, tries
        if tries == k:
            return f'Could not find 1 after {k} attempts'



def main():
    arr = mixer()
    arr2 = mixer()
    print("Las Vegas Algorithm: ", vegas(arr))
    print("Monte Carlo Algorithm: ", monte(arr2, 10))

if __name__ == "__main__":
    main()