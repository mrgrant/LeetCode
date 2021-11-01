class Solution(object):
    # def canPartitionKSubsets(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     """
    #     if sum(nums) % k:
    #         return False 
    #     if k == 1:
    #         return True
    #     nums = sorted(nums)
    #     nums = nums[::-1]
    #     target = sum(nums) // k
    #     if nums[0] > target:
    #         return False
    #     bucket = [0 for _ in range(k)]
        
    #     def backtrack(nums, index, bucket):
    #         if index == len(nums):
    #             for b in bucket:
    #                 if b != target:
    #                     return False
    #             return True
    #         for i in range(len(bucket)):
    #             if nums[index] + bucket[i] > target:
    #                 continue
    #             bucket[i] += nums[index]
    #             if backtrack(nums, index+1, bucket):
    #                 return True
    #             bucket[i] -= nums[index]
    #     return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k:
            return False 
        if k == 1:
            return True
        nums = sorted(nums)
        nums = nums[::-1]
        target = sum(nums) // k
        if nums[0] > target:
            return False
        used = [False for _ in range(len(nums))]
        
        def backtrack(nums, index, bucket, used, k):
            if k == 0:
                return True
            if bucket == target:
                return backtrack(nums, 0, 0, used, k-1)
            for i in range(index, len(nums)):
                if used[i]:
                    continue
                if bucket + nums[i] > target:
                    continue
                bucket += nums[i]
                used[i] = True
                if backtrack(nums, i+1, bucket, used, k):
                    return True
                bucket -= nums[i]
                used[i] = False
            return False
        return backtrack(nums, 0, 0, used, k)

if __name__ == "__main__":
    obj = Solution()
    obj.canPartitionKSubsets([4,3,2,3,5,2,1], 4)