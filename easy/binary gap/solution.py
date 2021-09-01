class Solution:
    def binaryGap(self, n: int) -> int:
        result = 0
        end = -999999
        for i in range(32):
            if (n >> i) & 1:
                if end != -999999:
                    result = max(result, i - end)
                end = i
        return result


s = Solution()
print(s.binaryGap(22))
print(s.binaryGap(5))
print(s.binaryGap(6))
print(s.binaryGap(8))
print(s.binaryGap(1))
