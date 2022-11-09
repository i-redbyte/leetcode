class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set("qwertyuioplkjhgfdsazxcvbnm")
        s = set(sentence)
        return len(alphabet.difference(s)) == 0


s = Solution()
print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(s.checkIfPangram("leetcode"))
