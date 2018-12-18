#!/usr/local/bin/python3
#python3 templates.py ../txt/magnus.txt ../txt/template.txt

import fileinput, re

def replacement(match):
    code = match.group(1)
    try:
        print(code)
        return str(eval(code, scope))
    except SyntaxError:
        print(code)
        exec(code, scope)
        return ''

field_pat = re.compile(r'\[(.+?)\]')
scope = {}
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

print(field_pat.sub(replacement, text))

