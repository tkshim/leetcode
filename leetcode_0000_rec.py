#!/usr/bin/env python
#coding: utf-8

#再起呼び出し


# Nを1までSumする
def rec(n):
    if n < 1:
        return n
    return n + rec(n-1)

print rec(3)
#https://techacademy.jp/magazine/19308

##フィボナッチ数計算
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

print fib(3)
#https://qiita.com/WestRiver/items/690ba23866c0a473319c
