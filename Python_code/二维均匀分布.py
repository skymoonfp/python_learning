#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.arange(0, 1, 0.01)
y = np.arange(0, 1, 0.01)
X, Y = np.meshgrid(x, y)
Z1 = 1
Z2 = 0
surf = ax.plot_surface(X, Y, Z1, color='b')
surf = ax.plot_surface(X, Y, Z2, color='r')

plt.show()

print('\n')
input('Please press Enter to exit!')
