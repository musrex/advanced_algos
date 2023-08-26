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
    

start_index = random.randint(1, 9998)

# Create an array of function values
function_values = [myFunction(i) for i in range(10000)]

def hillClimb(arr, start_index):
    current_index = start_index

    while True:
        # Get the left and right neighbor values if they exist
        left_value = arr[current_index - 1] if current_index > 0 else float('-inf')
        right_value = arr[current_index + 1] if current_index < len(arr) - 1 else float('-inf')

        # If we are on a local maximum
        if left_value < arr[current_index] > right_value:
            return current_index, arr[current_index]

        # Check if we are on a flat shoulder to the right
        elif arr[current_index] == right_value:
            shoulder_start = current_index

            # Traverse the shoulder to the right
            while current_index < len(arr) - 1 and arr[current_index] == arr[current_index + 1]:
                current_index += 1
            
            # If the value after the shoulder is higher, set it as the maximum value
            if current_index < len(arr) - 1 and arr[current_index + 1] > arr[shoulder_start]:
                return current_index + 1, arr[current_index + 1]
            # Otherwise, return the start of the shoulder
            else:
                return shoulder_start, arr[shoulder_start]
                
        # Check if we are on a flat shoulder to the left
        elif arr[current_index] == left_value:
            shoulder_start = current_index

            # Traverse the shoulder to the left
            while current_index > 0 and arr[current_index] == arr[current_index - 1]:
                current_index -= 1
            
            # If the value before the shoulder is higher, set it as the maximum value
            if current_index > 0 and arr[current_index - 1] > arr[shoulder_start]:
                return current_index - 1, arr[current_index - 1]
            # Otherwise, return the start of the shoulder
            else:
                current_index -=1

        # If there's a higher value on the left or the right, move to that index
        elif left_value > arr[current_index] or right_value > arr[current_index]:
            if left_value > right_value:
                current_index -= 1
            else:
                current_index += 1

# Call the hill climbing function
print(hillClimb([6,5,5,5,4,3,2], 5))  # Expected: (0, 6)
print(hillClimb([2,5,5,5,4,3,2], 5))  # Expected: (1, 5)

print(hillClimb(function_values, start_index))