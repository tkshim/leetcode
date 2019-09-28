#!/usr/bin/env python
#coding: utf-8

L=["test.email+alex@leetcode.com", "test.email@leetcode.com"]

X = []
for s in L:
    # step1 アットマークのインデックス番号を検索し、＠以降の文字列をゲット
    d=""
    index=s.find('@')
    domainName = s[index:len(s)]
    d += domainName
    
    #補足
    '''
    splitでも＠の前後で分割可能
    name,domain=i.split("@")
    '''

    # step2　.はスキップ、＋や＠が現れたら処理を中断
    # 上記以外は、文字列をxに代入
    x=""
    for i in s:
        if i == ".":
            continue
        elif i == "+" or i == "@":
            break
        x += i

    # step3　個別名とドメイン名を合体
    all = x + d
    X.append(all)

print X
# setにて重複排除
print len(set(X))
