import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a Line Plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label="Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple Line Plot in Matplotlib")
plt.legend()
plt.savefig('plot.png')
