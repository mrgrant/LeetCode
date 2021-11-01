#
# @lc app=leetcode id=1235 lang=python
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start

class Solution(object):
    def binarySearch(self, job, index, eTime):
        l = 0
        r = index
        while l <= r:
            m = (l + r) // 2
            if job[m][1] <= eTime:
                if job[m+1][1] <= eTime:
                    l = m + 1
                else:
                    return m
            else:
                r = m - 1
        return -1

    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        job = [[1, 1, 0]]

        n = len(startTime)
        for i in range(n):
            job.append([startTime[i], endTime[i], profit[i]])
        job = sorted(job, key = lambda x: (x[1], x[2]))
        dp = [0 for _ in range(n+1)]
        dp[1] = job[1][2]
        curE = job[1][1]

        for i in range(1, n):
            if job[i+1][0] >=  curE:
                dp[i+1] = dp[i] + job[i+1][2]
                curE = job[i+1][1]
            else:
                maxP = dp[i]
                j = self.binarySearch(job, i, job[i+1][0])
                if j != -1 and job[i+1][2] + dp[j] > maxP and job[j][1] <= job[i+1][0]:
                    maxP = job[i+1][2] + dp[j]
                    curE = job[i+1][1]
                # for j in range(i):
                #     if job[i+1][2] + dp[j] > maxP and job[j][1] <= job[i+1][0]:
                #         maxP = job[i+1][2] + dp[j]
                #         curE = job[i+1][1]
                dp[i+1] = maxP
        return dp[-1]

if __name__ == "__main__":
    obj = Solution()
    # startTime = [1,2,3,4,6]
    # endTime = [3,5,10,6,9]
    # profit = [20,20,100,70,60]

    startTime = [1,2,3,3]
    endTime = [3,4,5,6]
    profit = [50,10,40,70]
    a = obj.jobScheduling(startTime, endTime, profit)
# @lc code=end

