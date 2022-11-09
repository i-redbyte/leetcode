class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = list("qwertyuioplkjhgfdsazxcvbnm".strip())
        for s in sentence:
            if s in alphabet:
                alphabet.remove(s)
        return len(alphabet) == 0

    def checkIfPangram2(self, sentence: str) -> bool:
        result = {}
        for s in sentence:
            result[s] = 1
        return len(result.keys()) == 26

    def checkIfPangram1(self, sentence: str) -> bool:
        alphabet = set("qwertyuioplkjhgfdsazxcvbnm")
        s = set(sentence)
        return len(alphabet.difference(s)) == 0


s = Solution()
print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(s.checkIfPangram("leetcode"))
