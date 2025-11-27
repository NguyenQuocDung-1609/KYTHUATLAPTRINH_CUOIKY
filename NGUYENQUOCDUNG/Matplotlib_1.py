import matplotlib.pyplot as plt

x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]
z = [3,5,9]
labels = z

# Line plot
plt.subplot(2, 2, 1)
plt.plot(x, y, color='red')
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

# Bar chart
plt.subplot(2, 2, 2)
plt.bar(x, y, color='green')
plt.title("Bar Chart")
plt.xlabel("X values")
plt.ylabel("Y values")

# Pie chart
plt.subplot(2, 2, 3)
plt.pie(z,labels=labels)
plt.title("Pie Chart")

# Scatter plot
plt.subplot(2, 2, 4)
plt.scatter(x, y, color='orange')
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.tight_layout()
plt.show()
