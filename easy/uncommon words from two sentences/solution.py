from typing import List
from collections import Counter


class Solution:

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []
        s = (s1 + ' ' + s2).split()
        d = Counter(s)
        for k, v in d.items():
            if v == 1:
                result.append(k)
        return result


s = Solution()
print(s.uncommonFromSentences(s1="this apple is sweet", s2="this apple is sour"))
print(s.uncommonFromSentences(s1="apple apple", s2="banana"))
