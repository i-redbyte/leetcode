from typing import List


class Solution:
    def max_area(self, arr: List[int]) -> int:
        stack = []
        i = 0
        max_value = 0
        while i < len(arr):
            if not stack or arr[i] >= arr[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                a = stack.pop()
                area = arr[a] * ((i - stack[-1] - 1) if stack else i)
                max_value = max(area, max_value)
        pre = stack[-1]
        while stack:
            a = stack.pop()
            area = arr[a] * ((pre - stack[-1]) if stack else pre + 1)
            max_value = max(area, max_value)
        return max_value

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        histograms = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if i == 0:
                    histograms[i][j] = int(matrix[i][j])
                else:
                    if int(matrix[i][j]) == 0:
                        histograms[i][j] = 0
                    else:
                        histograms[i][j] = histograms[i - 1][j] + int(matrix[i][j])
        k = 0
        for i in histograms:
            k = max(k, self.max_area(i))
        return k

    def max_len(self, x: int) -> int:
        i = 0
        while x:
            x = x & (x >> 1)
            i += 1
        return i

    def maximalRectangle1(self, matrix: List[List[str]]) -> int:
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
