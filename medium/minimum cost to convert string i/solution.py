from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10 ** 30
        result = 0
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            a = ord(o) - 97
            b = ord(c) - 97
            if w < dist[a][b]:
                dist[a][b] = w

        for k in range(26):
            dk = dist[k]
            for i in range(26):
                di = dist[i]
                ik = di[k]
                if ik == INF:
                    continue
                base = ik
                for j in range(26):
                    v = base + dk[j]
                    if v < di[j]:
                        di[j] = v

        for s, t in zip(source, target):
            if s == t:
                continue
            a = ord(s) - 97
            b = ord(t) - 97
            v = dist[a][b]
            if v == INF:
                return -1
            result += v
        return result


s = Solution()
print(s.minimumCost(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
                    changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20]))
print(s.minimumCost(source="aaaa", target="bbbb", original=["a", "c"], changed=["c", "b"], cost=[1, 2]))
print(s.minimumCost(source="abcd", target="abce", original=["a"], changed=["e"], cost=[10000]))
