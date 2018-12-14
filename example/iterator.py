#!/usr/local/bin/python3

class iter:

    nums = None

    def __init__(self):
        self.nums = 0

    def __next__(self):
        self.nums += 1
        return self.nums

t = iter()
print(next(t))
print(next(t))
print(next(t))
