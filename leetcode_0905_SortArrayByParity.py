#!/usr/bin/env python
#coding:utf-8

def checkNumber(X):
    odd = []
    even = []
    for x in X:
        if x % 2 == 0:
            odd.append(x)
        else:
            even.append(x)
    return odd + even

print checkNumber([1,2,3,4])
