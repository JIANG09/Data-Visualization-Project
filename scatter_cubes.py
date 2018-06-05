import matplotlib.pyplot as plt

x_values = list(range(1,6))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, s=45)


plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of value", fontsize=14)

plt.tick_params(axis="both", which='major', labelsize=14)


plt.show()
