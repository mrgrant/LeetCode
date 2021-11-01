#
# @lc app=leetcode id=398 lang=python
#
# [398] Random Pick Index
#

# @lc code=start
import collections
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d = collections.defaultdict(list)
        for i, n in enumerate(nums):
            self.d[n].append(i)
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.d[target])
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

