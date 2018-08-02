class Solution:
    def isPalindrome(self, x):
        a = str(x)[::-1]
        if a == str(x):
            return True
        else:
            return False 