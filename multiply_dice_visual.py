from die import Die

import pygal

# create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

# roll the dice many times and keep the results in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize
hist = pygal.Bar()

hist.title = "Results of multiplying a D6 and a D10 50,000 times"
hist.x_labels = []
for i in range(1, max_result+1):
    hist.x_labels.append(str(i))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D10', frequencies)
hist.render_to_file('multiply_dice_visual.svg')
