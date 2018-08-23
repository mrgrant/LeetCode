class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = []

        def squared(n):
            num = []
            while n != 0:
                num.append(n % 10)
                n = n // 10
            squares = [x ** 2 for x in num]
            return sum(squares)

        while squared(n) != 1:
            l = squared(n)
            if l in seen:
                return False
            seen.append(l)
            n = l
        return True


if __name__ == '__main__':
    a = Solution().isHappy(20)
    print(a)
