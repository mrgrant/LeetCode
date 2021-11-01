#
# @lc app=leetcode id=1022 lang=python
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node, s):
            if not node.left and not node.right:
                self.res += (s << 1) + node.val
                return 
            if node.left:
                dfs(node.left, (s << 1) + node.val)
            if node.right:
                dfs(node.right, (s << 1) + node.val)
        dfs(root, 0)
        return self.res

        
# @lc code=end

