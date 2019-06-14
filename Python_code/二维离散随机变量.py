#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]):
    xs = np.arange(20)
    ys = np.random.rand(20)

    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

# 例子
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
dx = 0.3
dy = 0.3
dz = [0.02, 0.025, 0.35, 0.1, 0.15, 0.04, 0.25, 0.04, 0.025]
zpos = 0
i = 0
for xpos in [1, 2, 3]:
    for c, ypos in zip(['r', 'y', 'g'], [-1, 0, 1]):
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz[i], color=c)
        i = i + 1

ax.set_xlabel('SmokingLevel')
ax.set_ylabel('HealthLevel')
ax.set_zlabel('PopulProportion')

plt.show()

print('\n')
input('Please press Enter to exit!')
