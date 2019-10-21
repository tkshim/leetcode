#!/usr/bin/env python
#coding: utf-8

s1 = "(()())(())"
s2 = "(())"
s3 = "()()"

count = 0
first = 0
res = ""
for i in range(len(s3)):
    print "s3 is : ", s3[i]
    if s3[i] == "(":
        count +=1
    else:
        count -= 1
    if(count == 0):
        res +=(s3[first+1:i])
        print "res is: ", res
        first = i+1
print count