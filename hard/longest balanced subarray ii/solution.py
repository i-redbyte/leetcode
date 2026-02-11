from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        size = 4 * (n + 1)
        l = [0] * size
        r = [0] * size
        mn = [0] * size
        mx = [0] * size
        lazy = [0] * size

        def build(u: int, left: int, right: int) -> None:
            l[u] = left
            r[u] = right
            mn[u] = mx[u] = 0
            lazy[u] = 0
            if left == right:
                return
            mid = (left + right) >> 1
            build(u << 1, left, mid)
            build(u << 1 | 1, mid + 1, right)

        def apply(u: int, v: int) -> None:
            mn[u] += v
            mx[u] += v
            lazy[u] += v

        def push(u: int) -> None:
            if lazy[u] != 0:
                v = lazy[u]
                apply(u << 1, v)
                apply(u << 1 | 1, v)
                lazy[u] = 0

        def pull(u: int) -> None:
            left = u << 1
            right = u << 1 | 1
            mn[u] = mn[left] if mn[left] < mn[right] else mn[right]
            mx[u] = mx[left] if mx[left] > mx[right] else mx[right]

        def modify(u: int, ql: int, qr: int, v: int) -> None:
            if ql <= l[u] and r[u] <= qr:
                apply(u, v)
                return
            push(u)
            mid = (l[u] + r[u]) >> 1
            if ql <= mid:
                modify(u << 1, ql, qr, v)
            if qr > mid:
                modify(u << 1 | 1, ql, qr, v)
            pull(u)

        def query_first(u: int, target: int) -> int:
            if l[u] == r[u]:
                return l[u]
            push(u)
            left = u << 1
            right = u << 1 | 1
            if mn[left] <= target <= mx[left]:
                return query_first(left, target)
            return query_first(right, target)

        build(1, 0, n)

        last = {}
        now = 0
        result = 0

        for i, x in enumerate(nums, start=1):
            det = 1 if (x & 1) else -1

            p = last.get(x)
            if p is not None:
                modify(1, p, n, -det)
                now -= det

            last[x] = i
            modify(1, i, n, det)
            now += det

            pos = query_first(1, now)
            if i - pos > result:
                result = i - pos

        return result


s = Solution()
print(s.longestBalanced([2, 5, 4, 3]))
print(s.longestBalanced([3, 2, 2, 5, 4]))
print(s.longestBalanced([1, 2, 3, 2]))
