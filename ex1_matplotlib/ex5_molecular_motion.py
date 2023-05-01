import matplotlib.pyplot as plt
from random_walk import RandomWalk


rw = RandomWalk(5000)
rw.fill_walk()

plt.style.use("bmh")
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect("equal")

ax.plot(rw.x_values, rw.y_values, linewidth=1)
plt.show()
