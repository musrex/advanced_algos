import random
# Task 1
# Randomizes a vector of 1000 positve and negative integers
# Finds the maximum contiguous subsequence sum value
# Prints out maximum value
# a = [5,-1,56,-3,-18,22,-9]

def Mixer():
    '''Summary of Mixer()
    This function returns an array of 1000 i

    Input: This function takes no input parameters
    Output: This function returns an array of 1000 random integers.
    The integers range from -1000 to 1000.
    '''
    a = []
    while len(a) < 1000:
        a.append(random.randint(-1000,1000))        
    return a

def MCSS(a):
    '''
    Input: An array of n ints
    Output: An integer, the maximum subsequence sum value
    '''
    largest, acc, i = 0, 0, 0
    for j in range(len(a)):
        acc += a[j]
        if (acc > largest):
            largest = acc
        elif (acc < 0):
            i = j + 1
            acc = 0
    return largest

def taskOne():
    '''
    Input: This function takes no input paremeters.
    Output: This function returns the MCSS with the Mixer function
    passed as a parameter. 
    '''
    result = MCSS(Mixer())
    print(f'''Task 1
Maximum Contiguous Subsequence Sum Value: {result}
''')

if __name__=="__main__":
    taskOne()


# Task 2
# Extend Task 2
# Include initial and final index of elements used to compute
# maximum value

# a = [5, -1, 56, -3, -18, 22, -9]

def MCSStwo(a):
    '''
    Input: An array of n ints
    Output: An integer, the maximum subsequence sum value
    '''
    largest, acc, i = 0, 0, 0
    start, end = 0, 0
    for j in range(len(a)):
        acc += a[j]
        if (acc > largest):
            largest = acc
            end = j
        elif (acc < 0):
            i = j + 1
            acc = 0
            if i < len(a):
                start = i 
    return f"start: {start}; end: {end}; MCSS val: {largest}"

def taskTwo():
    '''
    Input: This function takes no input paremeters.
    Output: This function returns the MCSS with the Mixer function
    passed as a parameter. 
    '''
    result = MCSStwo(Mixer())
    print(f'''Task 2
{result}
''')

if __name__=="__main__":
    taskTwo()