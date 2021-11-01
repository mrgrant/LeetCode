#
# @lc app=leetcode id=606 lang=python
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        s = ""
        def preorder(node):
            if not node:
                return ""
            if node.right:
                return str(node.val) + "(" + preorder(node.left) + ")" + "(" + preorder(node.right) + ")"
            elif node.left:
                return str(node.val) + "(" + preorder(node.left) + ")"
            else:
                return str(node.val)
        return preorder(root)
# @lc code=end

