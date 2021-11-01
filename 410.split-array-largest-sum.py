#
# @lc app=leetcode id=410 lang=python
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # 由于题目的返回要求：返回最小和的值
        # 最小和必然落在 [max(nums), sum(nums)] 之间
        # 我们可以使用二分来进行查找
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            # 淘汰算法
            # 我们由前向后对nums进行划分，使其子数组和 <= mid，然后统计满足条件的数组数量
            # 若我们选的sum值过小，则满足条件的数量 > m，目标值应落在 [mid+1, high]
            # 若我们选的sum值过大，则满足条件的数量 < m，目标值应落在 [low, mid-1]
            count = 0
            sub_sum = 0
            for i in range(len(nums)):
                sub_sum += nums[i]
                if sub_sum > mid:
                    count += 1
                    sub_sum = nums[i]
            # 注意：末尾还有一个子数组我们没有统计，这里把它加上
            count += 1
            if count > m:
                low = mid + 1
            else:
                high = mid
        return low        
# @lc code=end

