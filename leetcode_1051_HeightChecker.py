#!/usr/bin/env python
#coding: utf-8

class Solution(object):
    def heightChecker(self, heights):
        count = 0
        sortheight = sorted(heights)
        for i in range(len(heights)):
            if sortheight[i] != heights[i]:
                count += 1
        return count

n = [1,1,4,2,1,3]
ins001 = Solution().heightChecker(n)
print ins001
