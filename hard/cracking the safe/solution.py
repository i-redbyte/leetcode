class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        result = list()
        nodeNum = k ** (n - 1)
        sides = [k - 1] * nodeNum

        node = 0
        while sides[node] >= 0:
            side = sides[node]
            sides[node] -= 1
            node = (node * k + side) % nodeNum
            result.append(str(side))
        return "0" * (n - 1) + "".join(result)


s = Solution()
print(s.crackSafe(n=1, k=2))
print(s.crackSafe(n=2, k=2))
