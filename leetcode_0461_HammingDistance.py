#!/usr/bin/env python
#coding: utf-8

'''
1= 000
2= 010
3= 011
4= 100
5= 101
6= 110
7= 111
'''

c=0
x=2
y=3
while x or y:
    X = (x & 1) 
    Y = (y & 1)
    print X,Y
    if X ^ Y:
        c += 1
    x >>= 1
    y >>= 1
print c

