import numpy as np
import random


x = 8
y = 8
a = np.random.rand(x, y)
b = np.random.rand(x, y)
new_array = np.zeros((x, y))

for i in range(a.shape[0]):
    for j in range(b.shape[1]):
        for k in range(b.shape[0]):
            new_array[i, j] += a[i, k] * b[k, j]

if np.allclose(new_array, np.array(a) @ np.array(b)):
    print("OK")
    print(new_array)
else:
    print("Something bad happened")
