import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 100, 0, 10])

for i in range(100):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()