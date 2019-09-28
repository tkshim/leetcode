#!/usr/bin/env python
#coding: utf-8

#
print (lambda price:price * 1.1)(100)

#
message = lambda a:a 
print message('Hello World')

#
print (lambda price:price > 1.1)(100)

#
tax = lambda c :  c * 1.1
p = [10,100,1000]
print map(tax, p)

def tax2(d):
    return d * 1.1
print map(tax2, p)
