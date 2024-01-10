from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
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
