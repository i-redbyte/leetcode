from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr) - 1
        arr.sort()
        delta = 999999999999999
        result = []
        for i in range(n):
            current_delta = arr[i + 1] - arr[i]
            if delta == current_delta:
                result.append([arr[i], arr[i + 1]])
            elif delta > current_delta:
                delta = current_delta
                result = [[arr[i], arr[i + 1]]]
        return result


s = Solution()
print(s.minimumAbsDifference([4, 2, 1, 3]))
print(s.minimumAbsDifference([1, 3, 6, 10, 15]))
print(s.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
