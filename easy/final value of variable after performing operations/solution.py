from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for s in operations:
            if "++" in s:
                x += 1
            else:
                x -= 1
        return x


s = Solution()
print(s.finalValueAfterOperations(["--X", "X++", "X++"]))
print(s.finalValueAfterOperations(["++X", "++X", "X++"]))
print(s.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))
