#!/usr/bin/env python
#!coding: utf-8

import collections

A = 'A'
B = 'A'
C = 'C'
D = 'C'
E = 'E'

X = [A,B,C,D,E]

n = 0
LIST=[]

for i in range(len(X)-1):
    print 'A is : ', X[n]
    source = X[n]
    print 'X list is : ', X[n+1:]
    target = X[n+1:]
    for i in target:
        if source == i:
            print 'bingo'
            LIST.append(i)
    n += 1
c = collections.Counter(LIST)
print c
print len(c)
