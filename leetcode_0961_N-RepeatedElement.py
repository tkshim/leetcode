#!/usr/bin/env python
#coding:utf-8
import collections
'''
もっとも頻出が高い値を計算する
Counterのmost_commonで頻出頻度で並び変え、一個目のvalueを取り出す。
most_commonのoutputはtuple型になっている
'''
def repeatedNTimes(A):
    c = collections.Counter(A)
    for i in c.most_common(1):
        return i[0]

print repeatedNTimes([5,1,5,2,5,3,5,4])
