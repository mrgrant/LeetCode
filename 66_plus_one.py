class Solution:
    def plusOne(self, digits):
        res = []
        if digits[-1] != 9:
            digits [-1] = digits[-1] + 1
            res = digits
        else:
            num = 0
            digits.reverse()
            for i in range(len(digits)):
                num = num + digits[i]*(10**i)
            num = str(num+1)
            for j in num:
                res.append(int(j))
        return res



if __name__ == '__main__':
    a = Solution().plusOne([1,2,9])
    print(a)

