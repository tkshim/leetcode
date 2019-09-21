#!/usr/bin/env python
#conding: utf-8

#A = "IDID"
A = "III"

#Length

class solution():
    def createList(self, list):
        l=len(list)
        n=0
        X=[]
        for i in list:
            if i == "I":
                X.append(n)
                n+=1
            elif i == "D":
                X.append(l)
                l-=1
        X.append(n)
        return X

ins001 = solution()
print ins001.createList(A)
