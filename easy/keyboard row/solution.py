from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def bitset(word):
            r = 0
            for c in word:
                r |= 1 << (ord(c) - 97)
            return r

        row1 = bitset('qwertyuiop')
        row2 = bitset('asdfghjkl')
        row3 = bitset('zxcvbnm')
        result = []
        for word in words:
            s = bitset(word.casefold())
            if s & (row1 | row2) < 1 or s & (row1 | row3) < 1 or s & (row2 | row3) < 1:
                result.append(word)
        return result

    def findWords1(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        result = []
        for w in words:
            for r in rows:
                if len(set(w.lower()) - r) == 0:
                    result.append(w)
                    break
        return result


s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
print(s.findWords(["omk"]))
print(s.findWords(["adsdf", "sfd"]))
