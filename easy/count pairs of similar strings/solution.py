from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        i = 0
        n = len(words)
        bitArr = [0] * n
        for w in words:
            b = 0
            for ch in w:
                b |= 1 << ord(ch) - ord('a')
            bitArr[i] = b
            i += 1
        result = 0
        for k in range(n):
            for j in range(k+1,n):
                if bitArr[k] == bitArr[j]:
                    result +=1
        return result


s = Solution()
print(s.similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))
print(s.similarPairs(["aabb", "ab", "ba"]))
print(s.similarPairs(["nba", "cba", "dba"]))
