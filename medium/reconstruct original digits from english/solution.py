from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        # numbers_dict = {0: "zero", 1: "one", 2: "two",
        #                 3: "three", 4: "four", 5: "five",
        #                 6: "six", 7: "seven", 8: "eight",
        #
        digits = {
            'z': [0],
            'w': [2],
            'u': [4],
            'x': [6],
            'g': [8],
            'h': [8, 3],
            'f': [4, 5],
            's': [6, 7],
            'o': [0, 2, 4, 1],
            'i': [5, 6, 8, 9],
        }
        counter = [0] * 10

        for ch in s:
            if ch in digits:
                counter[digits[ch][-1]] += 1
        meet_more_than_once = 'hfsoi'
        for ch in meet_more_than_once:
            counter[digits[ch][-1]] -= sum(counter[i] for i in digits[ch][:-1])
        return ''.join([str(i) * c for i, c in enumerate(counter) if c])


s = Solution()
print(s.originalDigits("owoztneoer"))
print(s.originalDigits("fviefuro"))
