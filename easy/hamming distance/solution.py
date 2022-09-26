class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        for i in range(31, -1, -1):
            if (x & 1 << i) ^ (y & 1 << i):
                result += 1
        return result

    def hammingDistance1(self, x: int, y: int) -> int:
        result = 0
        v = x ^ y
        while v > 0:
            result += 1
            v = v & (v - 1)
        return result


s = Solution()
print(s.hammingDistance(1, 4))
print(s.hammingDistance(3, 1))
