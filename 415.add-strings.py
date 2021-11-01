#
# @lc app=leetcode id=415 lang=python
#
# [415] Add Strings
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0 for _ in range(max(len(num1), len(num2)) + 1)]
        num1 = num1[::-1]
        for i in range(len(num1)):
            res[i] = ord(num1[i]) - ord('0')
        num2 = num2[::-1]
        for i in range(len(num2)):
            res[i] += ord(num2[i]) - ord('0')
        for i in range(len(res)-1):
            add = res[i] // 10
            res[i] = res[i] % 10
            res[i+1] += add
        while res[-1] == 0 and len(res) > 1:
            res.pop()
        res = [str(i) for i in res]
        return "".join(res)[::-1]
# @lc code=end

