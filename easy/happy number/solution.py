class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        d = {}
        while n > 0:
            s = 0
            while n > 0:
                x = n % 10
                s += x * x
                n = n // 10
            n = s
            if n in d:
                d[n] = d[n] + 1
            else:
                d[n] = 1
            if d[n] > 1:
                return False
            if n == 1:
                return True
        return False


s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))
