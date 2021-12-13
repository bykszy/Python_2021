import random
import numpy as np


def bubble_sort(numbers):
    is_changed = True

    while is_changed:
        is_changed = False
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                tmp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = tmp
                is_changed = True


if __name__ == '__main__':
    random_numbers = []
    for j in range(50):
        random_numbers.append(random.random())
    std_sorting = sorted(random_numbers, reverse=True)
    bubble_sort(random_numbers)

    if np.allclose(random_numbers, std_sorting):
        print("OK")
        print(f"Sorted numbers: {random_numbers}")
    else:
        print("Something bad happened")
