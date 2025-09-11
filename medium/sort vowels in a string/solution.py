class Solution:

    def sortVowels(self, s: str) -> str:
        vowel_mask = 0
        for ch in "aeiou":
            vowel_mask |= 1 << (ord(ch) - 97)

        def is_vowel(c: str) -> bool:
            oc = ord(c)
            idx = (oc | 32) - 97
            return 0 <= idx < 26 and ((vowel_mask >> idx) & 1) == 1

        ascii_vowels = [ord('A'), ord('E'), ord('I'), ord('O'), ord('U'),
                        ord('a'), ord('e'), ord('i'), ord('o'), ord('u')]
        pos = {code: i for i, code in enumerate(ascii_vowels)}
        cnt = [0] * 10

        for ch in s:
            if is_vowel(ch):
                cnt[pos[ord(ch)]] += 1

        res = []
        p = 0
        for ch in s:
            if is_vowel(ch):
                while p < 10 and cnt[p] == 0:
                    p += 1
                res.append(chr(ascii_vowels[p]))
                cnt[p] -= 1
            else:
                res.append(ch)
        return "".join(res)

    def sortVowels1(self, s: str) -> str:
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
