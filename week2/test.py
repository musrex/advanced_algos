import matplotlib.pyplot as plt
import numpy as np

# input sizes
n = np.linspace(1, 100, 100)

# calculate time complexities
constant = np.ones_like(n)
logarithmic = np.log(n)
linear = n
linearithmic = n * np.log(n)
quadratic = n**2

# plot the complexity classes
plt.figure(figsize=(10, 6))

# modified to increase linewidth and add linestyle
plt.plot(n, constant, label='O(1)', linewidth=2, linestyle='-')
plt.plot(n, logarithmic, label='O(log n)', linewidth=2, linestyle='--')
plt.plot(n, linear, label='O(n)', linewidth=2, linestyle='-.')
plt.plot(n, linearithmic, label='O(n log n)', linewidth=2, linestyle=':')
plt.plot(n, quadratic, label='O(n^2)', linewidth=2, linestyle='-.')

plt.xlabel('Input Size (n)', fontsize=14)
plt.ylabel('Time Complexity', fontsize=14)
plt.legend(loc='upper left')
plt.title('Comparison of Complexity Classes', fontsize=16)
plt.grid(True)
plt.show()
