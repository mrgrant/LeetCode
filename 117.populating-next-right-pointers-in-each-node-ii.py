#
# @lc app=leetcode id=117 lang=python
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        head = root
        while root:
            curNode = Node(0)
            dummy = curNode
            while root:
                if root.left:
                    curNode.next = root.left
                    curNode = curNode.next
                if root.right:
                    curNode.next = root.right
                    curNode = curNode.next
                root = root.next
            root = dummy.next
        return head

        
# @lc code=end

