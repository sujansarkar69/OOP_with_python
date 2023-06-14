import numpy as np
import matplotlib.pyplot as plt

data = [[12, 25, 10, 20, 13],
        [20, 23, 21, 17, 25],
        [25, 22, 17, 19, 15]]
x = np.arange(5)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(x + 0.00, data[0], color='r', width=0.25)
ax.bar(x + 0.25, data[1], color='g', width=0.25)
ax.bar(x + 0.50, data[2], color='b', width=0.25)
plt.show()
