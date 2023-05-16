from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        if len(word) == len(set(word)):
            return True
        word = list(word)
        for i in word:
            b = (word.index(i))
            if word.count(i) > 0:
                word.pop(word.index(i))
                if len(set(Counter(word).values())) == 1:
                    return True
                else:
                    word.insert(b, i)
        return False


s = Solution()
print(s.equalFrequency("abcc"))
print(s.equalFrequency("aazz"))
print(s.equalFrequency("aab"))
print(s.equalFrequency("ddaccb"))
print(s.equalFrequency("cccd"))
