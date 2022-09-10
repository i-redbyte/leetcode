from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        count = 0
        start = 0
        while count < n:
            current = start
            prev = nums[start]

            while True:
                next = (current + k) % n
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1

                if start == current:
                    break
            start += 1

    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = a[i]

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]


s = Solution()
s.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
