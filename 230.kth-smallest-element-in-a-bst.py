#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.rank = 0
        self.ret = 0
        def helper(root, k):
            if not root:
                return
            helper(root.left, k)
            self.rank += 1
            if self.rank == k:
                self.ret = root.val
                return
            helper(root.right, k)
        helper(root, k)
        return self.ret
            

        
# @lc code=end

