#
# @lc app=leetcode id=394 lang=python
#
# [394] Decode String
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        intSet = set(list("0123456789"))
    
        stack = []
        curStr = ""
        k = ""
        for c in s:
            if c == "[":
                stack.append((curStr, int(k)))
                curStr = ""
                k = ""
            elif c == "]":
                lastStr, curK = stack.pop(-1)
                curStr = lastStr + curK * curStr
            elif c in intSet:
                k += c
            else:
                curStr += c
        return curStr
            

# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    a = obj.decodeString("3[a]2[bc]")