# Worksheet 4 - Task 1 & 2
# Leandro Lopez
# Merrimack College, CS 2063

# Egyptian fraction Greedy
from math import ceil
  
# n is the numerator, d is the denominator
def egyptian(n, d):
  
    print("The Egyptian Fraction of {}/{}".format(n, d))
    ans = []
    # while numerator is not 0
    while (n > 0):
        x = ceil(d / n)          # compute the minimal larger denominator
        ans.append(x)            # hold it to the numerator list
        n, d = x * n - d, d * x  # update the remainder to n and d
    for a in ans:
        print("1/{}".format(a), end=" ")

def main():
    print("Greedy Algorithm to Compute Egytian Fractions")
    stay = True
    while stay:
        n = int(input("Enter the numerator: "))
        d = int(input("Enter the denominator: "))
        egyptian(n, d)
        stay = ("n" != (input("\nCompute another? (no to stop) ")+" ")[0])

main()

############
#  Task 1  #
############

# 5/6 = 1/2 + 1/3
# 7/15 = 1/3 + 1/8 + 1/120
# 23/34 = 1/2 + 1/6 + 1/102
# 121/321 = 1/3 + 1/23 + 1/7383
# 5/123 = 1/25 + 1/1538 + 1/4729350




############
#  Task 2  #
############
# My calculations were different from what the program returned. 
# At first they were close, but by the 4th the difference in the
# denominators was significant. I stopped at 4 because the results
# I was getting for 5 were pretty extreme.


### Program Output ###
# The Egyptian Fraction of 5/121
# 1/25 + 1/757 + 1/763309 + 1/873960180913 + 1/1527612795642093385023488


### Manual Calculations ###
# First fraction: 1/25
# 5/121, => 121/5 = 24.5, round up => 25, 1/25

# Second fraction: 1/757
# 5/121 - 1/25 = (525 - 1121) / (121*25) = (125 - 121) / 3025 = 4/3025
# 4/3025, => 3025/4 = 756.25, round up => 757, 1/757

# Third fraction: 1/763313
# 4/3025 - 1/757 = 2047/1562500000
# 2047/1562500000, => 1562500000/2047 = 763312.16, round up => 763313, 1/763313

# Fourth fraction: 1/714285714286
# 2047/1562500000 - 1/763313 = 7/5000000000000
# 7/5000000000000, => 5000000000000/7 = 714285714285.7142, round up = 714285714286, 1/714285714286

