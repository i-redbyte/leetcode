from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        union(0, firstPerson)

        meetings.sort(key=lambda x: x[2])
        m = len(meetings)
        i = 0

        while i < m:
            t = meetings[i][2]
            participants = set()

            j = i
            while j < m and meetings[j][2] == t:
                a, b, _ = meetings[j]
                union(a, b)
                participants.add(a)
                participants.add(b)
                j += 1

            root0 = find(0)
            for x in participants:
                if find(x) != root0:
                    parent[x] = x
                    size[x] = 1

            i = j

        root0 = find(0)
        return [p for p in range(n) if find(p) == root0]


s = Solution()
print(s.findAllPeople(n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1))
print(s.findAllPeople(n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3))
print(s.findAllPeople(n=5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson=1))
