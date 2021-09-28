from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits == "":
            return []
        d = {"1": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"],
             "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"],
             "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]
             }
        n = len(digits)

        def recursive_computation(s: str, pos: int):
            if pos >= n:
                result.append(s)
                return
            for ch in d[digits[pos]]:
                recursive_computation(s + ch, pos + 1)

        recursive_computation('', 0)
        return result


s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations(""))
print(s.letterCombinations("2"))
