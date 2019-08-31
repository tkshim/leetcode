#!/usr/bin/env python
#!coding: utf-8

import collections

A = 'A'
B = 'B'
C = 'B'
D = 'D'
E = 'E'

X = [A,B,C,D,E]
c = collections.Counter(X)
print c
print len(c)
