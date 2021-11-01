#
# @lc app=leetcode id=313 lang=python
#
# [313] Super Ugly Number
#

# @lc code=start
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [1]
        fac = [0 for _ in range(len(primes))]
        for k in range(n-1):
            imin = float("inf")
            umin = float("inf")
            for i, m in enumerate(primes):
                if dp[fac[i]] * m < umin:
                    umin = dp[fac[i]] * m
            for i, m in enumerate(primes):
                if dp[fac[i]] * m == umin:
                    fac[i] += 1
            dp.append(umin)
        return dp[-1]
        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    obj.nthSuperUglyNumber(12, [2, 7, 13, 19])
