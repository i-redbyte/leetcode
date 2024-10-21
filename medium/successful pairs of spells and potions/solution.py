from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        n = len(potions)
        for spell in spells:
            min_potion = (success + spell - 1) // spell
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if potions[mid] < min_potion:
                    left = mid + 1
                else:
                    right = mid
            count = n - left
            result.append(count)
        return result


s = Solution()
print(s.successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
print(s.successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))
