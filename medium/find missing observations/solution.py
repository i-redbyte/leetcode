from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        num = len(rolls) + n
        all_number = mean * num - sum(rolls)
        cond = all_number / n
        if cond > 6 or cond < 1:
            return []
        num, remainder = divmod(all_number, n)
        return [num] * (n - remainder) + [num + 1] * remainder


print(Solution().missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2))
print(Solution().missingRolls(rolls=[1, 5, 6], mean=3, n=4))
print(Solution().missingRolls(rolls=[1, 2, 3, 4], mean=6, n=4))
