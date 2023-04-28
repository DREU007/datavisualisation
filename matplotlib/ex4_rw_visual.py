import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()

    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values, rw.y_values,
        c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=10
    )

    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(
        rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100
    )

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_title('Random Walk', fontsize=24)
    # ax.set_xlabel('X coordinate', fontsize=14)
    # ax.set_ylabel('Y coordinate', fontsize=14)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
