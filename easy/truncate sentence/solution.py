class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result = s.split()
        return " ".join(list(result)[:k])


s = Solution()
print(s.truncateSentence(s="Hello how are you Contestant", k=4))
print(s.truncateSentence(s="What is the solution to this problem", k=4))
print(s.truncateSentence(s="chopper is not a tanuki", k=5))
