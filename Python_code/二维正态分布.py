#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pylab import *

s1, s2, m1, m2, r = map(float, input('请依次输入二维正态分布的五个参数(s1,s2,m1,m2,r)： ').split())
x = np.linspace(-10, 10, 200)
y = x
X, Y = meshgrid(x, y)
Z = bivariate_normal(X, Y, s1, s2, m1, m2, r)
fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='RdGy')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

print('\n')
input('Please press Enter to exit!')
