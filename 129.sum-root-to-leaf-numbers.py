# @before-stub-for-debug-begin
from python3problem129 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ret = []
        def helper (node, num):
            if not node.left and not node.right:
                num += str(node.val)
                ret.append(int(num))
                return
            num += str(node.val)
            if node.left:
                helper(node.left, num)
            if node.right:
                helper(node.right, num)
        helper(root, "")
        return sum(ret)
# @lc code=end

