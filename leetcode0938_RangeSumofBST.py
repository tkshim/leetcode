#!/usr/bin/env python
# coding:utf-8

class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                print type(node)
                #print node.val
root = [10,5,15,3,7,18]
L = 7
R = 15
ins001 = Solution()
ins001.rangeSumBST(root, L, R)
