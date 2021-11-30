from typing import List


class Solution:
    def max_len(self, x: int) -> int:
        i = 0
        while x:
            x = x & (x >> 1)
            i += 1
        return i

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        result = 0
        s = []
        for x in map(lambda vec: int(''.join(vec), 2), matrix):
            x_len = self.max_len(x)
            if x_len == 0:
                s.clear()
                continue
            result = max(result, x_len)
            stack = [x]
            for i, y in enumerate(s, 2):
                y = y & x
                if y == 0:
                    break
                y_len = self.max_len(y)
                result = max(result, y_len * i)
                stack.append(y)
            s.clear()
            s = stack
        return result


s = Solution()
print(s.maximalRectangle(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))

print(s.maximalRectangle(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
print(s.maximalRectangle([["1"]]))
print(s.maximalRectangle([["0", "0"]]))
