#!/usr/local/bin/python3

import fileinput

for line in fileinput.input('generator.py'):
    line = line.rstrip()
    num = fileinput.lineno()
    print('{:<50} # {:2d}'.format(line, num))
