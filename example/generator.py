#!/usr/local/bin/python3

def generator():
    i = 0
    while i < 10:
        print('start')
        yield i
        i += 1
        print('end')

ge = generator()

print(next(ge))
print(next(ge))
