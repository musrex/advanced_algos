import cProfile
import pstats
import random

def Mixer(array_size):
    '''Summary of Mixer()
    This function returns an array of 1000 i

    Input: This function takes an int as input that defines
    the size of the array.
    Output: This function returns an array of 1000 random integers.
    The integers range from -1000 to 1000.
    '''
    a = []
    while len(a) < array_size:
        a.append(random.randint(-1000,1000))        
    return a

# lists in various sizes
a1 = Mixer(1000)
a2 = Mixer(2000)
a3 = Mixer(3000)
a4 = Mixer(4000)
a5 = Mixer(5000)
a6 = Mixer(6000)
a7 = Mixer(7000)
a8 = Mixer(8000)
a9 = Mixer(9000)
a10 = Mixer(10000)


def merge_sort(array):
    '''This function recursively divides our array and then
    returns a list with the merge function passed as an argument.

    Input: Array
    Output: Sorted array
    '''
    if len(array) > 1:
        middle = len(array) // 2

        left = array[:middle]
        right = array[middle:]

        left = merge_sort(left)
        right = merge_sort(right)

        return list(merge(left, right))
    
    return array

def merge(left, right):
    '''This function merges our array, sorting it in the process.
    
    Input: The left and right halves of our array, set by merge_sort().
    Output: Our sorted array.
    '''
    array = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            array.append(left[0])
            left.remove(left[0])
        else:
            array.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        array = array + right
    else:
        array = array + left
    return array



if __name__=="__main__":
    cProfile.run('merge_sort(a1)')
    cProfile.run('merge_sort(a2)')
    cProfile.run('merge_sort(a3)')
    cProfile.run('merge_sort(a4)')
    cProfile.run('merge_sort(a5)')
    cProfile.run('merge_sort(a6)')
    cProfile.run('merge_sort(a7)')
    cProfile.run('merge_sort(a8)')
    cProfile.run('merge_sort(a9)')
    cProfile.run('merge_sort(a10)')    
