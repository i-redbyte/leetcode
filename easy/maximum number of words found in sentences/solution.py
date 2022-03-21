from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for line in sentences:
            result = max(result, len(line.split(" ")))
        return result


s = Solution()
print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print(s.mostWordsFound(["please wait", "continue to fight", "continue to win"]))
