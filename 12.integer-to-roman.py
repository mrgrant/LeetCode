#
# @lc app=leetcode id=12 lang=python
#
# [12] Integer to Roman
#

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {1:'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res = []
        times = 1
        while num > 0:
            mod = num % 10
            if mod == 4:
                res.append(roman[1*times]+roman[5*times])
            elif mod == 9:
                res.append(roman[1*times]+roman[10*times])
            elif 0 < mod < 4:
                res.append(roman[1*times]*mod)
            elif 5 <= mod < 9:
                res.append(roman[5*times]+roman[1*times]*(mod-5))
            num /= 10
            times *= 10
        return "".join(res[::-1])  
            


# @lc code=end

