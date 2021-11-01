#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] == "0" and s[i-1] == "0":
                return 0
            if s[i] == "0" and int(s[i-1]) >= 3:
                return 0
            if s[i] == "0" or s[i-1] == 0 or int(s[i-1]+ s[i]) > 26:
                dp[i] = dp[i-1]
            elif 11 <= int(s[i-1] + s[i]) <= 26:
                if i > 1:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1] + 1
        return dp[-1]
        
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    a = obj.numDecodings("2101")