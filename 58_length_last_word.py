class Solution:
    def lengthOfLastWord(self, s):
        temp = s.split()
        if len(temp) == 0:
            return 0 
        else:
            return len(temp[-1])
