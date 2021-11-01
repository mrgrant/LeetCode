#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#

# @lc code=start
import collections
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        d = collections.defaultdict(int)
        d[0] = 1
        for n in nums:
            temp = collections.defaultdict(int)
            for key in d:
                sum = key
                cnt = d[key]
                temp[sum-n] += cnt
                temp[sum+n] += cnt
            d = temp
        return d[target]

            
# @lc code=end
if __name__  == "__main__":
    obj = Solution()
    obj.findTargetSumWays([1,1,1,1,1], 3)
