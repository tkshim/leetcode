#!/usr/sortArrayByParityIIbiSolutionn/env python
#!coding: utf-8

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        #愚数、奇数、返り値のリストを用意する
        O=[]
        E=[]
        X=[]
        
        # %は任意の数で割った余りを示す
        # 偶数と奇数の箱に分ける。
        for i in A:
            if i % 2 == 0:
                O.append(i)
            else:
                E.append(i)
        # 偶数と奇数のリストから順番に値を取り出す。
        for n in range(len(A)/2):
            X.append(O[n])
            X.append(E[n])
            
        return X

ins001 = Solution()
print ins001.sortArrayByParityII([4,2,5,7])
