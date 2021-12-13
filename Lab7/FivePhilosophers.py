import threading
import time
import random


class Philosopher(threading.Thread):
    def __init__(self, number, leftfork, rightfork):
        super().__init__()
        self.number = number + 1
        self.leftfork = leftfork
        self.rightfork = rightfork

    def try_eating(self):
        self.leftfork.acquire()
        self.rightfork.acquire()

        print(f"Philosopher number {self.number} started eating ")
        time.sleep(1)
        print(f"Philosopher number {self.number} stopped eating ")

        self.leftfork.release()
        self.rightfork.release()

    def run(self):
        while True:
            print(f"Philosopher number {self.number} is contemplating about eating ")
            time.sleep(random.randint(1, 5))
            self.try_eating()


if __name__ == '__main__':
    fork = [threading.Condition(threading.Lock()) for i in range(5)]
    philosophers = [Philosopher(i, fork[i], fork[(i + 1) % 5]) for i in range(5)]

    for philosopher in philosophers:
        philosopher.start()
