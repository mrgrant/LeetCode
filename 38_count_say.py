class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        pre = '11'
        for i in range(3,n+1):
            res = ''
            cnt = 1
            for j in range(1,len(pre)):
                if pre[j] == pre[j-1]:
                    cnt += 1
                else:
                    res += str(cnt)+pre[j-1]
                    cnt = 1
            res += str(cnt) + pre[j]
            pre = res
        return res  
