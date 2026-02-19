from typing import List


class Solution:
    def nextGreatestLetter(self, letters, target):
        l, r = 0, len(letters)
        while l < r:
            m = (l + r) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m
        return letters[l % len(letters)]

    def nextGreatestLetter1(self, letters: List[str], target: str) -> str:
        result = letters[0]
        t = ord(target)
        tmp = 256
        for ch in letters:
            current = ord(ch)
            if ord(ch) > t:
                x = current - t
                if x < tmp:
                    tmp = x
                    result = ch
        return result


s = Solution()
print(s.nextGreatestLetter(letters=["c", "f", "j"], target="a"))
print(s.nextGreatestLetter(letters=["c", "f", "j"], target="c"))
print(s.nextGreatestLetter(letters=["x", "x", "y", "y"], target="z"))
