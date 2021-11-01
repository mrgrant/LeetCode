#
# @lc app=leetcode id=10 lang=python
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.m = len(s)
        self.n = len(p)
        self.d = {}
        def dp(s, i, p, j):
            if j == self.n:
                return i == self.m
            if i == self.m:
                if (self.n - j) % 2 == 1:
                    return False
                while j + 1 < self.n:
                    if p[j+1] != "*":
                        return False
                    j += 2
                return True
            key = str(i) + "," + str(j)
            if key in self.d:
                return self.d[key]
            res = False
            if s[i] == p[j] or p[j] == ".":
                if j < self.n - 1 and p[j+1] == "*":
                    res =  dp(s, i+1, p, j) or dp(s, i, p, j+2)
                else:
                    res =  dp(s, i+1, p, j+1)
            else:
                if j < self.n - 1 and p[j+1] == "*":
                    res =  dp(s, i, p, j+2)
                else:
                    res = False
            self.d[key] = res
            return res
        return dp(s, 0, p, 0)


# @lc code=end

