#!/usr/bin/env python
#coding: utf-8
from collections import deque

history = deque(maxlen=100)
lines = open("python.txt")
for line in lines:
    if 'python' in line:
        print lines
    history.append(line)
print history
