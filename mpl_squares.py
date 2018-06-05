
import matplotlib.pyplot as plt


input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_value, squares, linewidth=5)

# set title and label for axis
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# set tick
plt.tick_params(axis='both', labelsize=14)

plt.show()
