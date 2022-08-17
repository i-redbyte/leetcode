from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        s = set(words[0])
        for ch in s:
            count = words[0].count(ch)
            entry = 1
            n = len(words)
            for i in range(1, n):
                if ch in words[i]:
                    count = min(count, words[i].count(ch))
                    entry += 1
                else:
                    break
            if entry == n:
                for i in range(count):
                    result.append(ch)
        return result

    def commonChars1(self, words: List[str]) -> List[str]:
        result = list(words[0])
        for w in words[1:]:
            tmp = []
            for c in w:
                if c in result:
                    tmp.append(c)
                    result.remove(c)
            result = tmp
        return result


print(Solution().commonChars(["bella", "label", "roller"]))
print(Solution().commonChars(["cool", "lock", "cook"]))
