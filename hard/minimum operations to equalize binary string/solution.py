from collections import deque


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        cnt0 = s.count('0')
        if cnt0 == 0:
            return 0

        parents = []
        sizes = []
        for parity in (0, 1):
            m = (n - parity) // 2 + 1  # сколько чисел этой чётности в [0..n]
            sizes.append(m)
            parents.append(list(range(m + 1)))  # m = sentinel (конец)

        def find(parity: int, x: int) -> int:
            p = parents[parity]
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x

        def erase_val(val: int) -> None:
            parity = val & 1
            idx = (val - parity) // 2
            if 0 <= idx < sizes[parity]:
                parents[parity][idx] = find(parity, idx + 1)

        # стартовое состояние уже "посещено"
        erase_val(cnt0)

        q = deque([cnt0])
        steps = 0

        while q:
            for _ in range(len(q)):
                x = q.popleft()
                if x == 0:
                    return steps

                l = x + k - 2 * min(x, k)
                r = x + k - 2 * max(0, k - n + x)
                parity = l & 1

                lo = (l - parity) // 2
                hi = (r - parity) // 2
                if lo < 0:
                    lo = 0
                if hi >= sizes[parity]:
                    hi = sizes[parity] - 1
                if lo > hi:
                    continue

                idx = find(parity, lo)
                while idx <= hi:
                    y = parity + 2 * idx
                    q.append(y)
                    parents[parity][idx] = find(parity, idx + 1)  # удалить y
                    idx = find(parity, idx)

            steps += 1

        return -1


s = Solution()
print(s.minOperations(s="110", k=1))
print(s.minOperations(s="0101", k=3))
print(s.minOperations(s="101", k=2))
