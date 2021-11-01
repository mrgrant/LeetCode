#
# @lc app=leetcode id=71 lang=python
#
# [71] Simplify Path
#

# @lc code=start
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        pathList = path.split("/")
        for s in pathList:
            if not s or s == ".":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return "/" + "/".join(stack)
                

# @lc code=end

