from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        N = n - 1

        def nCk_small(a, b):
            if b < 0 or b > a:
                return 0
            if b == 0 or b == a:
                return 1
            num = 1
            den = 1
            for i in range(1, b + 1):
                num *= a - (i - 1)
                den *= i
            return num // den

        c5 = [[0] * 5 for _ in range(5)]
        for a in range(5):
            for b in range(a + 1):
                c5[a][b] = nCk_small(a, b) % 5

        s2 = 0
        s5 = 0
        for i, v in enumerate(nums):
            v %= 10
            if (i & N) == i:
                s2 = (s2 + (v & 1)) & 1
            x = N
            y = i
            cn5 = 1
            while x > 0 or y > 0:
                ax = x % 5
                by = y % 5
                if by > ax:
                    cn5 = 0
                    break
                cn5 = (cn5 * c5[ax][by]) % 5
                x //= 5
                y //= 5
            s5 = (s5 + v * cn5) % 5

        return (5 * s2 + 6 * s5) % 10

    def triangularSum1(self, nums: List[int]) -> int:
        n = len(nums)
        for end in range(n - 1, 0, -1):
            for i in range(end):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        return nums[0]


s = Solution()
print(s.triangularSum([1, 2, 3, 4, 5]))
print(s.triangularSum([5]))
