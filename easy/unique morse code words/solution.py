from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        seen = {"".join(morse[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)


s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
print(s.uniqueMorseRepresentations(["a"]))
