class Solution:
    def countPoints(self, rings: str) -> int:
        result = 0
        r, g, b = set(), set(), set()
        n = len(rings)
        for i in range(0, n, 2):
            k = i + 1
            if rings[i] == 'R':
                r.add(rings[k])
            elif rings[i] == 'G':
                g.add(rings[k])
            elif rings[i] == 'B':
                b.add(rings[k])
        for i in r:
            if i in g and i in b:
                result += 1
        return result


s = Solution()
print(s.countPoints("B0B6G0R6R0R6G9"))
print(s.countPoints("B0R0G0R9R0B0G0"))
print(s.countPoints("G4"))
