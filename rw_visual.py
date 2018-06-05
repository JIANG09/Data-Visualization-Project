import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    
    plt.figure(dpi=128, figsize=(8, 5))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=8)
    plt.scatter(0, 0, c='green', s=10)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=10)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another runnin?(y/n):')
    if keep_running == 'n':
        break
