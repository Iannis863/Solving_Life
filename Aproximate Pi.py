import matplotlib.pyplot as plt
import numpy as np
from Animate import ax

#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')

n = 5000

step = 5000
nr_steps = 5000
approximations = []

x = np.random.uniform(-1, 1, n)
y = np.random.uniform(-1, 1, n)
z = np.random.uniform(-1, 1, n)

circle_x = []
circle_y = []
circle_z = []

outside_circle_x = []
outside_circle_y = []
outside_circle_z = []

points_in_circle = 0

for j in range(nr_steps):
    extra_x = np.random.uniform(-1, 1, step)
    extra_y = np.random.uniform(-1, 1, step)
    extra_z = np.random.uniform(-1, 1, step)

    for i in range(n):
        if extra_x[i]**2 + extra_y[i]**2 + extra_z[i]**2  <= 1:
            points_in_circle += 1
            circle_x.append(extra_x[i])
            circle_y.append(extra_y[i])
            circle_z.append(extra_z[i])
        else:
            outside_circle_x.append(extra_x[i])
            outside_circle_y.append(extra_y[i])
            outside_circle_z.append(extra_z[i])

    np.append(x, extra_x)
    np.append(y, extra_y)
    np.append(z, extra_z)

    ax.scatter(circle_x, circle_y, circle_z, color='red')
    ax.scatter(outside_circle_x, outside_circle_y, outside_circle_z, color='blue')
    plt.show()

    approximations.append(points_in_circle / n * 4) # *8
    n += step

xs = np.linspace(0, 1, len(approximations))
approximations = np.array(approximations)
