#
# @lc app=leetcode id=537 lang=python
#
# [537] Complex Number Multiplication
#

# @lc code=start
class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = num1.split("+")
        n2 = num2.split("+")
        real1 = int(n1[0])
        img1 = int(n1[1][:-1])
        real2 = int(n2[0])
        img2 = int(n2[1][:-1])
        real =  real1 * real2 - img1 * img2
        img = real1 * img2 + real2 * img1
        return str(real) + "+" + str(img) + "i"

# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    
    obj.complexNumberMultiply("1+-1i", "0+0i")