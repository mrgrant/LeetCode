#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = []
        while columnNumber > 0:
            mod = columnNumber % 26
            if mod == 0:
                res.append('Z')
                columnNumber = (columnNumber - 26) // 26
            else:
                res.append(chr(ord('A') + mod - 1))
                columnNumber = columnNumber // 26
        return "".join(res)[::-1]
        
# @lc code=end

