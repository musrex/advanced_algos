# Project 3
# Leandro Lopez
# Merrimack College, CS 2063

def tribo(n) -> int:
    '''Summary of Tribo function
    This function computes the nth term of the Tribonacci sequence.
    
    input: n (int)
    output: nth term of the Tribonacci sequence (int)
    '''
    a, b, c = 1, 1, 1
    if n <= 3:
        return 1
    else:
        for i in range(3, n):
            a, b, c = b, c, a+b+c
        return c


# 1, 1, 1, 3, 5, 9, 17, 31, 57
# tribo(6) == 9


def main():
    '''Summary of main function
    This program prompts the user for an int and computes the nth term of the Tribonacci sequence.
    If the user enters a non-int, the program will print an error message and prompt the user again.
    If the user enters an int less than 1, the program will terminate.
    '''
    run = True
    while run:
        try:
            n = int(input("Enter an int: "))
            if n < 1:
                run = False
                break
            else:
                print(tribo(n))
        except:
            print("Error, please enter an int.")

if __name__ == "__main__":
    main()