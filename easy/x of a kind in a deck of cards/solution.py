from typing import List


class Solution:
    def fun_gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.fun_gcd(b, a % b)

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        n = len(deck)
        if n == 1:
            return False
        dic = {}
        i = 0
        for i in deck:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        g = dic[i]
        s = set(dic.values())
        for i in s:
            g = self.fun_gcd(max(g, i), min(g, i))
        return self.fun_gcd(max(g, i), min(g, i)) > 1


s = Solution()
print(s.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
print(s.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
