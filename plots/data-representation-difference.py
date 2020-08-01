import matplotlib.pyplot as plt
import random
import numpy as np

# For reproduction
random.seed(10)

cartesianFig = plt.figure()
ax = cartesianFig.add_subplot(111)
ax.set_title("Cartesian Coordinates")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.tick_params(bottom=False)
ax.set_xticklabels([])

ax.tick_params(left=False)
ax.set_yticklabels([])

polarFig = plt.figure()
xy = polarFig.add_subplot(111)
xy.set_title("Polar Coordinates")
xy.set_xlabel("r")
xy.set_ylabel(r"$\theta$")

xy.tick_params(bottom=False)
xy.set_xticklabels([])

xy.tick_params(left=False)
xy.set_yticklabels([])


innerCircle = 30
outerCircle = 100
offset = 10

for i in range(100):
    theta = random.uniform(0, 2 * np.pi)
    r = random.randint(0, innerCircle)
    
    x = r
    y = theta
    xy.plot(x, y, "+", 'b')
    ax.plot(r * np.cos(theta), r * np.sin(theta), "+")

for i in range(200):
    theta = random.uniform(0, 2 * np.pi)
    r = random.randint(innerCircle + offset, outerCircle)
    
    x = r
    y = theta
    xy.plot(x, y, "x")
    ax.plot(r * np.cos(theta), r * np.sin(theta), "x")


cartesianFig.savefig("cartesian.pdf", bbox_inches='tight')
polarFig.savefig("polar.pdf", bbox_inches='tight')
