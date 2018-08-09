class Solution:
    def plusOne(self, digits):
        if len(digits) == 0:
            return [1]
        else:
            s = 0
            for i in digits:
                s = s*10 + i
            s = s + 1
            l=[]
            while s != 0:
                l.append(s%10)
                s = s // 10   
            return l[::-1]


if __name__ == '__main__':
    a = Solution().plusOne([1,2,9])
    print(a)

