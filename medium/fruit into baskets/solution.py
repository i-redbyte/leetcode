from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        i = j = result = 0
        f, k = fruits[0], -1
        while j < n:
            if fruits[j] != f and k == -1:
                k = fruits[j]
            elif fruits[j] != k and fruits[j] != f:
                f, k = fruits[j - 1], fruits[j]
                result = max(result, j - i)
                i = j - 1
                while fruits[i - 1] == f:
                    i -= 1
            j += 1
        result = max(result, j - i)
        return result


s = Solution()
print(s.totalFruit(fruits=[1, 2, 1]))
print(s.totalFruit(fruits=[0, 1, 2, 2]))
print(s.totalFruit([1, 2, 3, 2, 2]))
