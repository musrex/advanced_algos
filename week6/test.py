import numpy as np

def get_coefficients(num_var):
    coefficients = []
    for i in range(num_var):
        coef = float(input(f"Enter the coefficient for variable {i+1}: "))
        coefficients.append(coef)
    return np.array(coefficients)

def get_matrix_data(num_var):
    matrix_data = []
    for i in range(num_var):
        data = input(f"Enter the coefficients for row {i+1} (space-separated): ").split()
        matrix_data.append([float(d) for d in data])
    return np.array(matrix_data)

def get_constraint_limits(num_var):
    constraint_limits = []
    for i in range(num_var):
        limit = float(input(f"Enter the constraint limit for constraint {i+1}: "))
        constraint_limits.append(limit)
    return np.array(constraint_limits)

def compute_solution(coefficients, matrix_data, constraints):
    inverse_matrix = np.linalg.inv(matrix_data)
    return np.dot(inverse_matrix, constraints)

def main():
    print('''
~~~~~~~~~~~~~~~Welcome to the~~~~~~~~~~~~~~~~~~
~~~~~~~~Linear Programming Calculator!~~~~~~~~~
+=============================================+
|                                             |
| This program will help you find the optimal | 
| solution to a linear programming problem.   |
|                                             |
+=============================================+
    ''')

    num_var = int(input("Enter the number of variables/constraints: "))
    coefficients = get_coefficients(num_var)
    matrix_data = get_matrix_data(num_var)
    constraints = get_constraint_limits(num_var)

    solution = compute_solution(coefficients, matrix_data, constraints)

    print(f"\nThe optimal solution is: {solution}")

    quit = input("Would you like to quit? (y/n): ")
    if quit == "y":
        return

main()
