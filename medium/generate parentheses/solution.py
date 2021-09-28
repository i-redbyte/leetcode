from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        max_len = 2 * n

        def recursive_computation(s: List[str], left: int, right: int):
            if len(s) == max_len:
                result.append("".join(s))
                return
            if left < n:
                s.append("(")
                recursive_computation(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(")")
                recursive_computation(s, left, right + 1)
                s.pop()

        recursive_computation([], 0, 0)
        return result


s = Solution()
print(s.generateParenthesis(3))
# print(s.generateParenthesis(1))
