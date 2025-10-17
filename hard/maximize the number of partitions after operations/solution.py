from functools import lru_cache
import sys


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        sys.setrecursionlimit(1 << 25)

        n = len(s)
        bits = [1 << (ord(c) - 97) for c in s]

        def popcount(x: int) -> int:
            return x.bit_count() if hasattr(int, "bit_count") else bin(x).count("1")

        @lru_cache(maxsize=None)
        def dp(i: int, can_change: bool, mask: int) -> int:
            if i == n:
                return 0

            def step(new_bit: int, next_can_change: bool) -> int:
                new_mask = mask | new_bit
                if popcount(new_mask) > k:
                    return 1 + dp(i + 1, next_can_change, new_bit)
                else:
                    return dp(i + 1, next_can_change, new_mask)

            best = step(bits[i], can_change)

            if can_change:
                for j in range(26):
                    best = max(best, step(1 << j, False))

            return best

        return dp(0, True, 0) + 1


s = Solution()
print(s.maxPartitionsAfterOperations(s="accca", k=2))
print(s.maxPartitionsAfterOperations(s="aabaab", k=3))
print(s.maxPartitionsAfterOperations(s="xxyz", k=1))
