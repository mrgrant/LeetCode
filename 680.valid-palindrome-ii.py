#
# @lc app=leetcode id=680 lang=python
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                left = s[i:j]
                right = s[i+1:j+1]
                return left == left[::-1] or right == right[::-1]
            i += 1
            j -= 1
        return True

# @lc code=end
if __name__ == "__main__":
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    obj = Solution()
    a = obj.validPalindrome(s)
