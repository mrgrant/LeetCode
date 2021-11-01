#
# @lc app=leetcode id=659 lang=python
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start
import collections
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = collections.defaultdict(int)
        need = collections.defaultdict(int)
        for n in nums:
            freq[n] += 1
        for n in nums:
            if freq[n] == 0:
                continue
            if need[n] > 0 and freq[n] > 0:
                need[n] -= 1
                freq[n] -= 1
                need[n+1] += 1
            elif freq[n] >= 1 and freq[n+1] >= 1 and freq[n+2] >= 1:
                freq[n] -= 1
                freq[n+1] -= 1
                freq[n+2] -= 1
                need[n+3] += 1
            else:
                return False
        return True
         
# @lc code=end

