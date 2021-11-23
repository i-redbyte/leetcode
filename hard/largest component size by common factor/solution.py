import collections
from typing import List


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        primes = []
        for x in range(2, int(max(nums) ** 0.5) + 1):
            for y in primes:
                if x % y == 0:
                    break
            else:
                primes.append(x)

        factors = collections.defaultdict(list)
        for a in nums:
            x = a
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    factors[a].append(p)
                    while x % p == 0:
                        x //= p
            if x > 1:
                factors[a].append(x)
                primes.append(x)

        primes = list(set(primes))
        n = len(primes)
        p2i = {p: i for i, p in enumerate(primes)}

        parent = [i for i in range(n)]

        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            pi, pj = find(i), find(j)
            if pi != pj:
                parent[pi] = pj

        for a in nums:
            if factors[a]:
                p0 = factors[a][0]
                for p in factors[a][1:]:
                    union(p2i[p0], p2i[p])

        count = collections.Counter(
            find(p2i[factors[a][0]]) for a in nums if factors[a])
        return max(count.values())


s = Solution()
print(s.largestComponentSize([4, 6, 15, 35]))
print(s.largestComponentSize([20, 50, 9, 63]))
print(s.largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39]))
