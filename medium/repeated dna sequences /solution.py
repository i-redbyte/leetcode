from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s):
        r, record = set(), set()
        n = len(s) - 9
        for i in range(n):
            substring = s[i:i + 10]
            [record, r][substring in record].add(substring)
        return list(r)

    def findRepeatedDnaSequences1(self, s: str) -> List[str]:
        len_s = len(s)
        if len_s < 10:
            return []
        dnas = set()
        result = set()
        n = len_s - 9
        for i in range(n):
            v = s[i:i + 10]
            if v in dnas:
                result.add(v)
            else:
                dnas.add(v)
        return list(result)


s = Solution()
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(s.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
