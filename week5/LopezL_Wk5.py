# Worksheet 5
# Leandro Lopez
# Merrimack College, CS 2063

# m starts as double the initial size, and each time the s == m condition is met,
# m doubles, growing exponentially. s on the other hand grows one at a time
# or is decremented based on probRemove. so the limit of s, m, out paces the growth of s. 
# costy operations only occur when the condition s == m is met, which becomes even rarer
# over time due to the exponential growth, while cheap conditions occur anytime s isn't equal to m. 
# this means that we will never reach a point where the costy value is 1%.

# in the code below, I have changed the conditional statement to allow us to get 1%, 1e+00

# Initial size: 2 Prob Remove: 5 out of 100
# Costy:   95092 (1e+00%)
# Cheap:       0 (0e+00%)

from random import randrange

def test(initialSize, probRemove):
    accCheap, accCosty = 0, 0
    s = initialSize
    m = 2*s
    for i in range(100000):
        if (randrange(100) < probRemove):
            if (s > 0):
                s -= 1
        else:
            if (s == m):
            # it we comment out correct condition, and insert condition below
            # that will allow us to get 1.
            # if (s <= m):
                m = m*2
                s += 1
                accCosty += 1
            else:
                s += 1 # if we comment this out and include the next line, we can reach 0.5%
                # s = m
                accCheap += 1
    print("Initial size:", initialSize, "Prob Remove:", probRemove, "out of 100")
    print("Costy: {:7} ({:3.1}%)".format(accCosty,accCosty/(accCosty+accCheap)))
    print("Cheap: {:7} ({:3.1}%)".format(accCheap,accCheap/(accCosty+accCheap)))

def main():
    test(2, 5)
    test(10, 5)
    test(20, 1)
    test(20, 5)
    test(50, 1)
    test(50, 5)
    test(100, 1)
    test(0, 1)

if __name__ == "__main__":
    main()