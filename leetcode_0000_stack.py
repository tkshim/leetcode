#!/usr/bin/env python
#coding: utf-8

class mystack():
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        del self.stack[-1]
        result = self.stack[-1]
        return result

ins001 = mystack()
for i in range(20):
    ins001.push(i)

print ins001.stack

for n in range(10):
    ins001.pop()

print ins001.stack

#https://www.atmarkit.co.jp/ait/articles/1908/06/news015.html
