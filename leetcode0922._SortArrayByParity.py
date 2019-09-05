#!/usr/bin/env python
#!coding: utf-8

A = [6,3,4,5]
O = []
E = []
X = []
for i in A:
    print i
    if i % 2 == 0:
        O.append(i)
    else:
        E.append(i)
print O,E
for x in range(len(A)/2):
    print x
    X.append(O[x])
    X.append(E[x])

print X
