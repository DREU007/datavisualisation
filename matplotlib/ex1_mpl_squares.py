import matplotlib.pyplot as plt


input_values = range(1, 6)
squares = [val ** 2 for val in input_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()
