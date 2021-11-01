#
# @lc app=leetcode id=863 lang=python
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def constructBinaryTree(elemList):
    # generate leetcode type of binary tree
    # :param elemList: leetcode unit test (hierachy form)
    # :return: root node
    # sample: constructBinaryTree([3,9,20,None,None,15,7])
    length = len(elemList)
    if(length == 0):
        return None
    _root = TreeNode(elemList[0])
    def recr(root, num):
        # num: number of node, start by 0 (root)
        leftNumber = 2*num+1
        rightNumber = 2*num+2
        if(leftNumber < length and elemList[leftNumber] != None):
            root.left = TreeNode(elemList[leftNumber])
            recr(root.left, leftNumber)
        else:
            root.left = None
        if(rightNumber < length and elemList[rightNumber] != None):
            root.right = TreeNode(elemList[rightNumber])
            recr(root.right, rightNumber)
        else:
            root.right = None
    recr(_root, 0)
    return _root

import collections
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        conn = collections.defaultdict(list)
        def dfs(node, child):
            if node and child:
                conn[node.val].append(child.val)
                conn[child.val].append(node.val)
            if child.left:
                dfs(child, child.left)
            if child.right:
                dfs(child, child.right)
            return 
        dfs(None, root)
        stack = [target]
        visit = set(stack)
        for i in range(k):
            temp = []
            for root in stack:
                for node in conn[root]:
                    if node not in visit:
                        temp.append(node)
                        visit.add(node)
            stack = temp
        return stack

# @lc code=end

if __name__ == "__main__":
    null = None
    tree = constructBinaryTree([3,5,1,6,2,0,8,null,null,7,4])
    obj = Solution()
    a = obj.distanceK(tree, 5, 2)
    print(a)
