class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        result = 1
        c = 1
        while n > 0:
            n -= 1
            tmp = result + c
            result = c
            c = tmp
        return result


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(10))
print(s.climbStairs(45))
