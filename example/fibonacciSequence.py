#!/usr/local/bin/python3

def fibonacciSequence(number):
    'Calculates fibonacci sequence that length equal number + 2'
    fibs = [0, 1]
    for i in range(8):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs

num = 8
result = fibonacciSequence(num)
print(fibonacciSequence.__doc__)
print(result)
