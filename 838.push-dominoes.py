#
# @lc app=leetcode id=838 lang=python
#
# [838] Push Dominoes
#

# @lc code=start
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        stack = []
        res = []
        dominoes = list(dominoes)
        while dominoes:
            n = dominoes.pop(0)  
            stack.append(n) 
            if n == "L":
                if stack[0] != "R":
                    res += ["L" for _ in range(len(stack))]
                    stack = []
                elif stack[0] == "R":
                    i = 0
                    j = len(stack) - 1
                    while i < j:
                        stack[i] = "R"
                        stack[j] = "L"
                        i += 1
                        j -= 1
                    res += stack
                    stack = []
            elif n == "R":
                if stack[0] == ".":
                    res += stack[:len(stack)-1]
                elif stack[0] == "R":
                    res += ["R" for _ in range(len(stack)-1)]
                stack = ["R"]
        if stack:
            if stack[0] == "R":
                res += ["R" for _ in range(len(stack))]
            else:
                res += stack
        return "".join(res)
    
if __name__ == "__main__":
    obj = Solution()
    obj.pushDominoes(".L.R...LR..L..")
              
# @lc code=end

