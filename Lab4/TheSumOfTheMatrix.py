import numpy as np


x = 128
y = 128
a = np.random.rand(x, y)
b = np.random.rand(x, y)
new_array = np.zeros((x, y))
for i in range(x):
    for j in range(y):
        new_array[i, j] = a[i, j] + b[i, j]

if np.allclose(new_array, np.add(a, b)):
    print("OK")
    print(new_array)
else:
    print("Something bad happened")
