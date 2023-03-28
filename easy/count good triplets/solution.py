from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            result += 1
        return result


s = Solution()
print(s.countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
print(s.countGoodTriplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1))
