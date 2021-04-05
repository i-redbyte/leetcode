class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            if n & 1 == 1:
                result += 1
            n = n >> 1
        return result


s = Solution()
print(s.hammingWeight(1))
print(s.hammingWeight(10))
print(s.hammingWeight(7))
print(s.hammingWeight(0))
