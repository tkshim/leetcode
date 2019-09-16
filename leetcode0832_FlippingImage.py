#!/usr/bin/env python
#coding:utf-8

Z=[]
X = [[1,1,0],[1,0,1],[0,0,0]]

# 数値変換の関数
def flip(n):
    if n == 0:
        return 1
    else:
        return 0

def mapped(x):
    for i in x:
        Z.append(map(flip,i))
    return Z

print 'mappedの結果：　 ', mapped(X)

def mapped2(x):
    return [map(flip,i) for i in x]

print 'mapped2の結果：　', mapped2(X)

'''
指定した文字列の削除
Y.remove('B')

指定したインデックスの削除
del Y[0:2]

文字列を変換
X = [[1,1,0],[1,0,1],[0,0,0]]
Y = ['A','B','C']
Z = []

print Y
for i in X:
    for m in i:
        mod = str(m).replace('0','1')
        Z.append(mod)
print Z
'''
