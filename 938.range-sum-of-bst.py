#
# @lc app=leetcode id=938 lang=python
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        res = []
        def dfs(node):
            if not node:
                return 
            if low <= node.val <= high:
                res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return sum(res)
# @lc code=end

