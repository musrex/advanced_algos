import numpy as np
# Implement a Linear Programming Calculator
# Your program should receive the necessary information
# for an LP problem, namely:
# - The number of variables (that will be equal to the number of constraints coefficients)
#  - x
# - The coefficients of each variable for the objective function
#   - f(x)
# - The data for the square matrix stating the constraints
#   - A 
# - The constraint limits
#   - b
# Having all input parameters, the program should compute the possible solution
# for each variable alone, and the solution of the linear equation system Ax = b.
# e.g. f(a,b,d) = 3a + 2b + 2c
# Ax = b
# A - Matrix Data
# b - Constraint Limits
# x - Variables
 
def get_coefficients(num_var):
    coefficients = []
    for i in range(num_var):
        coefs = float(input("Enter the coefficients for variables " + str(i+1) + ": "))
        coefficients.append(coefs)    

    return np.array(coefficients)

def get_matrix_data(num_var):
    matrix_data = []
    print('''Enter the data for the square matrix stating the constraint.
You will be asked for each row individually.
Separate each value by a space.
For example: 2 1 8''')
    for i in range(num_var):
        data = input("Enter the data for row " + str(i+1) + ": ")
        data = [float(x) for x in data.split()] 
        matrix_data.append(data)

    return np.array(matrix_data)    

def get_constraint_limits(num_var):
    constraint_limits = []
    for i in range(num_var):
        limit = float(input("Enter the constraint limit for constraint " + str(i+1) + ": "))
        constraint_limits.append(limit)

    return np.array(constraint_limits)

def header(num_var):
    print("\n| SUPPLY |", end="")
    for i in range(1, num_var+1):
        print(f" CONSTRAINT{i} |", end="")
    print(" PROFIT |")
    for i in range(num_var+1):
        print(f"================", end="")

def display_chart(coefficiants, matrix_data, constraints):
    print("\n")
    for i in range(len(coefficiants)):
        print(f"| Variable {i+1} | ", end="")
        for j in matrix_data[i]:
            print(f"     {j}", end="| ")
        print(f"     {coefficiants[i]}|")

def display_availability(constraints):
    print("\n| AVAIL. | ", end="")
    for c in constraints:
        print(f"     {c}", end="| ")

def linear_problem(constraints, matrix_data):
    A = matrix_data
    b = constraints    
    return(np.linalg.inv(A).dot(b))

def only_one(num_var,constraints, matrix_data):
    for i in range(1, num_var + 1):
        A = matrix_data[i-1,:]
        b = constraints[i-1]
        x = np.linalg.inv(A).dot(b)
        print(x)



def main():
    print(f'''
~~~~~~~~~~~~~~~Welcome to the~~~~~~~~~~~~~~~~~~
~~~~~~~~Linear Programming Calculator!~~~~~~~~~
+=============================================+
|                                             |
| This program will help you find the optimal | 
| solution to a linear programming problem.   |
|                                             |
+=============================================+''')
    run = True
    while run:
        try:
            num_var = int(input("Enter the number of variables: ")) # for example, 2 in slides, pants & jackets
            coefficients = get_coefficients(num_var)
            matrix_data = get_matrix_data(num_var)
            constraints = get_constraint_limits(num_var)
            header(num_var)
            display_chart(coefficients, matrix_data, constraints)
            display_availability(constraints)
            print("\n")
            x = linear_problem(constraints, matrix_data)
            print(f"The optimal solution is: {x}")
            quit = input("Would you like to quit? (y/n): ")
            if quit == "y":
                run = False
                break
        except:
            print("Invalid input. Please try again.")
            continue

if __name__ == "__main__":
    main()


# ~~~~~~~~~~~~~~~Welcome to the~~~~~~~~~~~~~~~~~~
# ~~~~~~~~Linear Programming Calculator!~~~~~~~~~
# +=============================================+
# |                                             |
# | This program will help you find the optimal | 
# | solution to a linear programming problem.   |
# |                                             |
# +=============================================+
# Enter the number of variables: 3
# Enter the coefficients for variables 1: 3000
# Enter the coefficients for variables 2: 2000
# Enter the coefficients for variables 3: 2000
# Enter the data for the square matrix stating the constraint.
# You will be asked for each row individually.
# Separate each value by a space.
# For example: 2 1 8
# Enter the data for row 1: 2 1 8
# Enter the data for row 2: 4 2 0
# Enter the data for row 3: 5 4 3
# Enter the constraint limit for constraint 1: 300
# Enter the constraint limit for constraint 2: 200
# Enter the constraint limit for constraint 3: 200
# 
# | SUPPLY | CONSTRAINT1 | CONSTRAINT2 | CONSTRAINT3 | PROFIT |
# ================================================================
# 
# | Variable 1 |      2.0|      1.0|      8.0|      3000.0|
# | Variable 2 |      4.0|      2.0|      0.0|      2000.0|
# | Variable 3 |      5.0|      4.0|      3.0|      2000.0|
# 
# | AVAIL. |      300.0|      200.0|      200.0| 
# 
# The optimal solution is: [ 91.66666667 -83.33333333  25.        ]
# Would you like to quit? (y/n): 