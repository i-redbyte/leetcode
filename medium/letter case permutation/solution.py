from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)

        def solution(res: List[str], index: int, s: List[str]):
            if index == n:
                res.append(''.join(s))
                return
            solution(res, index + 1, s)
            if s[index].isalpha():
                s[index] = chr(ord(s[index]) ^ (1 << 5))
                solution(res, index + 1, s)

        result = []
        solution(result, 0, list(s))
        return result


s = Solution()
print(s.letterCasePermutation("a1b2"))
print(s.letterCasePermutation("3z4"))
