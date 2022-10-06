class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        start = 1
        result = left
        while start <= left:
            start <<= 1
        if start <= right:
            return 0
        i = left + 1
        while i <= right and i <= start:
            result &= i
            i += 1
        return result


s = Solution()
print(s.rangeBitwiseAnd(5, 7))
print(s.rangeBitwiseAnd(0, 0))
print(s.rangeBitwiseAnd(left=1, right=2147483647))
