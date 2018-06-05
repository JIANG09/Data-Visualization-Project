from die import Die

import pygal

# create three D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# roll the dice many times and keep the results in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize
hist = pygal.Bar()

hist.title = "Results of rolling three D6 50,000 times"
hist.x_labels = []
for i in range(3, max_result+1):
    hist.x_labels.append(str(i))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('three D6', frequencies)
hist.render_to_file('3D6_dice_visual.svg')
