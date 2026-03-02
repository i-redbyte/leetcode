from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tz = []
        for row in grid:
            cnt = 0
            k = n - 1
            while k >= 0 and row[k] == 0:
                cnt += 1
                k -= 1
            tz.append(cnt)

        result = 0
        for i in range(n):
            need = n - 1 - i

            j = i
            while j < n and tz[j] < need:
                j += 1
            if j == n:
                return -1

            result += j - i
            while j > i:
                tz[j], tz[j - 1] = tz[j - 1], tz[j]
                j -= 1

        return result


s = Solution()
print(s.minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
print(s.minSwaps([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]))
print(s.minSwaps([[1, 0, 0], [1, 1, 0], [1, 1, 1]]))
