from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        prev_sig = None

        for w in words:
            sig = [0] * 26
            for ch in w:
                sig[ord(ch) - 97] += 1

            if sig != prev_sig:
                res.append(w)
                prev_sig = sig

        return res


s = Solution()

print(s.removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"]))
print(s.removeAnagrams(["a", "b", "c", "d", "e"]))
