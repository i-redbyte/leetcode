from typing import List
import math


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        full = (1 << n) - 1

        have = [0] * 26
        for s in stickers:
            for ch in s:
                have[ord(ch) - 97] = 1
        for ch in target:
            if not have[ord(ch) - 97]:
                return -1

        dp = [math.inf] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == math.inf:
                continue

            for s in stickers:
                super_mask = mask
                for c in s:
                    for i in range(n):
                        if ((super_mask >> i) & 1) == 0 and target[i] == c:
                            super_mask |= (1 << i)
                            break

                if super_mask != mask:
                    dp[super_mask] = min(dp[super_mask], dp[mask] + 1)

        return -1 if dp[full] == math.inf else dp[full]


s = Solution()
print(s.minStickers(stickers=["with", "example", "science"], target="thehat"))
print(s.minStickers(stickers=["notice", "possible"], target="basicbasic"))
