#
# @lc app=leetcode id=515 lang=python
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        def helper(node, level):
            if not node:
                return
            if len(res) == level:
                # write the first node
                res.append(node.val)
            else:
                res[level] = max(res[level], node.val)
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root, 0)
        return res

# @lc code=end

