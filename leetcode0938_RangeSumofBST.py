#!/usr/bin/env python
# coding:utf-8

class Solution(object):
    def rangeSumBST(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans
        
root = [10,5,15,3,7,18]
L = 7
R = 15
ins001 = Solution()
ins001.rangeSumBST([10,5,15,3,7,18], L, R)
