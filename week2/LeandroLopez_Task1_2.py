import random

# WORKSHEET TASKS 1 & 2 

# Worksheet Task 1
# A program that randomizes an array of 1000 integers from 1 to 1,000,000 
# and verifyies the uniqueness of its elements using a
# brute force algorithm and a transform-and-conquer algorithm

def Mixer(array_size, range_min, range_max):
    '''Summary of Mixer()
    This function returns an array of 1000 i

    Input: This requires as input the size of the array to be returned,
    the minimum value of the range, and the maximum value of the range.

    Output: This function returns an array according to the input parameters.
    '''
    a = []
    while len(a) < array_size:
        a.append(random.randint(range_min,range_max))        
    return a

def brute(a: list) -> bool:
    '''Summary of brute()
    This function returns True if the array contains no duplicates.
    
    This function uses a brute force algorithm. It compares each element
    of the array with every other element of the array to look for duplicates.
    This algorithm has an O(n^2) time complexity.

    Input: This function takes an array of integers as input.
    Output: This function returns True if the array contains no duplicates, 
    false otherwise.'''
    for i, val1 in enumerate(a):
        for j, val2 in enumerate(a[i+1:]):
            if val1 == val2:
                return False
    return True

def transform(a: list) -> bool:
    '''Summary of transform()
    This function returns True if the array contains no duplicates.

    This function uses a transform-and-conquer algorithm. It sorts the array
    by sorting it first and then comparing each element with the next one.
    This algorithm has an O(n log n) time complexity.

    Input: This function takes an array of integers as input.
    Output: This function returns True if the array contains no duplicates,
    false otherwise.'''
    a.sort()
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return False
    return True

def worksheet1():
    '''Summary of worksheet1()
    This function prints the results of the brute force algorithm and the
    transform-and-conquer algorithm for an array of 1000 random integers.

    Input: This function takes no input parameters.
    Output: This function prints the results of the brute force algorithm and
    the transform-and-conquer algorithm for an array of 1000 random integers.
    '''
    array1 = Mixer(1000,1,1000000)
    array2 = [1,2,3,4,5,6,7,8,9,0]
    array3 = [1,2,2,2,2,3,4,5,6,7,8,9,0]
    print('''
WORKSHEET TASK 1
================          
          ''')
    print(f'Array 1: Commented out') #{array1}')
    print(f'Array 2: {array2}')
    print(f'Array 3: {array3}')
    print(f'Brute, Array 1: {brute(array1)}')
    print(f'Brute, Array 2: {brute(array2)}')
    print(f'Brute, Array 3: {brute(array3)}')
    print(f'Transform, Array 1: {transform(array1)}')
    print(f'Transform, Array 2: {transform(array2)}')
    print(f'Transform, Array 3: {transform(array3)}')


# Worksheet Task 2
# The Mode within a sorted array
# A function that receives an array of numbers, 
# sorts this array and returns the mode.
# Ensure the code is less complex than the brute force algorithm

def mode(a: list) -> int:
    '''Summary of mode()
    This function returns the mode of an array of integers.
    
    This function uses a transform-and-conquer algorithm. It sorts the array
    and then compares each element with the next one. If the next element is
    the same as the current one, it increases the counter. If the counter is
    greater than the maximum counter, it updates the maximum counter and the
    mode. This algorithm has an O(n log n) time complexity.

    Input: This function takes an array of integers as input.
    Output: This function returns the mode of the array of integers.
    '''
    a.sort()
    mode, max, cur = 0, 0, 0

    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            cur += 1
            if cur > max:
                max = cur
                mode = a[i]
    return mode

def worksheet2():
    '''Summary of worksheet2()
    This function prints the mode of an array of 1000 random integers.

    Input: This function takes no input parameters.
    Output: This function prints the mode of an array of 1000 random integers.
    '''
    print('''
WORKSHEET TASK 2
================          
          ''')
    array1 = Mixer(1000,1,1000000)
    array2 = [1,2,2,2,2,3,4,5,6,7,8,9,0]

    print(f'Mode of array1: {mode(array1)}')
    print(f'Mode of array2: {mode(array2)}')


if __name__ == "__main__":
    worksheet1()
    worksheet2()