#
# @lc app=leetcode id=637 lang=python
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        stack = [root]
        while stack:
            temp = []
            s = []
            for node in stack:
                s.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(float(sum(s))/float(len(s)))
            stack = temp
        return res
                
# @lc code=end

