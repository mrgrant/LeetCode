#
# @lc app=leetcode id=1328 lang=python
#
# [1328] Break a Palindrome
#

# @lc code=start
class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" +palindrome[i+1:]
        return palindrome[:len(palindrome) - 1] + "b"
        
# @lc code=end

