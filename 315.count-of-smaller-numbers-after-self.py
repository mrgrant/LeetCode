#
# @lc app=leetcode id=315 lang=python
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.res = [0 for _ in range(len(nums))]
        arr = []
        for i, n in enumerate(nums):
            arr.append((n, i))
        self.mergeSort(arr)
        return self.res


    def merge(self, left, right):
        out = []
        rLess = 0
        i = j = 0
        while i < len(left) and j < len(right):
            if right[j][0] < left[i][0]:
                out.append(right[j])
                rLess += 1
                j += 1
            else:
                out.append(left[i])
                self.res[left[i][1]] += rLess
                i += 1 
        while i < len(left):
            out.append(left[i])
            self.res[left[i][1]] += rLess
            i += 1
        while j < len(right):
            out.append(right[j])
            j += 1
        return out

    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)

# @lc code=end

