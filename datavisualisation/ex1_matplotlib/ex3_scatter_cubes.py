import matplotlib.pyplot as plt


x_values = range(1, 5000)
y_values = [x ** 3 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Greens, s=20)
ax.axis([0, 6000, 0, 140_000_000_000])

plt.show()
