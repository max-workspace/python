#!/usr/local/bin/python3

def initNameConstruct():
    data = {}
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
    return data

def addNameConstruct(data, fullName):
    names = fullName.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(fullName)
        else:
            data[label][name] = [fullName]

def lookup(data, label, name):
    return data[label].get(name)


nameConstruct = initNameConstruct()
addNameConstruct(nameConstruct, 'Magnus Lie Hetland')
result = lookup(nameConstruct, 'middle', 'Lie')
print(result)
