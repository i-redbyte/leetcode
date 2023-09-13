from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic, stack, result = {}, [], []
        s = nums2[::-1]
        for num in s:
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                dic[num] = stack[-1]
            stack.append(num)
        for num in nums1:
            result.append(dic.get(num, -1))
        return result


s = Solution()
print(s.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(s.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))
