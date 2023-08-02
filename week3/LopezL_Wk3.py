# Worksheet 3
# Leandro Lopez
# Merrimack College, CS 2063

##########
# Task 1 #
##########
# Computing the number of balanced matrices  
# Enter an even matrix order:2  
# The number of balanced matrices is 2  

# Computing the number of balanced matrices  
# Enter an even matrix order:4  
# The number of balanced matrices is 90  

# Computing the number of balanced matrices  
# Enter an even matrix order:6  
# The number of balanced matrices is 297200  

# Computing the number of balanced matrices  
# Enter an even matrix order:8  
# *The program never finishes computing*  

from itertools import combinations

def permutations(n):
    ones = list(combinations(list(range(n)),n//2))
    ans = []
    for o in ones:
        case = []
        for i in range(n):
            if (i in o):
                case.append(1)
            else:
                case.append(0)
        ans.append(case)
    return ans

def check(mat):
    n = len(mat[0])
    for j in range(n):
        acc0, acc1 = 0, 0
        for i in range(len(mat)):
            if (mat[i][j] == 1):
                acc1 += 1
            elif (mat[i][j] == 0):
                acc0 += 1
            if (acc0 > (n//2)) or (acc1 > n//2):
                return False
    return True

def layer(r, mat, perm, ans):
    for p in perm:
        mat.append(p)
        if check(mat):
            if (r+1 == len(p)):
                ans += 1
            else:
                ans = layer(r+1, mat, perm, ans)
        mat.pop()
    return ans

def balanced01mat():
    print("Computing the number of balanced matrices")
    n = 1
    # changing the code so 2,4,6,8 are hard coded. Note: 8 has been 
    # removed - it takes too long to compute
    for n in [2,4,6]:
        if n == 8:
            pass
        perm = permutations(n)
        ans = layer(0, [], perm, 0)
        print(f"The number of balanced matrices in {n} matrix is {ans}")

# The number of balanced matrices in 2 matrix is 2
# The number of balanced matrices in 4 matrix is 90
# The number of balanced matrices in 6 matrix is 297200
# The calculations for 8 matrix took too long. Program was stopped

##########
# Task 2 #
##########

def hanoi(n, source, target, aux):
    '''Summary of hanoi function
    This function solves the Tower of Hanoi problem. 
    
    Input: n, the number of discs; source, target, and aux, the three pegs
    Output: the count of minimum moves required to solve problem
    '''
    if n == 0:
        return 0
    else:
        count = hanoi(n - 1, source, aux, target)
        # print(f'Move disk {n} from {source} to {target}')
        count += 1

        count += hanoi(n - 1, aux, target, source)

        return count

def main():
    ''' Summary of main function
    This function prompts the user for the number
    of discs to solve the Tower of Hanoi problem.
    It then calls the hanoi function and prints the
    number of moves required to solve the problem.
    '''
    num_discs = int(input('Enter the number of discs: '))
    print(f'Number of moves: {hanoi(num_discs, "A", "C", "B")}')

if __name__ == "__main__":
    balanced01mat()
    main()