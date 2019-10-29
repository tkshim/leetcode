#!/usr/bin/env python
#coding: utf-8

#
#　考え方
#　Rだと１進む。Lだと−１進む。
#　同じ回数だけ出現すると言う事は、合計が０になるはずである。
#　よって、カウンターが0になった時に合致した回数finalが１となる。
#
#
#

class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        final = 0
        for i in s:
            if i == 'R':
                count += 1
            else:
                count -= 1
            if count == 0:
                final += 1
        return final

s = 'RLLLLRRRLR'

instance01 = Solution()
print instance01.balancedStringSplit(s)
