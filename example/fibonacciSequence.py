#!/usr/local/bin/python3

fibs = [0, 1]
num = 8
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)
