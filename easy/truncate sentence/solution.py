class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result = ""
        count_word = 0
        for ch in s:
            if ch == ' ':
                count_word += 1
                if count_word == k:
                    return result
            result += ch
        return result

    def truncateSentence2(self, s: str, k: int) -> str:
        result = ""
        p = 0
        start = 0
        n = len(s)
        while p < k:
            p += 1
            for i in range(start, n):
                result += s[i]
                start += 1
                if s[i] == ' ':
                    break
        return result.rstrip()

    def truncateSentence1(self, s: str, k: int) -> str:
        result = s.split()
        return " ".join(list(result)[:k])


s = Solution()
print(s.truncateSentence(s="Hello how are you Contestant", k=4))
print(s.truncateSentence(s="What is the solution to this problem", k=4))
print(s.truncateSentence(s="chopper is not a tanuki", k=5))
