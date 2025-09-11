class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        sorted_vowels = sorted([ch for ch in s if ch in vowels])
        it = iter(sorted_vowels)

        res = []
        for ch in s:
            if ch in vowels:
                res.append(next(it))
            else:
                res.append(ch)
        return "".join(res)


s = Solution()
print(s.sortVowels("lEetcOde"))
print(s.sortVowels("lYmpH"))
