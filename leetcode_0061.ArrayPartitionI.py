#!/usr/bin/env python
#coding: utf-8

'''
n=0
Z=[]
while n < N:
    x = 2 * n
    Z.append(L[x:x+2])
    n += 1
print Z
'''

def minsum(L):
    #数字を昇順にソート
    L.sort()
    #レングスを２で割って分割数を求める
    N = len(L)/2
    n = 0
    #合計値
    sum = 0
    while n < N:
        #0,2,4,6,8〜の行列を作成
        x = 2 * n
        #最小値、つまりindexの偶数の値を合計
        sum += L[x]
        n += 1
    return sum
L = [1,4,3,2,5,6]
print minsum(L)
