import numpy as np
import matplotlib as plt

x = 0
y = 0

tolerance = 0.001

for i in range(100):

    new_x = (6-y)/4
    new_y = (8-2*x)/3

    error = max(abs(new_x-x), abs(new_y-y))

    x = new_x
    y = new_y

    if error < tolerance:
        break

    print("Iteration", i + 1)
    print("x =", x)
    print("y =", y)
    print()
