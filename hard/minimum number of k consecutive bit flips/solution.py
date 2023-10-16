from collections import deque
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        acc, flag = [0] * n, 0
        for i, num in enumerate(nums):
            if i >= k:
                flag ^= acc[i - k]

            if flag != num:
                continue
            if k > n - i:
                return -1
            flag ^= 1
            acc[i] = 1
        return sum(acc)

    def minKBitFlips2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        flip_count = 0
        flip_needed = [False] * n

        for i in range(n):
            if i >= k:
                flip_count -= flip_needed[i - k]
            if (nums[i] + flip_count) % 2 == 0:
                if i + k > n:
                    return -1
                flips += 1
                flip_count += 1
                flip_needed[i] = True

        return flips

    def minKBitFlips1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        flip_queue = deque()

        for i in range(n):
            if flip_queue and i >= flip_queue[0] + k:
                flip_queue.popleft()
            if nums[i] == 0 and (len(nums) - i) >= k:
                flips += 1
                flip_queue.append(i)

                for j in range(i, i + k):
                    nums[j] ^= 1
            elif nums[i] == 0:
                return -1

        return flips


s = Solution()
print(s.minKBitFlips(nums=[0, 1, 0], k=1))
print(s.minKBitFlips([1, 1, 0], k=2))
print(s.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], k=3))
