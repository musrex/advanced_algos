import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('speed.csv')

# plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['Array Size'], df['Speed of Execution'], marker='o')
plt.title('Array Size vs Speed of Execution')
plt.xlabel('Array Size (in thousands)')
plt.ylabel('Speed of Execution')
plt.grid(True)
plt.show()