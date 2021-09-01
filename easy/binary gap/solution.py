class Solution:
    def binaryGap(self, n: int) -> int:
        max_sum = 0
        current = 0
        count = 0
        while n != 0:
            if n & 1:
                count += 1
                max_sum = max(current, max_sum)
                current = 0
            else:
                if count > 0:
                    current += 1
            n = n >> 1
        return max_sum + 1 if count > 1 else 0

    def binaryGap2(self, n: int) -> int:
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
print(s.binaryGap(140))
