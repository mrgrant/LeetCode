#
# @lc app=leetcode id=915 lang=python
#
# [915] Partition Array into Disjoint Intervals
#

# @lc code=start
class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        max_left = float("-inf")
        min_right = float("inf")
        min_index = []
        i = 0
        j = len(nums) - 1
        while i < j:
            max_left = max(max_left, nums[i])
            if nums[j] < min_right:
                min_right = nums[j]
                min_index.append([j, nums[j]])
            if max_left <= min_right:
                j -= 1
            else:
                while max_left > min_right:
                    arr = min_index.pop()
                    j = arr[0]
                    min_right = min_index[-1][1]
                    while i < j:
                        max_left = max(max_left, nums[i])
                        i += 1
        return i + 1 

        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    a = obj.partitionDisjoint([5,0,3,8,6])

