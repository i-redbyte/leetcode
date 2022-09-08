from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words):
        d = {
            "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
            "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
            "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
        }

        n = len(words)
        for i in range(n):
            words[i] = "".join([d[c] for c in words[i]])
        return len(set(words))

    def uniqueMorseRepresentations2(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        s = set("")
        for w in words:
            code = []
            for ch in w:
                code.append(morse[ord(ch) - ord('a')])
            s.add(''.join(code))
        return len(s)

    def uniqueMorseRepresentations1(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        result = {"".join(morse[ord(c) - ord('a')] for c in word)
                  for word in words}
        return len(result)


s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
print(s.uniqueMorseRepresentations(["a"]))
