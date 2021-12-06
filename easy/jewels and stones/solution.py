class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        for jew in jewels:
            for s in stones:
                if jew == s:
                    if jew in d:
                        d[jew] += 1
                    else:
                        d[jew] = 1
        return sum(d.values())


s = Solution()

print(s.numJewelsInStones("aA", "aAAbbbb"))
print(s.numJewelsInStones("z", "ZZ"))
