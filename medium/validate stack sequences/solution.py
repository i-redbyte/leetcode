from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(popped)
        i = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and i < n and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == n


s = Solution()
print(s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
print(s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))
