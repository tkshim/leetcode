#!/usr/bin/env python
#coding:utf-8

L = [-4,-1,0,3,10]
l = [-7,-3,2,3,11]

def sortedSquare(l):
    A = [i*i for i in l]
    A.sort()
    return A

print sortedSquare(l)
