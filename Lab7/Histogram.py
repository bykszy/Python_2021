import concurrent.futures
import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def toss_a_coin():
    return random.randint(0, 1)


def hist(num_runs=10000):
    lotto_coupons = np.zeros(num_runs, dtype=int)
    for idx in range(num_runs):
        lotto_coupons[idx] = toss_a_coin() + toss_a_coin() + toss_a_coin() + toss_a_coin()

    c = Counter()
    for result in lotto_coupons:
        c[result] = c[result] + 1

    sort_c = {k: v for k, v in sorted(list(c.items()))}

    x_axis = list(sort_c.keys())
    y_axis = list(sort_c.values())

    return x_axis, y_axis


def run_calc():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as thread:
        th = thread.submit(hist, 10000)
    x_axis, y_axis = th.result()
    fig, ax = plt.subplots()
    ax.stem(x_axis, y_axis, use_line_collection=True)
    ax.set_title("Simulation of four coin tosses")
    plt.show()


if __name__ == '__main__':
    run_calc()