import random

class Queue:
    def __init__(self):
        self.a_in = []
        self.a_out = []

    def enqueue(self, d):
        self.a_in.append(d)

    def dequeue(self):
        if (self.a_out == []):
            self.a_out = self.a_in[::-1]
            self.a_in = []
        return self.a_out.pop()
    
def get_ratios():
    '''Summary of get_ratios function
    This function takes in a ratio from the user and returns the enqueue and dequeue ratios.
    The enqueue ratio must be between 0.34 and 0.66.
    '''
    while True:
        enqueue_ratio = float(input("Enter the enqueue ratio: "))
        if 0.34 <= enqueue_ratio <= 0.66:
            return enqueue_ratio, 1 - enqueue_ratio
        else:
            print("The ratio must be between 0.34 and 0.66. Please try again.")

def main():
    enqueue_ratio, dequeue_ratio = get_ratios()
    queue = Queue()

    costy = 0
    cheap = 0

    for _ in range(100000):
        operation = random.choices(['enqueue', 'dequeue'], [enqueue_ratio, dequeue_ratio], k=1)[0]

        if operation == 'enqueue':
            queue.enqueue(random.randint(1, 100))
        else:
            if queue.a_out == [] and queue.a_in != []:
                costy += 1
            if queue.a_out != [] or queue.a_in != []:
                queue.dequeue()

        cheap += 1


    print(f'''Costy operations: {costy}
Cheap operations: {cheap}''')

if __name__ == "__main__":
    main()