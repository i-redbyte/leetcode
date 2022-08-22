from typing import List


class Solution:
    def getSetBits(self, x: int) -> int:
        result = 0
        while x != 0:
            x = x & (x - 1)
            result += 1
        return result

    def sortByBits1(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        n = len(arr)
        maxNumber = -999999999
        result = []
        for i in range(n):
            maxNumber = max(maxNumber, self.getSetBits(arr[i]))
        k = 0
        while k <= maxNumber:
            for i in range(n):
                if self.getSetBits(arr[i]) == k:
                    result.append(arr[i])
            k += 1
        return result


print(Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(Solution().sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
