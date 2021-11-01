#
# @lc app=leetcode id=477 lang=python
#
# [477] Total Hamming Distance
#

# @lc code=start
import collections
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [[0, 0] for _ in range(32)]
        for num in nums:
            for bit in bits:
                bit[num & 1] += 1
                num /= 2
        res = 0
        for x, y in bits:
            res += x * y
        return res

# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    a = obj.totalHammingDistance([4, 14, 2])

