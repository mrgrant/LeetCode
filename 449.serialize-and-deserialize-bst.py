#
# @lc app=leetcode id=449 lang=python
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def recursive(root):
            if root is None:
                self.ret.append("#,")
                return
            self.ret.append(str(root.val)+",")
            recursive(root.left)
            recursive(root.right)
        self.ret = []
        recursive(root)
        return "".join(self.ret)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")

        def recursive(nodes):
            if not nodes:
                return None
            node = nodes.pop(0)
            if node == "#":
                return None
            root = TreeNode(int(node))
            root.left = recursive(nodes)
            root.right = recursive(nodes)
            return root
        return recursive(nodes)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end
if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    ser = Codec()
    deser = Codec()
    tree = ser.serialize(root)
    ans = deser.deserialize(tree)


