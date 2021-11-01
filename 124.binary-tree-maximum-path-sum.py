#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float("-inf")
        def oneside(node):
            if not node:
                return 0
            left = max(0, oneside(node.left))
            right = max(0, oneside(node.right))
            self.res = max(self.res, node.val + left + right)
            return max(left, right) + node.val
        oneside(root)
        return self.res
# @lc code=end

