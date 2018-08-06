class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1.0/self.myPow(x,-n)
        temp = self.myPow(x,n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return temp * temp * x

if __name__ == "__main__":
    a = Solution().myPow(2,20)
    print(a)

