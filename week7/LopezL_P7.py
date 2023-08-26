import math
import random

def myFunction(x):
    if x == 0:
        return 0
    elif ((math.log2(x) * 7) % 17) < (x % 13):
        return (x + math.log2(x))**3 
    elif ((math.log2(x) * 5) % 23) < (x % 19):
        return (math.log2(x) * 2)**3
    else:
        return (math.log2(x)**2) -x
    
start_index = random.randint(0,1000)

def hillClimb(arr, start_index):
    current_index = start_index

    while True:
        # If at the edges of the array, stop
        if current_index == 0 or current_index == len(arr) - 1:
            return current_index, arr[current_index]
        
        # Get the left and right neighbor values
        left_value = arr[current_index - 1]
        right_value = arr[current_index + 1]

        # Check if we are on a flat shoulder
        if arr[current_index] == left_value or arr[current_index] == right_value:
            original_index = current_index  # Save the original position before traversing the shoulder
            
            # Check the direction of the shoulder by moving right
            while current_index < len(arr) - 1 and arr[current_index] == arr[current_index + 1]:
                current_index += 1
            
            # If at the end of the shoulder the value decreases, return the original position
            if current_index < len(arr) - 1 and arr[current_index + 1] < arr[current_index]:
                return original_index, arr[original_index]
            # Otherwise, continue with the search
            else:
                continue
        
        # If the current index is a local maximum, return it
        elif arr[current_index] >= left_value and arr[current_index] >= right_value:
            return current_index, arr[current_index]
        
        # If there's a higher value on the left or the right, move to that index
        elif left_value > arr[current_index] or right_value > arr[current_index]:
            if left_value > right_value:
                current_index -= 1
            else:
                current_index += 1
        # If neither side is higher, then we're at a local maximum
        else:
            return current_index, arr[current_index]

# Example usage:
print(hillClimb([6,5,5,5,4,3,2], 5))  # Expected: (0, 6)
print(hillClimb([2,5,5,5,4,3,2], 5))  # Expected: (1, 5)
