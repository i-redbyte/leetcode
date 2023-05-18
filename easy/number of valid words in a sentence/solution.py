class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentence = sentence.split(' ')
        result = 0
        for word in sentence:
            add = hyphen = 0
            n = len(word)
            for idx, i in enumerate(word):
                if i in '0123456789' or i in '!,.' and idx != n - 1:
                    add = 0
                    break

                if i == '-':
                    if idx == 0 or idx == n - 1 or not word[idx - 1].islower() or not word[idx + 1].islower():
                        add = 0
                        break
                    hyphen += 1

                if hyphen > 1:
                    add = 0
                    break
                add = 1
            if add == 1:
                result += 1
        return result


s = Solution()
print(s.countValidWords("cat and  dog"))
print(s.countValidWords("!this  1-s b8d!"))
print(s.countValidWords("alice and  bob are playing stone-game10"))
