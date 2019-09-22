#!/usr/bin/env python
#coding: utf-8

L=["test.email+alex@leetcode.com", "test.email@leetcode.com"]

X = []
for s in L:
    # step1
    d=""
    index=s.find('@')
    domainName = s[index:len(s)]
    d += domainName

    # step2
    x=""
    for i in s:
        if i == ".":
            continue
        elif i == "+" or i == "@":
            break
        x += i

    # step3
    all = x + d
    X.append(all)

print X
print len(set(X))
