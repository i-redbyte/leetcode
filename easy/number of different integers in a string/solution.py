class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        tmp = ""
        for c in word:
            if "0" <= c <= "9":
                tmp += c
            else:
                if tmp != "":
                    s.add(int(tmp))
                tmp = ""
        if tmp.isdigit():
            s.add(int(tmp))
        return len(s)


s = Solution()
print(s.numDifferentIntegers("a123bc34d8ef34"))
print(s.numDifferentIntegers("leet1234code234"))
print(s.numDifferentIntegers("a1b01c001"))
print(s.numDifferentIntegers("a1b22ff"))
print(s.numDifferentIntegers(""))
print(s.numDifferentIntegers("01,1,11"))
print(s.numDifferentIntegers("000000000"))
