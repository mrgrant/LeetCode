#
# @lc app=leetcode id=652 lang=python
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        dic = {}
        ret = []
        if not root:
            return ret
        
        def helper(root):
            if not root:
                return "#"
            subtree = str(root.val) + "," + helper(root.left) + "," + helper(root.right)
            if subtree not in dic:
                dic[subtree] = 1
            else:
                dic[subtree] += 1
                if dic[subtree] <= 2:
                    ret.append(root)
            return subtree
        helper(root)
        return ret
# @lc code=end

