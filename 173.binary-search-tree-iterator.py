#
# @lc app=leetcode id=173 lang=python
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.arr = []
        self.dfs(root)
        

    def next(self):
        """
        :rtype: int
        """
        return self.arr.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.arr) != 0
    
    def dfs(self, node):
        if not node:
            return 
        self.dfs(node.left)
        self.arr.append(node.val)
        self.dfs(node.right)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

