import matplotlib.pyplot as plt

x_values= list(range(1,5001))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=30)

plt.title("Cube of 5000 Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of value", fontsize=14)

plt.tick_params(axis="both", which='major', labelsize=14)

plt.savefig('cubes_5000num_plot', bbox_inches='tight')
