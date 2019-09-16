#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:48:07 2019

@author: ecrespo
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange (1,11)
print(x)
y = np.random.randn(10)
plt.plot(x,y)
plt.plot(x,y--2)
plt.show()