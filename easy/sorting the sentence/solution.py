class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        n = len(words)
        result = [None] * n
        for i in range(n):
            v = int(words[i][-1])-1
            result[v] = words[i][:-1]

        return " ".join(result)


s = Solution()
print(s.sortSentence("is2 sentence4 This1 a3"))
print(s.sortSentence("Myself2 Me1 I4 and3"))
