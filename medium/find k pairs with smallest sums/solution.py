import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        if not nums1 or not nums2:
            return []
        n = len(nums1)
        m = len(nums2)
        for j in range(m):
            heapq.heappush(heap, [nums1[0] + nums2[j], 0, j])
        pairs = []

        while heap and k > 0:
            min_sum, i, j = heapq.heappop(heap)
            pairs.append([nums1[i], nums2[j]])
            if i + 1 < n:
                heapq.heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])
            k -= 1
        return pairs


s = Solution()
print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
print(s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
print(s.kSmallestPairs([1, 2], [3], 3))
